import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
input_audio_file=os.getenv("AUDIO_PATH")
output_dir=os.getenv("OUTPUT_FOLDER")

def gain(input_path, output_file_path):
    with wave.open(input_path, "rb") as f:
        params=f.getparams()

        byte_data = f.readframes(params.nframes)
        sample = np.frombuffer(byte_data, dtype=np.int16)
        gain = sample*0.5
        conv_int16 = gain.astype(np.int16)
        gain_bytes = conv_int16.tobytes()

    with wave.open(output_file_path, "wb") as out_f:
        out_f.setparams(params)
        out_f.writeframes(gain_bytes)
    
    print(f"File saved successfully: {output_file_path}")

target_path = os.path.join(output_dir, "drums_gain.wav")
gain(input_audio_file, target_path)

