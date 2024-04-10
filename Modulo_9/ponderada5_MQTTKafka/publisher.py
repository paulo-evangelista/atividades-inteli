import paho.mqtt.client as mqtt
import time
import struct
import json
import random

broker_address = "9b03d9bd4c824818a952674932512448.s1.eu.hivemq.cloud"
broker_port = 8883 

mqtt_username = "pytest"
mqtt_password = "Pytest123"

topic = "data"

def simulate_sps30_data(previous_message_id=0):
    data = {
        "message_id": previous_message_id + 1,
        "mc_pm1_0": random.randint(20, 100),
        "mc_pm2_5": random.randint(30, 60),
        "mc_pm4_0": random.randint(10, 30),
        "mc_pm10": random.randint(15, 25),
    }
    return json.dumps(data)

def on_connect(mqttc, obj, flags, reason_code, properties):
    print(f"Connected with reason code: {reason_code}\n")

def on_publish(mqttc, obj, mid, reason_code, properties):
    print(f"Message ID: {mid} published")

def on_message(mqttc, obj, msg):
    print(f"{msg.topic} {msg.qos} {msg.payload}")

client = mqtt.Client(protocol=mqtt.MQTTv5, callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message

client.username_pw_set(mqtt_username, mqtt_password)

client.tls_set() 
client.connect(broker_address, broker_port, 60)

client.loop_start()

print("Connecting to broker...")

try:
    message_id = 0
    while True:
        sensor_data = simulate_sps30_data(message_id)
        info = client.publish(topic, sensor_data, qos=1)
        info.wait_for_publish()
        message_id += 1
        print(f"Sent on topic: {topic}")
        print(f"{sensor_data}\n")
        time.sleep(1)

except KeyboardInterrupt:
    client.disconnect()
    print("Simulation stopped")
