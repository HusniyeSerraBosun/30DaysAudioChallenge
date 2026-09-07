import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
input_audio_file = os.getenv("OTHERS")
output_dir = os.getenv("OUTPUT_FOLDER")

def audio_loop (input_path, output_file_path):
    with wave.open(input_path, "rb") as f:
        params = f.getparams()
        byte_data = f.readframes(params.nframes)
        samples = np.frombuffer(byte_data, dtype=np.int16)

        N = len(samples)
        # Create an empty buffer 3 times the size of original audio
        output_buffer = np.zeros(N*3, dtype=np.int16)

        for i in range(3):
            # Calculate dynamic memory bounds for each repetition
            start = i*N
            end = (i+1)*N
            # Copy original samples into the calculated memory slice
            output_buffer[start : end] = samples

    # Convert the populated buffer into raw audio bytes        
    final_bytes = output_buffer.tobytes()

    with wave.open(output_file_path, "wb") as output:
        output.setparams(params)
        output.writeframes(final_bytes)
    print(f"File saved successfully: {output_file_path} ")

target_path = os.path.join(output_dir, "audio_loop.wav")
audio_loop(input_audio_file, target_path)
