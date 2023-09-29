from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

def text_to_speech(text, lang='en', slow=False):
    speech = gTTS(text=text, lang=lang, slow=slow)
    speech.save("output.mp3")

    # Load and play the output file
    sound = AudioSegment.from_file("output.mp3")
    play(sound)

# Test the function
text_to_speech('Hello, I am your text to speech application.', slow=False)
