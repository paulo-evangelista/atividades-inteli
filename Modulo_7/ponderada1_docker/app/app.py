from sanic import Sanic
from sanic.response import html
from sanic.request import Request

app = Sanic(__name__)

@app.route('/')
async def index(request: Request):
    with open('index.html', 'r') as file:
        html_content = file.read()
    return html(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
