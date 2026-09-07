import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
input_audio_file = os.getenv("AUDIO")
output_dir = os.getenv("OUTPUT_FOLDER")

def doubling(input_path, output_file_path):
    with wave.open(input_path,"rb") as f:
        params = f.getparams()

        byte_data = f.readframes(params.nframes)
        samples = np.frombuffer(byte_data, dtype=np.int16)
        samples = samples.reshape(-1, params.nchannels)

        samples = np.repeat(samples, repeats=2, axis=0)
        samples = samples.flatten()
        final = samples.tobytes()

    with wave.open(output_file_path, "wb") as out:
        out.setparams(params)
        out.writeframes(final)
    
    print(f"File saved successfully: {output_file_path}")

target_path = os.path.join(output_dir, "doubling.wav")
doubling(input_audio_file, target_path)
