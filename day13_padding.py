import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
audio_path = os.getenv("guitar")
output_path = os.getenv("OUTPUT_FOLDER")

def padding(audio_path, output_folder):
    with wave.open(audio_path,"rb") as f:
        params = f.getparams()
        byte_data = f.readframes(params.nframes)
        samples = np.frombuffer(byte_data,dtype=np.int16)

        silence_frames = params.framerate * params.nchannels * 2
        silence_buffer = np.zeros(silence_frames, dtype=np.int16)

    with wave.open (output_folder, "wb") as out:
        
        final = np.concatenate([samples, silence_buffer])
        out.setparams(params)
        out.writeframes(final.tobytes())

    print(f"File saved successfully {output_path}")
    
target_path = os.path.join(output_path, "padding.wav")
padding(audio_path, target_path)

