import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
input_audio_file = os.getenv("guitar")
output_dir = os.getenv("OUTPUT_FOLDER")

def padding(input_path, output_file_path):
    with wave.open(input_path,"rb") as f:
        params = f.getparams()
        byte_data = f.readframes(params.nframes)
        samples = np.frombuffer(byte_data,dtype=np.int16)

        silence_frames = params.framerate * params.nchannels * 2
        silence_buffer = np.zeros(silence_frames, dtype=np.int16)

    with wave.open (output_file_path, "wb") as out:
        
        final = np.concatenate([samples, silence_buffer])
        out.setparams(params)
        out.writeframes(final.tobytes())

    print(f"File saved successfully {output_file_path}")
    
target_path = os.path.join(output_dir, "padding.wav")
padding(input_audio_file, target_path)

