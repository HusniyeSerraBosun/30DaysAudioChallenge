import wave
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()
input_audio_file = os.getenv("DC_OFFSET")
output_dir = os.getenv("OUTPUT_FOLDER")

def dc_offset(input_path, output_file_path):
    with wave.open(input_path, "rb") as f:
        params = f.getparams()
        byte_data = f.readframes(params.nframes)
        samples = np.frombuffer(byte_data, dtype=np.int16)
        signal_32 = samples.astype(np.float32)

        # DC ofset before cleaning
        before_mean = np.mean(signal_32)
        print(f"Original Signal DC Offset (Mean): {before_mean:.4f}")

        final_signal = signal_32 - before_mean

        # control after cleaning
        after_mean = np.mean(final_signal)
        print(f"DC Offset After Cleaning(Mean): {after_mean:.6f}")

        signal = np.clip(final_signal, -32768, 32767).astype(np.int16)

    with wave.open(output_file_path, "wb") as out:
        out.setparams(params)
        out.writeframes(signal.tobytes())

    print(f"File saved successfully : {output_file_path}")

target_file_path = os.path.join(output_dir, "dc_offset_cleaning.wav")
dc_offset(input_audio_file, target_file_path)