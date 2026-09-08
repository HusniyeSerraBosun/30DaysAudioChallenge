import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
output_dir = os.getenv("OUTPUT_FOLDER")

def soft_clipping(output_file_path):
    samprate = 44100
    duration = 3
    A = 1
    f = 440
    phi = 0
    drive = 5.0
    t = np.linspace(0, duration, samprate*duration, endpoint=False)
    signal = A * np.sin(2*np.pi * f * t +phi)
    signal = ((np.tanh(signal*drive))*0.8) * 32767 #saturation-> output gain-> pcm
    signal = np.clip(signal, -32768, 32767).astype(np.int16)

    with wave.open(output_file_path, "wb") as out:
        out.setnchannels(1)
        out.setsampwidth(2)
        out.setframerate(samprate)
        out.setnframes(len(signal))
        out.writeframes(signal.tobytes())

    print(f"File saved successfully {output_file_path}")

target_file_path = os.path.join(output_dir,"soft_clipping.wav")
soft_clipping(target_file_path)