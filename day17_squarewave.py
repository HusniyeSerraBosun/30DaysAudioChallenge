import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
output_dir = os.getenv("OUTPUT_FOLDER")

def square_wave(output_file_path):
    samprate = 44100
    duration = 3
    a = 1
    phi = 0
    f = 440
    t = np.linspace(0,duration, samprate*duration, endpoint=False)

    sin_wave = a * np.sin( 2*np.pi *f* t + phi)

    #np.where(condition, value(if true), value(if false))
    square_wave = np.where(sin_wave>=0, 1.0, -1.0)
    square_wave = (square_wave * 32767).astype(np.int16)
    final_wave = square_wave.tobytes()

    with wave.open(output_file_path, "wb") as out:
        out.setnchannels(1)
        out.setsampwidth(2)
        out.setframerate(samprate)
        out.setnframes(len(square_wave))
        out.writeframes(final_wave)

    print(f"file saved successfully {output_file_path}")

target_file_path = os.path.join(output_dir, "square_440hz.wav")
square_wave(target_file_path)