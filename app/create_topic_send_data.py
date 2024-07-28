from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
import json
import time
import random

# Kafka configuration
bootstrap_servers = ['172.25.0.12:9092', '172.25.0.13:9092']
topic = 'weather_data'

# Create Kafka admin client to manage topics
admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

# Check if the topic exists and create it if not
existing_topics = admin_client.list_topics()
if topic not in existing_topics:
    topic_list = [NewTopic(name=topic, num_partitions=1, replication_factor=1)]
    admin_client.create_topics(new_topics=topic_list, validate_only=False)

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Function to generate weather data
def generate_data():
    return {
        'temperature': round(random.uniform(20.0, 30.0), 2),
        'humidity': round(random.uniform(30.0, 70.0), 2),
        'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
    }

# Send weather data to the Kafka topic continuously
while True:
    data = generate_data()
    producer.send(topic, value=data)
    time.sleep(1)
