import wave
import sys
import os

if len(sys.argv) < 2:
    print("Usage: python convert_exe_to_wave.py <input_file>")
    sys.exit()

input_file = sys.argv[1]
output_file = os.path.splitext(input_file)[0] + '.wav'

with open(input_file, 'rb') as f:
    data = f.read()

with wave.open(output_file, 'wb') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(44100)
    wf.writeframesraw(data)
    