# 🗂️ Dashboard + AI + Auth

### 🐳 Docker Hub
- **frontend:** `https://hub.docker.com/repository/docker/pauleradixzz/m7pond4-frontend/general`
- **server:** `https://hub.docker.com/repository/docker/pauleradixzz/m7pond4-server/general`

## O quê?

Esta atividade junta outras soluções desenvolvidas durante o módulo. É um sistema web para manipular a AI desenvolvida [nessa atividade](), com um dashboard online e autenticação em um servidor desenvolvido [nessa atividade]().

## A dashboard

A dashboard permite:
- Utilize a IA: Fazer novas previsões por meio da interface gráfica
- Estatísticas: Apresenta gráficos com dados de todas as previsões já realizadas e histórico de previsões

## ☁️ AWS
- Para a demonstração, o projeto foi deployado em nuvem comercial
- Foi utilizado apenas um AWS EC2 micro e um Postgres no AWS RDS.

## ❓ Como rodar o projeto

- O jeito mais fácil de rodar o projeto é por meio do Docker-compose:
    - Baixe apenas o arquivo `docker-compose.yaml` deste repositório.
    - Em um terminal no mesmo diretório, execute `docker compose up`

- Você também pode clonar este repositório e executar o mesmo comando