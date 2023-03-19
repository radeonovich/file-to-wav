import wave
import argparse
parser = argparse.ArgumentParser(description='Convert a file to a WAV file')
parser.add_argument('input_file', type=argparse.FileType('rb'), help='the input file')
parser.add_argument('--channels', type=int, default=1, help='the number of audio channels (default: 1)')
parser.add_argument('--framerate', type=int, default=44100, help='the frame rate of the audio data (default: 44100)')
parser.add_argument('--samplewidth', type=int, default=2, help='the sample width of the audio data in bytes (default: 2)')
args = parser.parse_args()

data = args.input_file.read()


output_file = args.input_file.name.rsplit('.', 1)[0] + '.wav'
with wave.open(output_file, 'wb') as wf:
    wf.setnchannels(args.channels)
    wf.setsampwidth(args.samplewidth)
    wf.setframerate(args.framerate)
    wf.writeframesraw(data)
