# 🈯 Tradutor

Script em python que transcreve um áudio, traduz o texto para a língua escolhida e transforma em áudio de novo. 

https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/fd057619-1a87-4b57-8d73-82b1a202b2a4

## ❓ Como funciona?

- Usamos o OpenAI Whisper localmente para transcrever o áudio.
    - Optei pelo modelo `base`, que precisa de ~1GB de VRAM
- Depois usamos as APIs gratuitas do google de tradução e TTS para traduzir e transformar em fala. 

## ❓ Como rodar o projeto

- Clone este repositório.
- Dentro dele, rode `pip install -r requirements.txt` para instalar as bibliotecas necessárias.
- Rode `python3 main.py`.
- Escolha a língua de destino e o caminho para o audio que quer traduzir.
