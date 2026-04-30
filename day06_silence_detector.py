import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
audio_path = os.getenv("AUDIO_PATH")

def zero_calc(audio_path):
    with wave.open(audio_path, "rb") as f:
        params = f.getparams()

        byte_data = f.readframes(params.nframes)
        samples = np.frombuffer(byte_data, dtype=np.int16)

        threshold = 50
        silent_sample_count = np.count_nonzero(np.abs(samples) < threshold)

        zero_duration = silent_sample_count/ (params.framerate*params.nchannels)
        minutes, seconds = divmod(zero_duration, 60)


    print(f"Total silence duration is : {int(minutes):02d}:{int(seconds):02d}")

zero_calc(audio_path)
