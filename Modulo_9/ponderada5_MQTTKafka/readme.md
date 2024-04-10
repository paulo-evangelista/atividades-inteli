# 🪳Kafka, 🍯HiveMQ e 🐍Pytest 

### Enunciado: [Aqui!](https://rmnicola.github.io/m9-ec-encontros/ponderada7)

https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/1d59852e-04c0-4c96-802b-dd73b91571c9

Sistema com Cluster MQTT no HiveMQ Cloud integrado com Confluent Cloud

- `test.py`: Programa Pytest que testa se as mensagens estão disponíveis, se a estrutura está correta e se elas estão corretamente sequenciadas.
- `publisher.py`: Envia mensagens simuladas para o HiveMQ.

## Como executar

> [!IMPORTANT]
> **Para executar esse projeto, você precisará:**
> - Um cluster no HiveMQ Cloud, com uma Integration com o Confluent Cloud.
> - Um Kafka devidamente configurado na Confluent Cloud.
> - Um arquivo `client.properties` com os dados da API do seu Kafka
> - Alterar ambos os arquivos com seus dados, como login do HiveMQ e o nome do tópico.

- Com o que foi mencionado acima funcionando, basta instalar as bibliotecas com `pip install paho-mqtt confluent_kafka pytest`
- Para rodar os testes no Kafka, basta rodar `pytest test.py`
- Para enviar mensagens MQTT e alimentar o Kafka, basta executar `python publisher.py`
