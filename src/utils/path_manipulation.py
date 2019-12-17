import os
import sys

def splitall(path):
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts

def contains_filetype(path, file_extesion=None, subfolders=False):
    """Returns True if path folder contains any files of specified extension.
    if subfolders is True, looks in all subdirectories. 
    """

    if file_extesion is None:
        raise ValueError("No file extension was passed to the function")

    _, subfolderList, files = next(os.walk(path))
    if subfolders is True:
        if len(subfolderList) > 0:
            for subfolder in subfolderList:
                return contains_filetype(os.path.join(path, subfolder), file_extesion=file_extesion, subfolders=True)
 
    if any(f.endswith(file_extesion) for f in files):
        return True
    else:
        return False

    