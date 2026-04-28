import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
audio_path = os.getenv("AUDIO_PATH")
output_path = os.getenv("OUTPUT_FOLDER")

def normalization(audio_path, output_path):
    with wave.open(audio_path, "rb") as f:
        params = f.getparams()

        byte_data = f.readframes(params.nframes)
        samples = np.frombuffer(byte_data, dtype=np.int16)
        max_value = np.abs(samples).max()

        norm_coeff = 31000/max_value #31000 for headroom
        gain = samples*norm_coeff

        conv_int16 = gain.astype(np.int16)
        new_bytes = conv_int16.tobytes()

    with wave.open(output_path, "wb") as out_f:
        out_f.setparams(params)
        out_f.writeframes(new_bytes)
    
    print(f"File saved successfully: {output_path}")

target_path = os.path.join(output_path, "drums_norm.wav")
normalization(audio_path, target_path)
