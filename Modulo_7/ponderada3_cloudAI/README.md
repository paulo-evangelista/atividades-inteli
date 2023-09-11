# 🗂️ fastAPI & AWS & AI

https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/55ef4805-6272-449b-87ce-191971b93844

### 🐳 Docker Hub
`https://hub.docker.com/repository/docker/pauleradixzz/fastapi-ai/general`

## 🤖 IA

### Função:

O dataset escolhido foi [esse](https://www.kaggle.com/datasets/joebeachcapital/customer-segmentation), que apresenta dados sobre clientes de shopping. Os dados disponíveis são *idade, gênero, renda e qualidade.*
Nossa meta é, com as três primeiras colunas, prever a qualidade do cliente: Uma porcentagem que estima o valor de um cliente para o shopping. **Clientes de maior qualidade tendem a gastar mais dinheiro quando visitam um shopping.**

### O modelo:

> Veja `notebook.ipynb`

Após testes usando Pycaret, o modelo escolhido foi um **KNN de regressão**. Faz sentido, já que temos poucas colunas e relações bem estabelecidas entre elas.

## 🖥 Servidor
- FastAPI com apenas uma rota, responsável por executar o modelo com os dados recebidos.
- Type Safety com Pydantic.

## ☁️ AWS
- O projeto foi deployado em nuvem comercial, como demonstrado no vídeo.
- Foi utilizado apenas um AWS EC2.

## ❓ Como rodar o projeto

- Clone a imagem do DockerHub -> `docker pull pauleradixzz/fastapi-ai`
- Crie e execute um container a partir da imagem (atrelando a porta 8000 do sistema local com a porta 8000 do container) -> docker run -p 8000:8000 `pauleradixzz/fastapi-ai`
- Faça um POST para `localhost:8000/predict` com o seguinte JSON no body da requisição:
    - **Age:** Idade da pessoa em questão (INT)
    - **Gender:** Gênero da pessoa: 0 para homem, 1 para mulher (INT)
    - **Income:** Sálario mensal da pessoa, em milhares de reais (FLOAT com duas casas decimais)
 

