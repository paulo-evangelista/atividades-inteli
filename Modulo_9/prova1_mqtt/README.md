# Prova 1 - mqtt

enunciado: [aqui!](https://rmnicola.github.io/m9-ec-encontros/the-gods-are-always-watching/)

https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/07aa6db6-aec3-4029-9f53-7ecc57f48f51

**Os testes englobam recebimento de mensagens, estrutura das mensagens e validação de tipos e valores para cada campo**

## Como executar
- É necessário um broker mqtt rodando na porta 1883, sem autenticação. No ubuntu, você pode instalar o Eclipse Mosquitto com `sudo apt install mosquitto`
- Clone o repositório e instale as bibliotecas necessãrias com `pip install pytest paho_mqtt`
- Rode o publisher com `python publisher.py`
- Para executar os testes, rode `pytest test.py`
- E para ver as leituras no seu terminal, rode `python subscriber.py`

# 🙉
