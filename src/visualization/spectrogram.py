import os 

scriptPath = os.path.dirname(os.path.abspath(__file__))
projRootPath = os.path.abspath(
    os.path.join(scriptPath ,
                os.path.join('..', '..')))

import numpy as np

# matplotlib for displaying the output
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from scipy import signal
from scipy.io import wavfile

# and IPython.display for audio output
import IPython.display

# Librosa for audio
import librosa

# And the display module for visualization
import librosa.display

#### Path to data
# Get data files
two_up =  os.path.abspath(os.path.join('.' ,"../.."))
print("Project root path is: ", two_up)


dataDirName = "data"
rawDataDirName = "converted_wav"
className = "violin"
# className = "guitar"
data_path = os.path.join(projRootPath, dataDirName, rawDataDirName, className)

print(data_path)
root_paths = []

# Get all files from data_path 
# r=root, d=directories, f = files
(_, d, allFiles) = next(os.walk(data_path))
wavFiles = [f for f in allFiles if f.endswith(".wav")]


file = wavFiles[1]
sample_rate, samples = wavfile.read(os.path.join(data_path, file))
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

# all spectrogram
plt.pcolormesh(times, frequencies, spectrogram)
plt.imshow(spectrogram)
plt.ylabel('Frequency')
plt.gca().invert_yaxis()
plt.xlabel('Time')
plt.show()