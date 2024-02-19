# Publisher MQTT com sensor SPS30

https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/c758ad82-1d98-4719-82cc-b9e2568e9ba7

Seguindo o datasheet do Sensiron SPS30:

![image](https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/daf6e093-cf6f-42aa-aa70-0fe681e70cb8)

Criei um script que simula os dados de concentração de massa de particulas PM1, PM2.5, PM5 e PM10 esses publica esses dados no formato original (big-endian de 16bits em hex) com QoS 1.

![image](https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/d112c614-a7be-444e-8c03-d7a6928e8cdf)

## Como rodar o script:

- Clone o repositório
- Instale a biblioteca Paho-MQTT com `pip3 install paho-mqtt==2.0.0`
- dentro do repositório, execute o script com `python3 main.py`
