import sublime
from os.path import expanduser

PLUGIN_NAME = 'sublime-quick-move'

def separator():
    separator = '/'
    if sublime.platform() == "windows":
        separator = '\\'
    return separator

def getFilename(fullpath):
    return fullpath[fullpath.rfind(separator()) + 1:]

def oneThingSelected(paths):
    return len(paths) == 1

def getPluginDir():
    return sublime.packages_path() + separator() + PLUGIN_NAME

def getHome():
    return expanduser('~')
