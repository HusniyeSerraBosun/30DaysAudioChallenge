# 30 Days Audio Challenge: Digital Audio Processing Fundamentals

A personal 30-day challenge where I implement core audio manipulation algorithms, sample-level math, and basic effects in Python using NumPy and the standard `wave` module.

---

## Technology Stack

### Languages & Tools
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Audio%20Buffers-013243?style=flat&logo=numpy&logoColor=white)
![Wave](https://img.shields.io/badge/Wave-Standard%20Library-blue?style=flat)
![python-dotenv](https://img.shields.io/badge/python--dotenv-Environment-ECD53F?style=flat&logoColor=black)

---

## Why This Project?

Most high-level Python audio packages handle buffer reading and transformations automatically. I started this challenge to build a solid ground-level understanding of digital sound by working directly with uncompressed WAV samples and NumPy arrays—no black-box DSP packages involved.

The challenge is split into 4 weekly focus areas:
1. **Week 1: Data & Basic Manipulation** — Parsing WAV headers, mono conversion, and simple amplitude math.
2. **Week 2: Editing & Time-Domain Processing** — Slicing arrays, volume fades, loops, and basic speed adjustments.
3. **Week 3: Signal Generation & Waveforms** *(In Progress)* — Synthesizing standard waveforms and applying clipping curves.
4. **Week 4: Audio Effects & Analysis** *(Planned)* — Delays, stereo panning, and basic audio metrics (RMS, ZCR).

> **Current Status:** ⚠️ In Progress (15 / 30 Days Completed)

---

## Roadmap & Progress Tracker

### Week 1: Data & Basic Manipulation (Completed)
- [x] **Day 01 - Metadata Extraction:** Read and print sample rate, channels, and bit depth from file headers.
- [x] **Day 02 - Duration Calculation:** Calculate duration in seconds using frame count and sample rate.
- [x] **Day 03 - Stereo to Mono Conversion:** Average stereo channels into a single mono buffer.
- [x] **Day 04 - Gain Adjustment:** Scale audio amplitude linearly ($0.5\times$ attenuation).
- [x] **Day 05 - Peak Normalization:** Scale peak sample value to full dynamic range ($1.0$).
- [x] **Day 06 - Silence Detection:** Measure the total duration of zero-value samples in a file.
- [x] **Day 07 - Reverse Audio:** Flip the sample array along the time axis.

### Week 2: Editing, Slicing & Time-Domain Processing (Completed)
- [x] **Day 08 - Trim Audio:** Discard the first 500 ms slice from the audio buffer.
- [x] **Day 09 - Linear Fade-In:** Apply a linear volume ramp-up ($0 \to 1$) over the first 2 seconds.
- [x] **Day 10 - Linear Fade-Out:** Apply a linear volume ramp-down ($1 \to 0$) over the final 2 seconds.
- [x] **Day 11 - Cross-Fade:** Overlap and blend boundaries between two audio files.
- [x] **Day 12 - Audio Looping:** Repeat and concatenate an audio buffer 3 times.
- [x] **Day 13 - Digital Silence Padding:** Append 2 seconds of zero-samples to the end of a track.
- [x] **Day 14 - Speed Up (Skipping):** Double playback speed by dropping alternate samples.
- [x] **Day 15 - Slow Down (Doubling):** Halve playback speed by repeating consecutive samples.

### Week 3: Signal Generation & Waveforms
- [ ] **Day 16 - Sine Wave Synthesis:** Generate and export a pure 440 Hz (A4) tone.
- [ ] **Day 17 - Square Wave Synthesis:** Generate a periodic square waveform ($\pm 1$).
- [ ] **Day 18 - Sawtooth Wave Synthesis:** Generate a linear ramp-up sawtooth waveform.
- [ ] **Day 19 - White Noise Generator:** Generate uniform random noise samples.
- [ ] **Day 20 - Hard Clipping:** Hard threshold limiting for amplitudes exceeding $0.7$.
- [ ] **Day 21 - Soft Clipping:** Non-linear threshold saturation using $\tanh$.
- [ ] **Day 22 - Amplitude Modulation (AM):** Modulate carrier amplitude with an LFO (tremolo).

### Week 4: Audio Effects & Analysis
- [ ] **Day 23 - DC Offset Removal:** Calculate average signal displacement and re-center at zero.
- [ ] **Day 24 - Stereo Panning:** Shift audio from left to right channel over 5 seconds.
- [ ] **Day 25 - Bitcrusher:** Reduce audio resolution via sample quantization/rounding.
- [ ] **Day 26 - RMS Calculation:** Calculate Root Mean Square energy across audio frames.
- [ ] **Day 27 - Zero-Crossing Rate (ZCR):** Count buffer sign changes for fundamental pitch estimation.
- [ ] **Day 28 - Feedback Echo / Delay:** Mix a delayed ($500\text{ ms}$) and attenuated copy back into the signal.
- [ ] **Day 29 - Ping-Pong Delay:** Alternate delayed reflections between left and right channels.
- [ ] **Day 30 - Multi-FX Processing Chain:** Chain Gain $\to$ Fade $\to$ Clipping in a single processing sequence.

---

## Project Structure

```text
30DaysAudioChallenge/
├── day01_metadata.py           # Individual daily exercise scripts
├── day02_duration.py
├── day03_mono_conv.py
├── ...
├── .gitignore
└── README.md
```
---
## Setup & Running
### 1. Clone & Setup Environment
````
git clone <repository-url>
cd 30DaysAudioChallenge

python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install numpy python-dotenv
````
### 2. Configure Local Paths
Create a `.env` file in the project root to point to your local .wav files.

```
AUDIO_PATH="path/to/your/input.wav"
OUTPUT_FOLDER="path/to/your/output/"
```
### 3. Run a Script
Each day is kept as an independent, self-contained script.
```
python day01_metadata.py
```
## Next Steps
- **C++ Port**: Once I finish the 30 days in Python, my goal is to re-implement these exact 30 tasks in modern C++ to dive into manual memory management, buffer pointers, and real-time execution performance.
