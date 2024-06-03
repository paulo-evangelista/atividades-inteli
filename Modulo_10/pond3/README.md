# 📲 Flutter w/ Login&Camera (Entrega parcial - WIP!)

https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/47afe822-fb0f-42b6-a6c3-dd2f07ecff36

## 🧩 Features

- Microserviços:
    - Flask para autenticação
    - Outro Flask para processamento de imagens
- Login & Signin (Com logging)
- Envio e recebimento da imagem c/ backend
- Backend que inverte as cores da foto
- Notificação quando o resultado é recebido
- Containerizado

## ❓ Como executar
- Clone o repositório e instale as bibliotecas necessárias com `pip3 install flask pillow`
- Rode ambos os serviços com `docker compose up`
- Para o Flutter na pasta `app`, reinicie o projeto com `flutter create .` e rode na sua plataforma preferida com ` flutter run`
    - Lembre-se de rodar ambos servidor e app em uma mesma rede local!📲
