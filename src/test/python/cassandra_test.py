import uuid
from cassandra.cluster import Cluster

# Connect to Cassandra
cluster = Cluster(['localhost'])
session = cluster.connect()

# Create keyspace
session.execute("CREATE KEYSPACE IF NOT EXISTS test_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}")

# Use keyspace
session.set_keyspace('test_keyspace')

# Create table
session.execute("CREATE TABLE IF NOT EXISTS test_table (id UUID PRIMARY KEY, name TEXT)")

# Insert data
insert_query = session.prepare("INSERT INTO test_table (id, name) VALUES (?, ?)")
session.execute(insert_query, [uuid.uuid4(), 'John Doe'])
session.execute(insert_query, [uuid.uuid4(), 'Jane Smith'])

# Query data
rows = session.execute("SELECT * FROM test_table")
for row in rows:
    print("Test subject: " + str(row.id) + str(row.name))

# Close connection
cluster.shutdown()
