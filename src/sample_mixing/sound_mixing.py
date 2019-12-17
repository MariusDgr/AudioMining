import os
import sys
import logging

scriptPath = os.path.dirname(os.path.abspath(__file__))
projRootPath = os.path.abspath(
    os.path.join(scriptPath ,
                os.path.join('..', '..')))
sys.path.append(projRootPath)

from pydub import AudioSegment

from src.utils.console_functions import printProgressBar
from src.utils.path_manipulation import splitall, contains_filetype

# Setup Logger first
logger = logging.getLogger()
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
log_f = logging.FileHandler(os.path.join("logs" ,"conversion_log.log"))
logger.addHandler(log_f)

daraDir = "data"
sampleDir = "converted_wav"
classDir = "violin"
mixedDir = "converted_wav"

mp_path = os.path.join(projRootPath, daraDir, sampleDir)

roots = []
instruments = []

# r=root, d=directories, f = files
for r, d, f in os.walk(mp_path):
    print(r)
    roots.append(r)
    instruments.append(os.path.split(r)[1])

print(len(instruments))
