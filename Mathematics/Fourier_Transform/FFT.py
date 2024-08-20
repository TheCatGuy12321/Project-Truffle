import numpy as np
import matplotlib.pyplot as plt
import pydub
from sys import argv as arg

if len(arg) != 2:
    print(f"""Usage: python {arg[0]} (wav file)
\nRuns a Fourier Transform through a wav file and graphs the output""")
    exit()


filename = arg[1]

try:
    a = pydub.AudioSegment.from_wav(filename)
    a = a.set_channels(1)
    y = np.array(a.get_array_of_samples())
    aud_data = y
except:
    print("Error, try checking the file path")
    exit(1)
channel_1 = aud_data[:]

fft = np.fft.fft(channel_1)

fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.tight_layout()
ax1.set_title("Input Function (.wav)")
ax2.set_title("Fourier Transform (real)")
ax3.set_title("Fourier Transform (imag)")
ax1.plot(channel_1)
ax2.plot(abs(fft.real))
ax3.plot(abs(fft.imag))
plt.show()
