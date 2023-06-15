# Image saver

Esta atividade é composta por um servidor que armazena imagens recebidas no sistema de arquivos local.
Visto que nosso projeto (LINK DO PROJETO) é uma aplicação Electrum, faz sentido que os arquivos fiquem salvos no sistema local, no formato JPG, para fácil acesso e backup.

## server.py
- servidor python Sanic responsável por receber as imagens e armazena-las no sistema de arquivos.
    - As imagens são salvas com um nome aleatório, retornado na resposta da requisição.
- Também retorna pode retornar a imagem pelo nome do arquivo.

## main.ipynb
- Script acessório que captura uma imagem da webcam e envia para o servidor

## index.html
- Página acessória apenas para visualização de fotos enviadas.
    - As imagens podem ser acessadas com base no nome do arquivo (que é recebido na resposta da requisição)
    