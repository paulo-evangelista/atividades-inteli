from kafka import KafkaProducer
import time
import random
import json
import math

print("starting producer..")

producer = KafkaProducer(bootstrap_servers='localhost:9092')
try:
    for i in range(50):
        print("creating simulated data..")

        data = json.dumps({
            "idSensor": "sensor_001",
            "timestamp": math.ceil(time.time()),
            "tipoPoluente": "PM2.5",
            "nivel": random.randint(20,50)
        })  

        print(data)

        print("saving message...")
        producer.send('sensordata', data.encode())
        print("message added.\n")

    producer.flush()
    print("\nflushed all messages!\n")
    
    print("closing producer...")
    producer.close()
    print("gracefully stopped.")

except KeyboardInterrupt:
    print("closing producer...")
    producer.close()
    print("gracefully stopped.")