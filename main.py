import aubio
import pyaudio
import numpy as np 
import keyboard

#Initate Pyaudio 
p = pyaudio.PyAudio()

#stream thing
stream = p.open(format=pyaudio.paFloat32,
    channels=1, rate=20000, input=True,
    frames_per_buffer=1024)

#aubio thing
pDetection = aubio.pitch(method = "default", buf_size = 2048,
    hop_size = 2048//2, samplerate = 20000)


# Set unit.
pDetection.set_unit("Hz")
pDetection.set_silence(-40)

while True:

    data = stream.read(1024)
    samples = np.frombuffer(data,
        dtype=aubio.float_type)
    pitch = pDetection(samples)[0]

    pitch = float(pitch)
    print(str(pitch))

    #KEYBOARD things

    #These link certain pitches/notes to different keys 
    
    #E3
    if pitch > 162 and pitch < 166:
        keyboard.press('w')
    #C3
    elif pitch > 128 and pitch < 133:
        keyboard.press('a')
    #D3
    elif pitch > 144 and pitch < 148:
        keyboard.press('s')
    #G3
    elif pitch > 194 and pitch <198:
        keyboard.press('d')
    #F3
    elif pitch > 172 and pitch < 178:
        keyboard.press('q')
    #A3
    elif pitch > 218 and pitch < 222:
        keyboard.press('e')
    #B2 
    elif pitch > 121 and pitch < 125:
        keyboard.press('tab')
    
  
