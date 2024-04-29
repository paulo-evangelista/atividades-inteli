# 📒 API To-do list v2

~(Entrega parcial 1)~

~(Entrega parcial 2)~

**Ponderada 2**

> [!IMPORTANT]
> Mudanças entre a primeira parcial (pond1) e essa (pond2):
> - Dockerização
>   - Para executar o projeto, basta rodar `docker compose up` no diretório `Modulo_10/pond2`
> - Servidor Gunicorn.
> - Vídeo de demonstração da API.
> Tirando isso, as funcionalidades são as mesmas da pond1 ⬇️

---

https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/3be9f2d3-4f9f-455c-a76c-d879718b3168



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
