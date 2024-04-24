# 📒 API To-do list

(Entrega parcial 1)

![m10pond1](https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/dddc9270-a116-4a2c-8d83-34620ed82311)

## 🧩 Features

- Threading desligado, totalmente síncrono.
- As tarefas ficam em memória.
- Autenticação (Basic Auth).
- Documentação OpenAPI (em /static/collection.json).
- Página Swagger.
- Criar, listar, alterar e excluir tarefas.

## ❓ Como executar
- Clone o repositório e instale as bibliotecas necessárias com `pip3 install flask flask-swagger-ui Flask-HTTPAuth flask-CORS`
- Rode o servidor com `python3 app.py`
  - Para autenticação, use o usuário `paulo` e a senha `senha` 
  - Acesse a documentação Swagger em `localhost:5000/docs`
