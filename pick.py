# from pocketsphinx import LiveSpeech

# speech = LiveSpeech(lm=False, keyphrase='wake word', kws_threshold=1e-20)

# for phrase in speech:
#     print(phrase.segments(detailed=True)) # You should see 'wake word' printed when you say it


from pocketsphinx import LiveSpeech

speech = LiveSpeech(lm=False, keyphrase='wake word', kws_threshold=1e-20)

for phrase in speech:
    segments = phrase.segments(detailed=True)
    if segments is not None:
        print(segments) # You should see 'wake word' printed when you say it
