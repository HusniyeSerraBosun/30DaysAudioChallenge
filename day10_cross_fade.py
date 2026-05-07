import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
song_one = os.getenv("SONG_ONE")
song_two = os.getenv("SONG_TWO")
output_path = os.getenv("OUTPUT_FOLDER")

def crossfade(song_one, song_two, output_path):
    with wave.open(song_one, "rb") as one:
        params_one = one.getparams()
        byte_data_one = one.readframes(params_one.nframes)
        samples_one = np.frombuffer(byte_data_one, dtype=np.int16).copy()
        fade_frames_one = params_one.framerate * params_one.nchannels * 4
        fade_out_ramp = np.linspace(1.0, 0.0, fade_frames_one)
        convert_one = samples_one.tobytes()

    with wave.open(song_two, "rb") as two:
        params_two = two.getparams()
        byte_data_two = two.readframes(params_two.nframes)
        samples_two = np.frombuffer(byte_data_two, dtype=np.int16).copy()
        fade_frames_two = params_two.framerate * params_two.nchannels * 4
        fade_in_ramp = np.linspace(0.0, 1.0, fade_frames_two)
        convert_two = samples_two.tobytes()

    with wave.open(output_path, "wb") as out:
        out.setparams(params_one)

        song_one_end = samples_one[:-fade_frames_one]
        
        first_part = samples_one[-fade_frames_one:] *fade_out_ramp
        second_part = samples_two[:fade_frames_two] * fade_in_ramp
        combined_middle = (first_part + second_part).astype(np.int16)

        song_two_start = samples_two[fade_frames_two:]

        final = np.concatenate([song_one_end,combined_middle,song_two_start])
        out.writeframes(final.tobytes())
    
    print(f"File saved successfully {output_path}")

target_path = os.path.join(output_path, "cross_fade.wav")
crossfade(song_one, song_two, target_path)