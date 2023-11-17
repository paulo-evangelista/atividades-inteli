import re

intencoes = {
    r"(atualizar.*(pagamento|cartão))|(pagamento.*desatualizado)|(mudar.*pagamento)": "Intenção A",
    r"(status.*pedido)|(acompanhar.*pedido)|(rastrear.*pedido)|(onde.*pedido)|(status.*entrega)": "Intenção B"
}


acoes = {
    "Intenção A": "Para atualizar suas informações de pagamento, acesse a seção 'Configurações de Pagamento' em sua conta e siga as instruções.",
    "Intenção B": "Para acompanhar o status do seu pedido, acesse a seção 'Meus Pedidos', escolha o pedido desejado e verifique o status atual."
}

def identificar_resposta(comando):
    if comando == "sair": exit()
    for padrao, intencao in intencoes.items():
        if re.search(padrao, comando, re.IGNORECASE):
            return acoes[intencao]
    return "Desculpe, não consegui entender sua solicitação."


while True:
    comando = input("\ndigite seu comando:\n -> ")
    print("\n   ",identificar_resposta(comando))