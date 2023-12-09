import whisper
from googletrans import Translator
from gtts import gTTS
import os
import inquirer

LANGUAGES_MAPPING = [
   ("Francês", "fr" ),
    ("Espanhol", "es" ),
    ("Inglês", "en" ),
    ("Italiano", "it" ),
    ("Japonês", "ja" ),
]

def speech_to_text(audio_path):
    model = whisper.load_model("medium")
    result = model.transcribe(audio_path)
    return result["text"]

def translate(text, target_language):
    trans = Translator()
    translated = trans.translate(text, dest=target_language)
    return translated.text

def text_to_speech(text, target_language):
    tts = gTTS(text=text, lang=target_language)
    audio_file = 'translated_audio.mp3'
    tts.save(audio_file)
    return audio_file

def choose_language_cli():
    questions = [
        inquirer.List('language',
                      message="Escolha a língua destino para tradução:",
                      choices=LANGUAGES_MAPPING,
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['language']

def play_audio(audio_path):
    os.system(f"xdg-open {audio_path}") 

def main():
    target_language = choose_language_cli()
    audio_path = input("Digite o caminho do arquivo de áudio -> \033[96m")

    print("\n \033[92m -> \033[0m Transcrevendo áudio...")
    text = speech_to_text(audio_path)
    print("\n \033[92m -> \033[0m Traduzindo texto...")
    translated_text = translate(text, target_language)
    print("\n \033[92m -> \033[0m Gerando áudio traduzido...")
    audio_path = text_to_speech(translated_text, target_language)
    print("\n \033[92m -> Done! \033[0m \n")
    
    play = inquirer.confirm("Deseja ouvir o áudio traduzido?", default=True)
    if play:
        play_audio(audio_path)

if __name__ == "__main__":
    main()
