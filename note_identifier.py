import wave


def read_wav_file(file_loc):
	wav = wave.open(file_loc, "r")
	frame_rate = wav.getframerate()
	wav_bytes = wav.readframes(wav.getnframes())

if __name__ == "__main__":
	read_wav_file("wav_files/lotr.wav")

'''
1) import wav file

2) generate audio wave from file

3) find best fitting sin wave
	- look at change in frequency
		- slides
		- vibrato
		
4) use sin wave to determine note (will be different for chord based stuff)


TODO:

look at actual sound files from guitar (use midpoint)


lord of the rings notes at 3:50 (should be a low d)

'''