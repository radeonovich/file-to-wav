# Convert any file to WAV

This Python script converts any file to a wave file by treating the raw byte data of the file as audio data. The resulting wave file will sound like noise.
### Warning:
Resulting file will be loud.

## Usage

 
To use the script, run the following command in a terminal or command prompt:

`python convert_exe_to_wave.py <input_file>`

You can also use additional parameters:

`--channels` - the number of audio channels (default: 1)

`--framerate` - sampling frequency in Hz (default: 44100)

`--samplewith` - bit depth in bytes (default: 2)

The script will generate a wave file with the same name as the input file, but with a `.wav` extension. The wave file will be saved in the same directory as the input file.

