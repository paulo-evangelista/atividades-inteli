# Image saver

https://github.com/paulo-evangelista/atividades-m6/assets/99093520/4a8439ce-e750-44c6-a249-4ce6c17fb824

Esta atividade é composta por um servidor que armazena imagens recebidas no sistema de arquivos local.
Visto que nosso projeto ([2023m6t2/gerbros](https://github.com/2023M6T2-Inteli/Grupo05)) é uma aplicação Electrum, faz sentido que os arquivos fiquem salvos no sistema local, no formato JPG, para fácil acesso e backup.

### server.py
- servidor python Sanic responsável por receber as imagens e armazena-las no sistema de arquivos.
    - As imagens são salvas com um nome aleatório, retornado na resposta da requisição.
- Também retorna pode retornar a imagem pelo nome do arquivo.

### main.ipynb
- Script acessório que captura uma imagem da webcam e envia para o servidor

### index.html
- Página acessória apenas para visualização de fotos enviadas.
    - As imagens podem ser acessadas com base no nome do arquivo (que é recebido na resposta da requisição)
    



