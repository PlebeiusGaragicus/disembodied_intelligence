from gtts import gTTS
import os

def text_to_speech(text, lang='en', filename='output.mp3', pitch=0):
    speech = gTTS(text=text, lang=lang, slow=False)
    speech.save(filename)

    # Playing the converted file with altered speed
    os.system(f"mpg123 --pitch {pitch} {filename}")

text_to_speech('Hello, I am your text to speech application.Hello, I am your text to speech application.Hello, I am your text to speech application.Hello, I am your text to speech application.Hello, I am your text to speech application.Hello, I am your text to speech application.', filename='output1.mp3', pitch=10)
