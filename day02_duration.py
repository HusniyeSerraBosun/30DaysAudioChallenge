import os
import wave
from dotenv import load_dotenv

load_dotenv()
audio_path=os.getenv("AUDIO_PATH")

def sound_len_calc(audio_path):
    with wave.open(audio_path,"rb") as f:
        sound_length=f.getnframes()/f.getframerate()        
    minutes, seconds= divmod(sound_length, 60)
    formatted_time= f"{int(minutes):02d}:{int(seconds):02d}"
    return formatted_time

print(f"Duration: {sound_len_calc(audio_path)}")