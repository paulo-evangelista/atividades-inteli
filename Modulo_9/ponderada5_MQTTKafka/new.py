from confluent_kafka import Producer, Consumer
import json
import pytest

class Kafka_consumer:
    def __init__(self):
        self.config = {}
        with open("client.properties") as fh:
            for line in fh:
                line = line.strip()
                if len(line) != 0 and line[0] != "#":
                    parameter, value = line.strip().split('=', 1)
                    self.config[parameter] = value.strip()
        
        self.config["group.id"] = "python-group-1"
        self.config["auto.offset.reset"] = "earliest"

        self.consumer = Consumer(self.config)
        self.consumer.subscribe(["data"])


        self.messages = []
        while True:
            msg = self.consumer.poll(1.0)
            if msg is not None and msg.error() is None:
                key = msg.key().decode("utf-8")
                value = msg.value().decode("utf-8")
                print(json.loads(value))
                self.messages.append(json.loads(value))
            else:
                print("Mensagens consumidas:", len(self.messages))
                break


@pytest.fixture(scope="session")
def kafka_messages():
    kafka_consumer = Kafka_consumer()

    yield kafka_consumer.messages

    kafka_consumer.consumer.close()

def test_connection(kafka_messages):
    assert len(kafka_messages) > 0, "Nenhuma mensagem recebida"

def test_data_validation(kafka_messages):
    for message in kafka_messages:
        assert all(key in message for key in ["message_id", "mc_pm1_0", "mc_pm2_5", "mc_pm4_0", "mc_pm10"]), "Dados em formato inválido"

def test_id_sequence(kafka_messages):
    for i in range(len(kafka_messages)-1):
        assert kafka_messages[i]["message_id"] == kafka_messages[i+1]["message_id"]-1, "IDs fora de ordem, repetidos ou faltando"