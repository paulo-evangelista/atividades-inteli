# Containers Docker
### Servidor Sanic e curriculo
[Docker hub](https://hub.docker.com/repository/docker/pauleradixzz/pauloevangelista-sanic/general)

Um simples servidor Sanic containerizado que serve uma única página HTML com uma linda versão do meu breve currículo

## Como executar
- Clone a imagem do DockerHub -> `docker pull pauleradixzz/pauloevangelista-sanic`
- Crie e execute um container a partir da imagem (atrelando a porta 8000 do sistema local com a porta 8000 do container) -> `docker run -p 8000:8000 pauleradixzz/pauloevangelista-sanic`
- Acesse `http://0.0.0.0:8000` para ver meu currículo :)