from sanic import Sanic
from sanic.response import text, file, json, html
from sanic.request import Request
import os
import random
from sanic_cors import CORS

app = Sanic(__name__)
CORS(app)

#cria a pasta para salvar as imagens, caso ela não exista
if not os.path.exists('./images'):
    os.mkdir('./images')

#Rota para envio do html de visualização das imagens
@app.route('/')
async def index(request: Request):
    with open('index.html', 'r') as file:
        html_content = file.read()

    return html(html_content)

#rota que recebe a imagem e salva na pasta images
@app.route('/upload', methods=['POST'])
async def upload_image(request: Request):
    image_bytes = request.body

    #número aleatório para definir como nome da imagem
    randomNumber = random.randint(0, 100000)

    #escreve a imagem na pasta images
    with open(f'./images/{randomNumber}.jpg', 'wb') as file:
        file.write(image_bytes)

    #retorna o id/nome da imagem salva
    return json({'id': randomNumber, "status": "success"}, status=200)

#rota que recebe um id/nome e retorna a imagem correspondente
@app.route('/images/<id:int>', methods=['GET'])
async def get_image(_, id: int):

    try:
        return await file(f'./images/{id}.jpg', status=200)
    except:
        return text('Imagem não encontrada', status=400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
