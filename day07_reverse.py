import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
audio_path = os.getenv("AUDIO_PATH")
output_path = os.getenv("OUTPUT_FOLDER")

def reverse(audio_path, output_path):
    with wave.open(audio_path, "rb") as f:
        params = f.getparams()

        byte_data = f.readframes(params.nframes)
        samples = np.frombuffer(byte_data, dtype=np.int16)

        samples = samples.reshape(-1, params.nchannels)
        reversed_samples = np.flip(samples, axis=0)
        reversed_samples = reversed_samples.flatten()

        convert_reversed= reversed_samples.tobytes()

    with wave.open(output_path, "wb") as out_f:
        out_f.setparams(params)
        out_f.writeframes(convert_reversed)

    print(f"File saved successfully: {output_path}")

target_path = os.path.join(output_path, "drums_reversed.wav")
reverse(audio_path, target_path)
    