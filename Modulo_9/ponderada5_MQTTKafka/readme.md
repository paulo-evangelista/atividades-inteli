# 🪳 Kafka e MongoDB 🙉 

### Enunciado: [Aqui!](https://rmnicola.github.io/m9-ec-encontros/would-you-kindly/)

https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/eaac07c9-853e-485b-bda9-2b1b49f72839

- O primeiro programa, `pub.py`, é responsável por criar dados simulados de um sensor e enviá-los para o Kafka.
- O segundo programa, `consumer.py`, consome os dados do Kafka e insere-os no MongoDB, para persistência dos dados. Após isso, rodamos dois testes:
  - O primeiro testa se todos os dados que foram consumidos estão inseridos no banco.
  - O segundo confere se todos os objetos salvos tem a estrutura desejada, com as chaves `["idSensor", "timestamp", "tipoPoluente", "nivel"]`.

## Como executar
- Primeiro rode os containers docker, com `docker compose up`
- Certifique-se que tem as bibliotecas necessárias instaladas com `pip install kafka-python pymongo pytest`
- Agora execute o producer, com `python pub.py`
- E para consumir as mensagens, rode `pytest consumer.py` 
