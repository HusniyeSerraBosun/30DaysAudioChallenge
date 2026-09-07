import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
output_dir = os.getenv("OUTPUT_FOLDER")

def sawtooth(output_file_path):
    samprate = 44100
    duration = 3
    f = 440
    T = 1/f #period
    t = np.linspace(0, duration, samprate*duration, endpoint=False)
    ramp = t % T
    normalized_ramp = ramp / T 
    final = 2 * normalized_ramp - 1
    final =(final * 32767).astype(np.int16)

    with wave.open(output_file_path, "wb") as out:
        out.setnchannels(1)
        out.setsampwidth(2)
        out.setframerate(samprate)
        out.setnframes(len(final))
        out.writeframes(final.tobytes())

    print(f"File saved successfully {output_file_path}")

target_file_path = os.path.join(output_dir, "sawtooth_440hz.wav")
sawtooth(target_file_path)
