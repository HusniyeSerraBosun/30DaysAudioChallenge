import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
audio_path = os.getenv("AUDIO_PATH_V2")
output_path = os.getenv("OUTPUT_FOLDER")

def fadein_fadeout(audio_path, output_path):
    with wave.open(audio_path, "rb") as f:
        params = f.getparams()

        byte_data = f.readframes(params.nframes)
        samples = np.frombuffer(byte_data, dtype=np.int16).copy() # Create a mutable copy to prevent read-only memory errors
        samples = samples.reshape(-1, params.nchannels) # Reshape to table with 2 columns: [Left, Right]

        fade_frames = params.framerate *  5

        # Generate linear gain ramps from 0.0 to 1.0
        fade_in_ramp = np.linspace(0.0, 1.0, fade_frames)
        fade_out_ramp = np.linspace(1.0, 0.0, fade_frames)

        #Prepare ramp for both Left and Right channels(Broadcasting)
        samples[:fade_frames] = samples[:fade_frames] * fade_in_ramp[:, np.newaxis]
        samples[-fade_frames:] = samples[-fade_frames:] *fade_out_ramp[:, np.newaxis]

        # Revert to 1D array before converting to bytes
        samples = samples.flatten()
        convert_bytes = samples.tobytes()

    with wave.open(output_path, "wb") as out_f:
        out_f.setparams(params)
        out_f.writeframes(convert_bytes)

    print(f"File saved successfully: {output_path}")

target_path = os.path.join(output_path, "drums_fade_in_out.wav")
fadein_fadeout(audio_path, target_path) 