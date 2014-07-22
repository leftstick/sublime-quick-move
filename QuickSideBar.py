import sublime, sublime_plugin
from os.path import join, isfile, isdir
import time
import shutil
from .libs import Utils as utils
from .libs.Operation import Operation

class QuickMoveToCommand(Operation, sublime_plugin.WindowCommand):

    def run(self, paths):
        src = paths[0]
        self.showOperPanel(self.window, 'Move to : ', src, 'move')


    def doOperation(self, src, dest, views):
        
        srcDir = utils.getParent(src)

        isSrcFile = isfile(src)

        if srcDir == dest:
            sublime.status_message('nothing to be moved')
            return

        destPath = join(dest, utils.getBaseName(src))
        if isSrcFile:
            if isfile(destPath):
                sublime.error_message(destPath + ' already exist!')
                return
        else:
            if isdir(destPath):
                sublime.error_message(destPath + ' already exist!')
                return

        try:
            shutil.move(src, dest)
        except OSError as e:
            print(str(e))
        self.window.run_command('refresh_folder_list')


    def is_enabled(self, paths):
        return utils.oneThingSelected(paths)

    def is_visible(self, paths):
        return utils.oneThingSelected(paths)


class QuickCopyToCommand(Operation, sublime_plugin.WindowCommand):

    def run(self, paths):
        src = paths[0]
        self.showOperPanel(self.window, 'Copy to : ', src, 'copy')

    
    def doOperation(self, src, dest, views):
        isSrcFile = isfile(src)

        dest = join(dest, utils.getBaseName(src))
        if isSrcFile:
            if isfile(dest):
                dest = dest + '_' + str(time.time())
            copyMethod =  shutil.copy
        else:
            if isdir(dest):
                dest = dest + '_' + str(time.time())
            copyMethod = shutil.copytree
            
        try:
            copyMethod(src, dest)
        except OSError as e:
            sublime.status_message(str(e))
        self.window.run_command('refresh_folder_list')


    def is_enabled(self, paths):
        return utils.oneThingSelected(paths)

    def is_visible(self, paths):
        return utils.oneThingSelected(paths)