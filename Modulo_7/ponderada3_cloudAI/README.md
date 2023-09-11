# 🗂️ fastAPI & AWS & AI

https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/675fa69b-8d66-4413-ba4b-0817bf2340d0

## 🐳 Docker Hub
`https://hub.docker.com/repository/docker/pauleradixzz/fastapi-ai/general`

# IA:

## Função:

O dataset escolhido foi [esse](https://www.kaggle.com/datasets/joebeachcapital/customer-segmentation), que apresenta dados sobre clientes de shopping. Os dados disponíveis são ** idade, gênero, renda e qualidade.**
Nossa meta é, com as três primeiras colunas, prever a qualidade do cliente: Uma porcentagem que estima o valor de um cliente para o shopping. *Clientes de maior qualidade tendem a gastar mais dinheiro quando visitam um shopping. *

## O modelo:

> Veja `notebook.ipynb`

Após testes usando Pycaret, o modelo escolhido foi um KNN de regressão. Esse modelo faz sentido pois:
- A quantidade reduzida de colunas favorece


## 🧰 Funcionalidades:
- Criar e logar em sua conta
- Adicionar Pokemons à sua pokedex (por espécie ou n° dex)
- Editar o apelido do Pokemon
- Remover Pokemons

## ❓ Como rodar o projeto

- Clone o repositório
- Dentro dele, execute `docker compose up`
    > Para executar em modo otimizado para produção, rode `docker compose -f ./docker-compose.prod.yml up`
- Pronto! Agora é só acessar `http://localhost:3000` e criar sua conta!
 
## 🔐 Segurança

A segurança opera com base em tokens JWT salvos no cliente. O token é gerado e inserido no cliente quando o usuário faz login.
- O token é enviado pelo cliente e conferido no servidor em todas as requisições.
- O token é conferido quando o usuário tenta acessar a home do website (caso seja inválido, o usuário é enviado à página de login)
- O token tem validade de 30 minutos.
