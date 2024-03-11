# Testes automatizados para MQTT

Usando o mesmo publisher da ponderada 1, criei um subscriber que realiza testes unitários.



https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/097f533c-f62e-4318-9d12-c54485e90d92



## Testes realizados:

- **Teste 1 - Recebimento:** Confirma que as mensagens estão sendo enviadas e são acessíveis por subscribers.
- **Teste 2 - Estrutura:** Valida a estrutura do corpo da mensagem enviada.
- **Teste 3 - Latência:** Confirma que as mensagens estão chegando no intervalo esperado de tempo, 2 segundos, com uma margem de erro de 0,5 segundos.

## Como rodar o script:

- Clone o repositório
- Instale a biblioteca Paho-MQTT e Pytest com `pip3 install paho-mqtt==2.0.0 pytest==8.0.1`
- dentro do repositório, execute primeiro o script do publisher com `python3 publisher.py`
- Com o publisher ainda rodando, em outro terminal, execute os testes com `pytest subscriber.py`
