import os
import sys
import logging

scriptPath = os.path.dirname(os.path.abspath(__file__))
projRootPath = os.path.abspath(
    os.path.join(scriptPath ,
                os.path.join('..', '..')))

from pydub import AudioSegment

sys.path.append(projRootPath)

from src.utils.console_functions import printProgressBar
from src.utils.path_manipulation import splitall

# Setup Logger first
logger = logging.getLogger()
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
log_f = logging.FileHandler(os.path.join("logs" ,"conversion_log.log"))
logger.addHandler(log_f)

dataDirName = "data"
mpDirName = "raw"
dataSetName = "mp3"
wavDirName = "converted_wav"

mp_path = os.path.join(projRootPath, dataDirName, mpDirName, dataSetName)

roots = []
instruments = []

# r=root, d=directories, f = files
for r, d, f in os.walk(mp_path):
    roots.append(r)
    instruments.append(os.path.split(r)[1])

# print(instruments)
# print(len(roots))

# print(roots)

# remove root folder first
# print(mp_path)
roots.remove(mp_path)

remainingInstruments = []

for r in roots:
    _, _, files = next(os.walk(r))

    pathList = splitall(r)
    instrument = pathList[-1]
    mpIndx = pathList.index(dataSetName)
    sameStructPath = os.path.join(*pathList[mpIndx+1:])

    convPath = os.path.join(projRootPath, 
                            dataDirName, 
                            wavDirName, 
                            sameStructPath)

    
    os.makedirs(convPath, exist_ok=True)

    logger.info(instrument + " with " + str(len(files)) + " files.")

    if len(files) > 0:
        printProgressBar(0, len(files), prefix = instrument, suffix = 'Complete', length = 50)

        for i, f in enumerate(files):
            if f.endswith('.mp3'):
                try:
                    sound = AudioSegment.from_mp3(os.path.join(r, f))
                    wavPath = os.path.join(convPath, f.replace(".mp3", ".wav"))
                    sound.export(wavPath, format="wav")
                    logger.info("File " + f + "was converted.")

                except:
                    logger.warning("File " + f + " could not be converted.")

                # Update Progress Bar
                printProgressBar(i + 1, len(files), prefix = instrument, suffix = 'Complete', length = 50)

    logger.info("Completed\n")



    
