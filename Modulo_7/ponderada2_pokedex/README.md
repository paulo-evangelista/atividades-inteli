# Pokedex

## 🐳 Docker hub
- Frontend: `https://hub.docker.com/repository/docker/pauleradixzz/pokedex-frontend/`
- Server: `https://hub.docker.com/repository/docker/pauleradixzz/pokedex-server/`
- Database: `postgres:latest`

Pokedex online com autenticação para a ponderada 2 do módulo 7 de Eng. de Computação

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
