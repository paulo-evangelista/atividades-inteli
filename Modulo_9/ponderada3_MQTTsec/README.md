# Segurança para MQTT

Está atividade compreende a utilização do broker HiveMQ com segurança, como usar usuário e senha para autenticação e usar TLS.

**A ponderada feita anteriormente já compreende esses requisitos, portanto vou deixar apenas o link dela aqui. Todas as instruções e demonstração lá permanecem vãlidas.**

[Ponderada 2: Testes automatizados para MQTT](https://github.com/paulo-evangelista/atividades-inteli/tree/main/Modulo_9/ponderada2_MQTTpytest)

- A utilização de TLS é evidenciada tanto pela porta do broker usada (porta `8883`, padrão para conexão MQTTS) quanto na configuração do cliente MQTT, com a opção `client.tls_set()`

- A autenticação é evidenciada na configuração do cliente MQTT, com a linha `client.username_pw_set(mqtt_username, mqtt_password)
`
