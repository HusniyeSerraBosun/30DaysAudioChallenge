import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
audio_path = os.getenv("AUDIO_PATH")
output_path = os.getenv("OUTPUT_FOLDER")

def trim(audio_path, output_path): 
    with wave.open(audio_path, "rb") as f:
        params = f.getparams()

        byte_data = f.readframes(params.nframes)
        samples = np.frombuffer(byte_data, dtype=np.int16)
        samples_to_remove = params.framerate * params.nchannels * 10  #remove first 10 sec
        trimmed_samples = samples[int(samples_to_remove):]
        convert = trimmed_samples.tobytes()

    with wave.open(output_path, "wb") as out_f:
        out_f.setparams(params)
        out_f.writeframes(convert)

    print(f"File saved successfully: {output_path}")

target_path = os.path.join(output_path, "drums_trimmed.wav")
trim(audio_path, target_path)