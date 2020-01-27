import numpy as np
import pydub 
import os
from scipy.io import wavfile


#################################### Data handling functions
# as seen in https://stackoverflow.com/questions/53633177/how-to-read-a-mp3-audio-file-into-a-numpy-array-save-a-numpy-array-to-mp3?noredirect=1&lq=1
def read_mp3(f, normalized=False):
    """MP3 to numpy array"""
    a = pydub.AudioSegment.from_mp3(f)
    y = np.array(a.get_array_of_samples())
    if a.channels == 2:
        y = y.reshape((-1, 2))
    if normalized:
        return a.frame_rate, np.float32(y) / 2**15
    else:
        return a.frame_rate, y

def write_mp3(f, sr, x, normalized=False):
    """numpy array to MP3"""
    channels = 2 if (x.ndim == 2 and x.shape[1] == 2) else 1
    if normalized:  # normalized array - each item should be a float in [-1, 1)
        y = np.int16(x * 2 ** 15)
    else:
        y = np.int16(x)
    song = pydub.AudioSegment(y.tobytes(), frame_rate=sr, sample_width=2, channels=channels)
    song.export(f, format="mp3", bitrate="320k")

def read_all_files_as_numpy():
    pass


####################### Signal processing functions ##################
def range_map(x, inp_range, out_range):
    return (x - inp_range[0]) * (out_range[1] - out_range[0]) / (inp_range[1] - inp_range[0]) + out_range[0]

def pad_length_to_max(soundList, pad_value):
    lens = [len(x) for x in soundList]
    maxLen = pad_value
    paddedArrays = []
    for vect in soundList:
        pad_len = maxLen - len(vect)
        padding = np.zeros((1, pad_len))[0].astype(int)
        paddedArrays.append(np.concatenate((vect, padding)))

    return paddedArrays


def mix_samples(sample1, sample2, r1=0.5, r2=0.5):
    """Overlay two wav samples
    The samples need to have the same sampling rate.
    
    Args:
        sample1: first sound as numpy array
        sample2: second sound as numpy array
        r1: amplitude of first sample
        r2: amplitude of second sample  
    """
  

    # pad with 0 so they are the same length
    if len(sample1) < len(sample2):
        pad_len = len(sample2) - len(sample1)
        padding = np.zeros((1, pad_len))[0].astype(int)
        sample1 = np.concatenate((sample1, padding))
    elif len(sample1) > len(sample2):
        pad_len = len(sample1) - len(sample2)
        padding = np.zeros((1, pad_len))[0].astype(int)
        sample2 = np.concatenate((sample2, padding))

    return r1 * sample1 + r2 * sample2