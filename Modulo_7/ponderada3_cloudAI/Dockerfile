# Usando uma imagem base com Python 3.8
FROM python:3.8-slim

# Definindo a pasta de trabalho
WORKDIR /app

# Copiando o conteúdo local para a pasta de trabalho
COPY . .

# Instalando as dependências necessárias
RUN pip install fastapi[all] uvicorn pycaret h11

# Comando para iniciar a aplicação FastAPI quando o contêiner for iniciado
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
 