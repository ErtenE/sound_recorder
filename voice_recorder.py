import sounddevice as sd
from scipy.io.wavfile import write
#sample rate
fs = 44100 
# recording duration seconds
seconds = 20  

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  
write('output.wav', fs, myrecording) 