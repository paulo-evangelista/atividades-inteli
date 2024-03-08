
import paho.mqtt.subscribe as subscribe
import json
import math
def print_messages(client, userdata, message):
    content = json.loads(message.payload)
    tipo = content["tipo"].split(" ")[0]
    temperatura = content["temperatura"]

    print("\n\n%s : %s°C " % (content["tipo"], round(temperatura, 2)), end="")

    if tipo == "geladeira":
        if temperatura > 10:
            print("[ATENÇÃO: Temperatura alta]", end="")
        elif temperatura < 2:
            print("[ATENÇÃO: Temperatura baixa]", end="")

    elif tipo == "freezer":
        if temperatura > -15:
            print("[ATENÇÃO: Temperatura alta]", end="")
        elif temperatura < -25:
            print("[ATENÇÃO: Temperatura baixa]", end="")

subscribe.callback(print_messages, "#", hostname="localhost")