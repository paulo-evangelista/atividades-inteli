# Chatbot RegEx

Chatbot para a prova 1 do módulo 8

## Comandos:

Para acessar o fluxo de atualizar suas informações de pagamento, a frase inserida pelo usuário deve ter as palavras chave:
- `atualizar` seguido por `pagamento` ou `cartão`
- `pagamento` seguido por `desatualizado`
- `mudar` seguido por `pagamento` ou `cartão`

Para acessar o fluxo de acompanhar seu pedido, a frase inserida pelo usuário deve ter as palavras chave:
- `status` seguido por `pedido`
- `rastrear` seguido por `pedido`
- `onde` seguido por `pedido`
- `status` seguido por `entrega`



> As palavras não precisam estar juntas na frase. A frase `onde está o meu pedido` é válida, por exemplo.


Para sair do programa, o usuário pode digitar `sair`.


## Como executar:
- Apenas baixe o script python e execute com `python3 chat.py`