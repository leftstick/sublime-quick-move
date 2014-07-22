import sublime
import os.path

def getBaseName(fullpath):
    return os.path.basename(fullpath)

def oneThingSelected(paths):
    return len(paths) == 1

def removeNonPathEnd(path):
    return path.rstrip('\\/')

def getParent(path):
    return os.path.dirname(path)

def revert(view):
    while view.is_dirty():
        view.run_command('undo');