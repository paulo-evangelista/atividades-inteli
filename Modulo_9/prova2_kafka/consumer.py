import pytest
from pymongo import MongoClient
from kafka import KafkaConsumer
import json


@pytest.fixture()
def mongo_client():
    mongoClient = MongoClient('mongodb://localhost:27017/')
    yield mongoClient
    mongoClient.close()

@pytest.fixture()
def kafka_consumer():
    print("creating Kafka consumer...")
    kafkaConsumer = KafkaConsumer(
            'sensordata',
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            group_id='my-sensor-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
    yield kafkaConsumer
    kafkaConsumer.close()

def test_data(mongo_client, kafka_consumer):

    db = mongo_client['sensor_database']
    collection = db['sensordata']

    inserted_count = 0

    print("Running consumer...")
    msg_pack = kafka_consumer.poll(timeout_ms=10000)
    for tp, messages in msg_pack.items():
        for message in messages:
            collection.insert_one(message.value)
            inserted_count += 1

    db = mongo_client['sensor_database']
    collection = db['sensordata']

    print("kafka reported consuming {} messages".format(inserted_count))

    
    print("\nasserting that all messages read by kafka were written to Mongo...")
    assert collection.count_documents({}) == inserted_count, "Document count is incorrect"
    print("DONE")

    print("\nasserting object structure...")
    for doc in collection.find():
        assert all(key in doc for key in ["idSensor", "timestamp", "tipoPoluente", "nivel"]), "Document structure is incorrect "
    print("DONE")
