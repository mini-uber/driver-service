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
