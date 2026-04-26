import os
import wave
import numpy as np
from dotenv import load_dotenv

load_dotenv()
audio_path = os. getenv("AUDIO_PATH")
output_path= os.getenv("OUTPUT_FOLDER")

def mono_conv(audio_path, output_path):
    with wave.open(audio_path,"rb") as f:
        params = f.getparams()

        byte_data = f.readframes(params.nframes)
        samples = np.frombuffer(byte_data, dtype=np.int16)

        if params.nchannels == 2:
            new_matrix = samples.reshape(-1,2)
            average = np.mean(new_matrix, axis=1)
            conv_int16= average.astype(np.int16)
            mono_bytes = conv_int16.tobytes()
        else:
            mono_bytes = byte_data

    with wave.open(output_path, "wb") as out_f:
        out_f.setnchannels(1)
        out_f.setframerate(params.framerate)
        out_f.setsampwidth(params.sampwidth)
        out_f.writeframes(mono_bytes)

    print(f"Dosya başarıyla kaydedildi: {output_path}")

target_path= os.path.join(output_path, "drums_mono.wav")
mono_conv(audio_path,target_path)