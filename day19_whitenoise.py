import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
output_dir = os.getenv("OUTPUT_FOLDER")

def white_noise(output_file_path):
    samprate = 44100
    duration = 5
    N = samprate * duration
    noise = (np.random.uniform(low=-1.0, high=1.0, size=N) * 32767).astype(np.int16)
    # Note: Can use np.random.normal for Gaussian distribution

    with wave.open (output_file_path, "wb") as out:
        out.setnchannels(1)
        out.setsampwidth(2)
        out.setframerate(samprate)
        out.setnframes(N)
        out.writeframes(noise.tobytes()) 

    print(f"Files saved successfully {output_file_path}")

target_path = os.path.join(output_dir, "white_noise.wav")
white_noise(target_path)
    