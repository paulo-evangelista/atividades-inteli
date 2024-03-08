import paho.mqtt.client as mqtt
import time
import struct
import json
import random

broker_address = "localhost"
broker_port = 1883 

mqtt_username = "pytest"
mqtt_password = "Pytest123"

topic = "sensor/readings"

def simulate_data(last_temp, tipo):
    data = {
        "tipo": tipo,
        "temperatura": last_temp + random.uniform(-0.5,+0.5),
        "timestamp": time.time(),
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

client.connect(broker_address, broker_port, 60)

client.loop_start()

try:
    last_temp_1 = 5
    last_temp_2 = 3
    last_temp_3 = -11
    last_temp_4 = -22
    while True:
        s1 = simulate_data(last_temp_1, "geladeira 1")
        s2 = simulate_data(last_temp_2, "geladeira 2")
        s3 = simulate_data(last_temp_3, "freezer 1")
        s4 = simulate_data(last_temp_4, "freezer 2")

        info = client.publish(topic, s1, qos=1)
        info.wait_for_publish()

        info = client.publish(topic, s2, qos=1)
        info.wait_for_publish()

        info = client.publish(topic, s3, qos=1)
        info.wait_for_publish()

        info = client.publish(topic, s4, qos=1)
        info.wait_for_publish()

        print(f"Sent all messages on topic: {topic}")
        print(f"{s4}\n")
        time.sleep(5)

except KeyboardInterrupt:
    client.disconnect()
    print("Simulation stopped")
