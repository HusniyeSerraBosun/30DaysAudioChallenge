import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
audio_path = os.getenv("AUDIO")
output_path = os.getenv("OUTPUT_FOLDER")

def skipping(audio_path, output_path):
    with wave.open(audio_path,"rb") as f:
        params = f.getparams()

        byte_data = f.readframes(params.nframes)
        samples = np.frombuffer(byte_data, dtype=np.int16)
        samples = samples.reshape(-1, params.nchannels)

        samples = samples[::2]
        samples = samples.flatten()
        final = samples.tobytes()

    with wave.open(output_path, "wb") as out:
        out.setparams(params)
        out.writeframes(final)

    print(f"File saved successfully: {output_path}")

target_path = os.path.join(output_path, "skipping.wav")
skipping(audio_path, target_path)
