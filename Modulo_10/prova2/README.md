# 📒 Prova 1

Features:
  - Dockerfile devidamente configurado para produção
  - API Rest de nível 2, com recurso definido e verbos HTTP devidos.
  - O arquivo `api-collection.json` pode ser importado em qualquer cliente API para testes

Rotas:
  - `/novo:` **(POST)** Cria um novo pedido a partir das informações do body.
  - `/pedidos`
    - `/` **(GET)** Retorna todos os pedidos.
    - `/:id` **(PUT)** Atualiza o pedido com as informações do body.
    - `/:id` **(DELETE)** Deleta o pedido.
    - `/:id` **(GET)** Retorna o pedido.

Explicação:

- Tudo está no arquivo `app.py`. Os pedidos são salvos no objeto global `pedidos` e as rotas apenas manipulam esse objeto.

Collection:

![Screenshot from 2024-05-17 09-56-51](https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/3c8cfcce-75f5-4adc-9124-765f62c4b0aa)

## ❓ Como executar
- Clone o repositório e certifique-se que o docker está corretamente instalado.
- Builde a imagem Docker com `docker build -t m10prova1 .`
- Rode a imagem, expondo a porta 5000, com `docker run -p 5000:5000 m10prova1`

## ❓ Enunciado
``` 
Para a questão prática da avaliação, você deve entregar uma API de nível de maturidade 2 no Modelo de Maturidade de Richardson, escrita em Python.
Você deve criar um dois recursos permitam ao usuário realizar um cadastro de um pedido. Esse pedido deve possuir o nome do usuário, o e-mail do usuário e a descrição do pedido. Ele deve ser enviado como um JSON. 

O seu sistema deve fornecer, no mínimo, as seguintes rotas:

●      /novo: cadastrar um novo pedido. Recebe um JSON e retorna um ID.

●      /pedidos: retorna todos os pedidos cadastrados

●      /pedidos/<id>: retorna o pedido do ID fornecido. Se esse pedido não existir, retornar que não foi possível locallizar ele, da forma mais apropriada para atender as questões do problema proposto.

O recurso / pedidos/<id> ainda deve possibilitar editar o pedido e excluir ele, implementados em recursos distintos.

Nenhuma interface gráfica deve ser implementada, apenas as rotas. Elas devem ser testadas utilizando collections do Insomnia. Essas coleções devem ser exportadas no repositório.

A solução deve ser dockerizada.

Não existe a necessidade de armazenar as requisições em disco, pode ser utilizado apenas memória.

