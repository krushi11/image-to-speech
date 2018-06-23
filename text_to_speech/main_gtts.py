from gtts import gTTS
import os

#Class TextToSpeech:

def read(file_path):
    with open(file_path, 'r') as myfile:
        data=myfile.read().replace('\n', '')

    tts = gTTS(text=data, lang='en')
    tts.save("speech.mp3")
    os.system("mpg123 speech.mp3")
