import sublime, sublime_plugin
from os.path import isfile
from os.path import isdir
from os.path import dirname
from os.path import basename
from os import walk
import os
import time
from shutil import move
from shutil import copy
from shutil import copytree
from .libs import Utils as utils

def onChangeEmpty(arg):
    pass

def clearEmpty():
    pass

class QuickMoveToCommand(sublime_plugin.WindowCommand):

    def run(self, paths):

        src = paths[0]

        self.window.show_input_panel(
            'Move to : ', dirname(src),
            self.getOnMoveToDone(src), onChangeEmpty, clearEmpty
        )

    def getOnMoveToDone(self, src):

        def onMoveToDone(arg):

            srcDir = dirname(src)

            isMoveFile = isfile(src)

            dest = arg
            
            while dest.endswith('/'):
                dest = dest[:len(dest) - 1]

            while dest.endswith('\\'):
                dest = dest[:len(dest) - 1]
            
            if srcDir == dest:
                sublime.status_message('nothing to be moved')
                return

            if not isdir(dest):
                try:
                    os.makedirs(dest)
                except OSError as e:
                    sublime.error_message('Destination has to be a valid directory!')
                    return

            views = self.window.views()

            if isMoveFile:
                fileName = utils.getFilename(src)
                for view in views:
                    if view.file_name() != src:
                        continue
                    self.window.focus_view(view)
                    self.window.run_command("close_file")

                if isfile(dest + utils.separator() + fileName):
                    sublime.error_message(dest + utils.separator() + fileName + ' already exist!')
                    return
            else:
                fileOpened = False
                for view in views:
                    if view.file_name().find(src) != 0:
                        continue
                    fileOpened = True
                    self.window.focus_view(view)
                    break
                if fileOpened:
                    sublime.message_dialog('You have views opened, please close them manually, and try move again')
                    return
                if isdir(dest + utils.separator() + basename(src)):
                    sublime.error_message(dest + utils.separator() + basename(src) + ' already exist!')
                    return
            try:
                move(src, dest)
            except OSError as e:
                print(str(e))
            self.window.run_command('refresh_folder_list')

        return onMoveToDone


    def is_enabled(self, paths):
        return utils.oneThingSelected(paths)

    def is_visible(self, paths):
        return utils.oneThingSelected(paths)


class QuickCopyToCommand(sublime_plugin.WindowCommand):

    def run(self, paths):

        src = paths[0]

        self.window.show_input_panel(
            'Copy to : ', dirname(src),
            self.getOnCopyToDone(src), onChangeEmpty, clearEmpty
        )


    def getOnCopyToDone(self, src):

        def onCopyToDone(arg):

            dest = arg
            
            while dest.endswith('/'):
                dest = dest[:len(dest) - 1]

            while dest.endswith('\\'):
                dest = dest[:len(dest) - 1]

            if not isdir(dest):
                try:
                    os.makedirs(dest)
                except OSError as e:
                    sublime.error_message('Destination has to be a valid directory!')
                    return

            views = self.window.views()

            for view in views:
                if view.file_name().find(src) != 0:
                    continue
                self.window.focus_view(view)
                if view.is_dirty():
                    save = sublime.ok_cancel_dialog(utils.getFilename(view.file_name()) + ' has been modified, save changes?')
                    if save:
                        self.window.run_command("save")
                    else:
                        while view.is_dirty():
                            self.window.run_command("undo")
            if isfile(src):
                if isfile(dest + utils.separator() + utils.getFilename(src)):
                    dest = dest + utils.separator() + utils.getFilename(src) + '_' + str(time.time())
                copyMethod =  copy
            else:
                dest = dest + utils.separator() + basename(src)
                if isdir(dest):
                    dest = dest + '_' + str(time.time())
                copyMethod = copytree
                
            try:
                copyMethod(src, dest)
            except OSError as e:
                sublime.status_message(str(e))
            self.window.run_command('refresh_folder_list')

        return onCopyToDone

    def is_enabled(self, paths):
        return utils.oneThingSelected(paths)

    def is_visible(self, paths):
        return utils.oneThingSelected(paths)