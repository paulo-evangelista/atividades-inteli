# Metabase

Enunciado: [Aqui!](https://rmnicola.github.io/m9-ec-encontros/ponderada5)

Juntamos os pubs e subs que fiz nas atividades anteriores com um banco de dados e o Metabase para visualizar os dados. Nesse caso, estamos simulando apenas um sensor de massa de partículas (PM1-10)

https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/34061af7-298e-48c8-86a2-40087c8cc021

##  No vídeo:

1. Iniciamos o docker compose, que sobe um Postgres e o Metabase
2. Iniciamos o broker MQTT.
3. Iniciamos o subscriber MQTT.
4. Iniciamos o publisher MQTT.

## Como rodar o sistema:

- Clone o repositório
- Começe com o docker compose, com `docker compose up` dentro do reposítório.
- Agora rode o Subscriber com `python3 subscriber.py`.
- Com ambos ainda rodando, em outro terminal, execute os publisher com `python3 publisher.py`.
- Agora acesse `localhost:3000` para usar o Metabase.
