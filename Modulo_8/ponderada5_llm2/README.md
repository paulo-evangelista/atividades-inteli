# 🗂️ Chatbot Ollama v2

---

> [!NOTE]
> Se você está procurando a atividade de tradução com TTS e STT, ela está [aqui](https://github.com/paulo-evangelista/atividades-inteli/edit/main/Modulo_8/ponderada8_translate)

---

Mesmo modelo e código [dessa atividade](https://github.com/paulo-evangelista/atividades-inteli/tree/main/Modulo_8/ponderada4_llm), mas agora com uma [mensagem de sistema](https://github.com/paulo-evangelista/atividades-inteli/blob/main/Modulo_8/ponderada5_llm2/context.py) que contextualiza as respostas do modelo com informações sobre segurança de alunos em aulas práticas no laboratório.

> Como cada prompt demora 100 segundos, resumi o vídeo em um screenshot :)
![image](https://github.com/paulo-evangelista/atividades-inteli/assets/99093520/c81b97b1-9be3-4cd8-a944-2ba3cd0328b6)

## ❓ Como rodar o projeto

- Instale o Ollama no seu computador [aqui.](https://ollama.ai/)
- Clone este repositório.
- Dentro dele, rode `pip install -r requirements.txt` para instalar as bibliotecas necessárias.
- Rode `ollama create assistant -f Modelfile` para baixar e configurar o modelo.
- Por fim, rode `python3 main.py` e acesse [http://127.0.0.1:7860/](http://127.0.0.1:7860/) para conversar!
