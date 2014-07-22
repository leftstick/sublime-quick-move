import sublime
from . import Utils as utils
from os.path import isfile, isdir
import os
import shutil

class Operation():

    def showOperPanel(self, window, caption, src, oper):
        window.show_input_panel(
            caption, utils.getParent(src),
            self.getOperDone(src, window, oper), self.onChangeEmpty, self.clearEmpty)

    def getOperDone(self, src, window, oper):

        def operDone(arg):

            dest = utils.removeNonPathEnd(arg)
            isSrcFile = isfile(src)

            newlyCreated = False

            if not isdir(dest):
                try:
                    os.makedirs(dest)
                    newlyCreated = True
                except OSError as e:
                    sublime.error_message('Destination has to be a valid directory!')
                    return
            
            views = window.views()

            if isSrcFile:
                for view in views:
                    if view.file_name() != src:
                        continue
                    window.focus_view(view)
                    window.run_command("close_file")
                    break
            else:
                for view in views:
                    if view.file_name().find(src) != 0:
                        continue
                    if oper == 'move':
                        window.focus_view(view)
                        if newlyCreated:
                            shutil.rmtree(dest)
                        sublime.message_dialog('You have views opened, please close them manually, and try move again')
                        return
                        
                    if view.is_dirty():
                        window.focus_view(view)
                        save = sublime.ok_cancel_dialog(utils.getBaseName(src) + ' has been modified, save changes?')
                        if save:
                            view.run_command('save')
                        else:
                            utils.revert(view)

            self.doOperation(src, dest, views)

        return operDone

    def doOperation(self, src, dest, views):
        pass

    def onChangeEmpty(self, arg):
        pass

    def clearEmpty(self):
        pass