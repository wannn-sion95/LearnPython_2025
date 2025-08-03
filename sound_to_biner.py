import wave


def sound_to_biner(path):
    with wave.open(path, 'rb') as wav:
        frames = wav.readframes(10)
        for byte in frames:
            print(format(byte, '08b'), end=' ')


sound_to_biner('example_sound.wav')
