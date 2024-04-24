'''
import requests

# Base URL of your Spring Boot application
BASE_URL = "http://localhost:8080/api/v1/drivers"

# Function to send a POST request to create a new driver
def create_driver(name):
    data = {"name": name}
    response = requests.post(BASE_URL, json=data)
    return response

# Function to send a DELETE request to remove a driver by ID
def remove_driver(driver_id):
    url = f"{BASE_URL}/{driver_id}"
    response = requests.delete(url)
    return response

# Test create driver functionality
print("Creating driver...")
create_response = create_driver("John Doe")
if create_response.status_code == 201:
    print("Driver created successfully!")
    driver_id = create_response.json()["id"]
else:
    print("Failed to create driver.")
    exit(1)

# Test remove driver functionality
print(f"Removing driver with ID: {driver_id}")
remove_response = remove_driver(driver_id)
if remove_response.status_code == 204:
    print("Driver removed successfully!")
else:
    print("Failed to remove driver.")
    exit(1)

# Test Kafka integration (assuming Kafka is running locally)
print("Testing Kafka integration...")
# You can add test cases here to send requests and verify Kafka messages

print("All tests passed successfully!")
'''

import requests
from confluent_kafka import Producer, Consumer


def test_api_endpoints():
    base_url = "http://localhost:8080/api/v1/drivers"

    # Test POST /create
    create_url = f"{base_url}/create"
    driver_data = {"id": 1, "name": "John Doe", "location": "New York", "availability": True}
    response = requests.post(create_url, json=driver_data)
    print("POST /create Status Code:", response.status_code)
    created_driver = response.json()
    print("Created Driver:", created_driver)

    # Test DELETE /delete/{id}
    delete_url = f"{base_url}/delete/1"
    response = requests.delete(delete_url)
    print("DELETE /delete/{id} Status Code:", response.status_code)

    # Test Kafka listeners (assuming Kafka is running locally)
    # You need to adjust the Kafka configurations based on your setup
    kafka_update_driver_location_topic = "update-driver-location"
    kafka_update_driver_availability_topic = "update-driver-availability"
    kafka_get_all_drivers_topic = "get-all-drivers"

    # Kafka producer configuration
    kafka_producer_conf = {"bootstrap.servers": "localhost:9092"}

    # Produce messages for Kafka topics
    producer = Producer(kafka_producer_conf)

    # Produce message for update-driver-location topic
    producer.produce(kafka_update_driver_location_topic, key=str("1"), value="New York|||1")
    producer.flush()

    # Produce message for update-driver-availability topic
    producer.produce(kafka_update_driver_availability_topic, key=str("1"), value="1|||true")
    producer.flush()

    # Produce message for get-all-drivers topic
    producer.produce(kafka_get_all_drivers_topic, key=None, value=None)
    producer.flush()

    # Kafka consumer configuration
    kafka_consumer_conf = {"bootstrap.servers": "localhost:9092", "group.id": "test_group"}

    # Kafka consumer for update-driver-updates topic
    consumer = Consumer(kafka_consumer_conf)
    consumer.subscribe([kafka_update_driver_location_topic, kafka_update_driver_availability_topic])

    # Consume messages
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue
        print("Consumed message: topic={}, partition={}, offset={}, key={}, value={}".format(
            msg.topic(), msg.partition(), msg.offset(), msg.key().decode("utf-8"), msg.value().decode("utf-8")))
        if msg.topic() == kafka_update_driver_location_topic and msg.key() == str("1").encode("utf-8"):
            break
        if msg.topic() == kafka_update_driver_availability_topic and msg.key() == str("1").encode("utf-8"):
            break

    # Unsubscribe from topics and close consumer and producer
    consumer.unsubscribe()
    consumer.close()
    producer.close()


if __name__ == "__main__":
    test_api_endpoints()
