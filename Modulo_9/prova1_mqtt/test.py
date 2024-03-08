import pytest
import paho.mqtt.client as mqtt
import time
import json

broker_address = "localhost"
broker_port = 1883
topic = "sensor/readings"


class MQTTClient:
    def __init__(self):
        self.client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2,reconnect_on_failure=True, client_id="pytest")
        self.received_messages = []

    def on_connect(self, mqttc, obj, flags, reason_code, properties):
        print("Connected")
        self.client.subscribe(topic)

    def on_message(self, client, userdata, msg):
        self.received_messages.append((msg.payload, time.time()))

    def connect(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(broker_address, broker_port, 60)
        self.client.loop_start()

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()

@pytest.fixture
def mqtt_client():
    client = MQTTClient()
    client.connect()
    yield client
    client.disconnect()

def test_recebimento(mqtt_client):
    time.sleep(10)
    assert len(mqtt_client.received_messages) > 0, "Nenhuma mensagem recebida"

def test_validacao_dos_campos(mqtt_client):
    for payload, _ in mqtt_client.received_messages:
        data = json.loads(payload)
        assert all(key in data for key in ["tipo", "timestamp", "temperatura"]), "Dados inválidos"

def test_validacao_dos_dados(mqtt_client):
    for payload, _ in mqtt_client.received_messages:
        data = json.loads(payload)
        assert isinstance(data["tipo"], str), "Tipo inválido"
        assert isinstance(data["timestamp"], float), "Timestamp inválido"
        assert isinstance(data["temperatura"], (float)), "Temperatura inválida"
