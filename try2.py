from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

def text_to_speech(text, lang='en', slow=False):
    speech = gTTS(text=text, lang=lang, slow=slow)
    speech.save("output.mp3")

    # Load the audio file
    sound = AudioSegment.from_file("output.mp3")

    # Speed up the speech
    fast_sound = speed_change(sound, 1.5)
    
    # Play the output file
    play(fast_sound)

def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This gives the effect of speeding up the playback without changing the pitch.
    sound_with_altered_frame_rate = sound.speedup(playback_speed=speed)

    return sound_with_altered_frame_rate

# Test the function
text_to_speech('Hello, I am your text to speech application.', slow=False)
