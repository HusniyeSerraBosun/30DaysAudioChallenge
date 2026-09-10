import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
output_dir = os.getenv("OUTPUT_FOLDER")

def am_modulation(output_file_path):
    samprate=44100
    duration = 3
    N = samprate*duration
    A = 1
    f_one = 440
    f_two = 4
    phi = 0
    t = np.linspace(0, duration, N, endpoint=False)

    carrier = A * np.sin(2*np.pi * f_one * t + phi)
    modulator = (A * np.sin(2*np.pi * f_two * t + phi) + 1) /2

    signal = (carrier * modulator * 32767).astype(np.int16)

    with wave.open(output_file_path, "wb") as out:
        out.setframerate(samprate)
        out.setnchannels(1)
        out.setsampwidth(2)
        out.setnframes(len(signal))
        out.writeframes(signal.tobytes())

    print(f"File saved successfully {output_file_path}")

target_path_file = os.path.join(output_dir, "am_modulation.wav")
am_modulation(target_path_file)



