import pvporcupine
import struct
import pyaudio

porcupine = None
pa = None
audio_stream = None

try:
    porcupine = pvporcupine.create(keyword_paths=['path/to/keyword.ppn'])

    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
                    rate=porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=porcupine.frame_length)

    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        result = porcupine.process(pcm)

        if result:
            print('Wake word detected!')

finally:
    if porcupine is not None:
        porcupine.delete()

    if audio_stream is not None:
        audio_stream.close()

    if pa is not None:
        pa.terminate()
