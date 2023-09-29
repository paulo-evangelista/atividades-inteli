# 🗂️ Prova 2 - 🎨 FullStack em cloud
https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/9ddf5b22-bd77-4f8a-a6e9-87faecb5936c



> Repo com o template e instruções: [Murilo-ZC/Avalicacao-M7-2023-EC](https://github.com/Murilo-ZC/Avaliacao-P2-M7-2023-EC/tree/main)
## 🤌 Quais passos apliquei?
- Antes de mais nada fui na AWS e criei dois EC2 e um RDS
- Garanti que todos estavam com comunicação liberada par2a qualquer IP
- Testei a conexão com o DB e fiz um ping para as EC2. Tudo func2ionou
- Alterei javascript do front para colocar os endereços do meu servidor
- Alterei o FastAPI para colocar a conexão do meu DB
- Tentei Rodar o script python fornecido para criar as tabelas do DB
- Não funcionou, então conectei o banco no DBeaver e rodei o SQL direto por lá
- Joguei tudo do repositório original para esse aqui e clonei ele dentro das duas máquinas
- na primeira máquina, instalei PIP e as dependencias necessárias para rodar o servidor
- Coloquei o servidor pra rodar
- Instalei Apache na segunda máquina e coloquei ele também pra rodar
- Corrigi os bugs do Murilo
- e gravei o vídeo

## 🐛 O quê eu mudei no código original?
- dados de conexão com banco de dados e servidor
- O `criar_tabelas.py` não funcionou, então criei na mão
- o comando `sudo cp ./Avaliacao-P2-M7-2023-EC/frontend /var/www/html` não funcionou, copiei na mão
- o front estava tentando importar `style.css`, mas o nome era `styles.css`. Corrigi o import
- A cor de background era a mesma da fonte nos lembretes, parecia que o texto estava faltando. Mudei o CSS

😀
