from TTS.api import TTS
from playsound import playsound

tts = TTS(model_name="tts_models/pt/cv/vits", progress_bar=False)
print("\nBem vindo! Digite o texto:\n")

while True:
    text = input("\033[92m  ➔ \033[96m")
    tts.tts_to_file(text, file_path="output.wav")
    playsound("output.wav")