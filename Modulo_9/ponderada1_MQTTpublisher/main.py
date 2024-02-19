import paho.mqtt.client as mqtt
import time
import struct
import json

broker_address = "broker.emqx.io"
broker_port = 1883
topic = "sensor/sps30"

def simulate_sps30_data():
    import random
    data = {
        "mc_pm1_0": struct.pack(">I", random.randint(0, 100)),
        "mc_pm2_5": struct.pack(">I", random.randint(0, 100)),
        "mc_pm4_0": struct.pack(">I", random.randint(0, 100)),
        "mc_pm10": struct.pack(">I", random.randint(0, 100)),
    }
    hex_data = {k: v.hex() for k, v in data.items()}
    return json.dumps(hex_data)

def on_connect(mqttc, obj, flags, reason_code, properties):
    print("reason_code: " + str(reason_code)+"\n")
def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
def on_publish(mqttc, obj, mid, reason_code, properties):
    print("message ID: " + str(mid))

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2,reconnect_on_failure=True, client_id="paulo-sps30-sensor")

client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message

client.connect(broker_address, broker_port, 60)

print("connecting to broker...")
connection = client.loop_start()

if connection == 0:
    print("connected to broker at:", broker_address)

try:
    while True:
        sensor_data = simulate_sps30_data()
        info = client.publish(topic, sensor_data, qos=1)
        mid = info.wait_for_publish()
        print("sent on topic:", topic)
        print(sensor_data, "\n")
        time.sleep(2)

except KeyboardInterrupt:
    client.disconnect()
    print("Simulation stopped")
