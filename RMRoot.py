import pathlib
from pathlib import Path
import os
def getRoot():
    return pathlib.Path(__file__).parent.resolve()

def putLocalDirectory(name: str):
    path = getRoot() / Path(name)
    Path(path).mkdir(parents=True, exist_ok=True)
    #os.mkdir(path,)
    return path.absolute()

