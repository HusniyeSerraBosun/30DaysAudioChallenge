import wave
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()
output_dir = os.getenv("OUTPUT_FOLDER")

def sin_wave(output_file_path):
    #sin wave = A.sin(2pi*f*t + phi)
    #sample_rate = 44100, duration = 3sec, samples = 44100*3 =132300

    t = np.linspace(start=0, stop=3, num=132300 , endpoint=False) #time vector
    a = 1 #amplitude
    f = 440 # frequency -- note A 
    phi = 0 #phase shift

    sin_wave_v1 = a * np.sin(2*np.pi * f * t + phi) #sin_wave contains float values between [-1,1] right now. 

    sin_wave_v2 = sin_wave_v1 * 32767 
    sin_wave_v3 = sin_wave_v2.astype(np.int16)
    sin_final_wave = sin_wave_v3.tobytes()

    with wave.open(output_file_path, "wb") as output:
        output.setframerate(44100)
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setnframes(len(sin_wave_v3))
        output.writeframes(sin_final_wave)

    print(f"File saved successfully {output_file_path}")

target_file_path = os.path.join(output_dir,"sin_440hz.wav")
sin_wave(target_file_path)
