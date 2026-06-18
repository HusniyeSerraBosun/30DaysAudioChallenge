import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
audio_path = os.getenv("OTHERS")
output_path = os.getenv("OUTPUT_FOLDER")

def audio_loop (audio_path, output_path):
    with wave.open(audio_path, "rb") as f:
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

    with wave.open(output_path, "wb") as output:
        output.setparams(params)
        output.writeframes(final_bytes)
    print(f"File saved successfully: {output_path} ")

target_path = os.path.join(output_path, "audio_loop.wav")
audio_loop(audio_path, target_path)