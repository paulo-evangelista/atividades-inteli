# 🗂️ Prova 1 - Módulo 7
### Dockerfile e docker-compose

- `backend/Dockerfile`**:** parte da imagem base de Python no debian slim; Define a pasta `app` do container como raiz e copia tudo lá pra dentro; Pip instala todos os item de `requirements.txt`; Python executa o arquivo principal.
  
- `frontend/Dockerfile`**:** Parte da imagem base de Node no debian slim; Define a pasta `app` do container como raiz e copia tudo lá pra dentro; NPM instala todos os item de `package.json`; Node executa o arquivo principal.
  
- `./docker-compose.yaml`**:**  Define os serviços ***frontend e server***, indicando o Dockerfile para montar cada um e o parelhamento de portas. 


## 🐳 Docker Hub
- **frontend:** [m7prova1-frontend](https://hub.docker.com/repository/docker/pauleradixzz/m7prova1-frontend/general)
- **backend:** [m7prova1-backend](https://hub.docker.com/repository/docker/pauleradixzz/m7prova1-backend/general)

## 🖥️ Como executar
- Clone o repositório
- execute `docker compose up`
