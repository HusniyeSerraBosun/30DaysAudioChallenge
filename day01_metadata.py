import os 
import wave
from dotenv import load_dotenv

load_dotenv()
audio_path=os.getenv("AUDIO_PATH")

with wave.open(audio_path, "rb") as f:

    params=f.getparams()
    print(params._fields)

    print("-" * 30)
    print("   AUDIO FILE IDENTITY")
    print("-" * 30)

    print(f"Channels: {params.nchannels}")
    print(f"Bit Depth: {params.sampwidth} bit")
    print(f"Sample Rate: {params.framerate} Hz")
    print(f"Total Frames: {params.nframes}")
    print(f"Compression Type: {params.comptype}")
    print(f"Compression Type: {params.comptype}")
    print(f"Compression Type Name: {params.compname}")

    print("-" * 30)


