# 📒 Prova 2

https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/5d8f7843-2901-47db-b4df-b0bb56b3b25c

**Features**:
  - Dockerfile e Compose devidamente configurados.
  - FastAPI.
  - Logging em um arquivo para níveis superiores a WARN.
  - Nginx como gateway.
  - Testes API com o Insomnia.

**Atenção!!**
  - Infelizmente o Insomnia instalado pelo Snap não consegue exportar collections 😢
  - Bindei a porta 80 do NGINX para a 3000 do computador, e o NGINX faz o proxy_pass da rota `/api/` para o container da api na porta `8000`. Portanto o URL para acessar a API é `http://127.0.0.1:3000/api/`
  - Fiz um Bind Mount para o arquivo de logs. Assim qualquer mudança feita nele dentro no container reflete no host em `api/logs.log`.

## ❓ Como executar
- Clone o repositório e certifique-se que o docker está corretamente instalado.
- Rode com `docker compose  up` na raiz do repositório.
- A API fica disponivel em `http://127.0.0.1:3000/api/`

## ❓ Enunciado
``` 
Atividade Prática
Para a avaliação prática, vocês podem consultar a documentação das ferramentas utilizadas, o repositório de vocês e o material de instrução. A única ferramenta de IA generativa que pode ser utilizada é o GitHub Copilot, se ele estiver habilitado no VS Code de vocês.

Considere o seguinte código para a construção da atividade:

https://gist.github.com/Murilo-ZC/21ef031290faa2ccb03dac07423faac1 
O que deve ser desenvolvido:

1. Realizar a adequação do projeto desenvolvido em Flask para FastAPI (até 1.0 ponto).

2. Adicionar o log em todas as rotas do sistema. O log deve ficar armazenado em um arquivo. Logar apenas informações de nível WARNING em diante (até 3.0 pontos).

3. Implementar o sistema em um container docker (até 1.0 ponto).

4. Adicionar um container com um Gateway utilizando NGINX para o sistema (até 2.0 pontos).

5. Criar um arquivo docker-compose que permita executar toda a aplicação (até 2.0 pontos).

6. Implementar os testes da API com Insomnia (até 1.0 ponto).

A entrega da avaliação deve acontecer pelo repositório do GitHub, enviando o link dele no forms de avaliação. ATENÇÃO: repositórios que não forem PÚBLICOS não serão corrigidos!!

Não esqueçam de escrever no README o procedimento para criar um ambiente virtual e instalar suas dependências, além das instruções para executar a aplicação de vocês.

PARA NÃO ESQUECER: criar corretamente o arquivo gitignore para não enviar os dados do ambiente virtual.

PARA NÃO ESQUECER 2: o seu repositório deve ser público!! Repositórios privados não serão avaliados.

Boa avaliação!

