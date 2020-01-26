import os
import sys
import logging

scriptPath = os.path.dirname(os.path.abspath(__file__))
projRootPath = os.path.abspath(
    os.path.join(scriptPath ,
                os.path.join('..', '..')))
sys.path.append(projRootPath)

from pydub import AudioSegment
import scipy
import csv

from src.utils.console_functions import printProgressBar
from src.utils.path_manipulation import splitall, contains_filetype
from src.utils.sound_functions import mix_samples

# Setup Logger first
logger = logging.getLogger()
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.WARNING)
log_f = logging.FileHandler(os.path.join("logs" ,"mixing_log.log"))
logger.addHandler(log_f)

# Setup 
dataDir = "data"
sampleDir = os.path.join("raw", "mp3")
firstInstrument = "violin"
secondInstrument = "guitar"

mp_path = os.path.join(projRootPath, dataDir, sampleDir)

roots = []
instruments = []

# r=root, d=directories, f = files
for r, d, f in os.walk(mp_path):
    roots.append(r)
    instruments.append(os.path.split(r)[1])

# print(instruments)
# print(len(roots))

# setup save location
mixedDir = "mixed_samples"
mixedDirPath = os.path.join(projRootPath, dataDir, mixedDir)
os.makedirs(mixedDirPath, exist_ok=True)

# setp samples locations
firstSamplesDir = os.path.join(mp_path, firstInstrument)
secondSamplesDir = os.path.join(mp_path, secondInstrument)
savePath = os.path.join(mixedDirPath, firstInstrument+"_and_"+secondInstrument)
os.makedirs(savePath, exist_ok=True)

firstRoot, firstFolders, firstFiles = next(os.walk(firstSamplesDir))
secondRoot, secondFolders, secondFiles = next(os.walk(secondSamplesDir))

if len(firstFiles) == 0:
    raise ValueError("There are no files in root direcory "+firstSamplesDir)

if not contains_filetype(firstSamplesDir, file_extesion="wav"):
    raise ValueError("There are no wav files in root folder "+firstSamplesDir)

if len(secondFiles) == 0:
    raise ValueError("There are no files in root direcory "+secondSamplesDir)

if not contains_filetype(secondSamplesDir, file_extesion="wav"):
    raise ValueError("There are no wav files in root folder "+secondSamplesDir)

firstSamples = [x for x in firstFiles if x.endswith(".wav")]
secondSamples = [x for x in secondFiles if x.endswith(".wav")]


# fs1, data1 = wavfile.read(sample1)
# fs2, data2 = wavfile.read(sample2)
# assert fs1 == fs2

logger.info("Mixing samples from " + firstSamplesDir + " and " + secondSamplesDir)

with open(os.path.join(savePath, "mixing_trace.csv"), "w", newline='') as traceFile:
    csvCols = ["mixedFile", "file1", "file2", "amplitude1", "amplitude2"]
    traceWriter = csv.writer(traceFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
    traceWriter.writerow(csvCols)
    for i, file1 in enumerate(firstSamples):
        printProgressBar(0, len(firstSamples), prefix = file1, suffix = 'Complete', length = 50)

        for j, file2 in enumerate(secondSamples):
            if file2.endswith('.wav'):
                try:
                    firstFilePath = os.path.join(firstRoot, file1)
                    secondFilePath = os.path.join(secondRoot, file2)

                    r1 = 0.5
                    r2 = 0.5
                    mixedSample, sr = mix_samples(firstFilePath, secondFilePath, r1=r1, r2=r2)
                    mixedFileName = file1.replace(".wav", "") + "_with_" + file2
                    scipy.io.wavfile.write(filename=os.path.join(savePath, mixedFileName), rate=sr, data=mixedSample)
                    traceWriter.writerow([mixedFileName, firstFilePath, secondFilePath, r1, r2])
                    logger.info("File " + file1 + " and " + file2 + " were overlapped")

                except Exception as e:
                    logger.warning("Could not overlap files " + file1 + " and " + file2)
                    print(e)

        # Update Progress Bar
        printProgressBar(i + 1, len(firstSamples), prefix = file1, suffix = 'Complete', length = 50)

logger.info("Completed\n")

