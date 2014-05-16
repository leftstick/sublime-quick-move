import sublime, sublime_plugin
from .AchillesSideBarBase import AchillesSideBarBase
from string import Template
import getpass
import datetime
import calendar
from os.path import isfile

class AchillesSideBarAddNgCtrlCommand(AchillesSideBarBase, sublime_plugin.WindowCommand):

    def get_input_panel_caption(self):
        return 'Enter a name for the ngController'

    def get_template_file_name(self):
        return 'NgController.js'

    def run(self, dirs):
        self.show_input_panel(dirs)

    def handle_template(self, tplStr, outputDir, input_string, fileName):
        name = input_string[0].upper() + input_string[1:]
        fileName = fileName[0].upper() + fileName[1:]
        
        if isfile(outputDir + '/' + fileName):
            self.window.open_file(outputDir + '/' + fileName)
            return

        tpl = Template(tplStr)
        date = datetime.datetime.now()
        ctrlStr = tpl.substitute(name=name, user=getpass.getuser(), date=calendar.month_name[date.month]+' '+str(date.day)+'th, '+str(date.year))
        outputFile = open(outputDir + '/' + fileName, 'w')
        outputFile.write(ctrlStr)
        self.window.open_file(outputDir + '/' + fileName)

    def is_visible(self, dirs):
        if self.isStrictMode():
            return len(dirs) == 1 and dirs[0].endswith('controller')
        else:
            return True
            
class AchillesSideBarAddNgDirCommand(AchillesSideBarBase, sublime_plugin.WindowCommand):

    def get_input_panel_caption(self):
        return 'Enter a name for the ngDirective'

    def get_template_file_name(self):
        return 'NgDirective.js'

    def run(self, dirs):
        self.show_input_panel(dirs)

    def handle_template(self, tplStr, outputDir, input_string, fileName):
        
        dirs = ''
        for index, s in enumerate(input_string):
            if index == 0:
                dirs += s.lower()
            else:
                if s.isupper():
                    dirs += '-' + s.lower()
                else:
                    dirs += s
        fileName = fileName[0].upper() + fileName[1:]
        name = input_string[0].lower() + input_string[1:]

        if isfile(outputDir + '/' + fileName):
            self.window.open_file(outputDir + '/' + fileName)
            return

        tpl = Template(tplStr)
        date = datetime.datetime.now()
        dirStr = tpl.substitute(name=name, user=getpass.getuser(), date=calendar.month_name[date.month]+' '+str(date.day)+'th, '+str(date.year), dir=dirs)
        outputFile = open(outputDir + '/' + fileName, 'w')
        outputFile.write(dirStr)
        self.window.open_file(outputDir + '/' + fileName)

    def is_visible(self, dirs):
        return len(dirs) == 1 and dirs[0].endswith('directive')

class AchillesSideBarAddNgFactoryCommand(AchillesSideBarBase, sublime_plugin.WindowCommand):

    def get_input_panel_caption(self):
        return 'Enter a name for the ngFactory'

    def get_template_file_name(self):
        return 'NgFactory.js'

    def run(self, dirs):
        self.show_input_panel(dirs)

    def handle_template(self, tplStr, outputDir, input_string, fileName):
        name = input_string[0].upper() + input_string[1:]
        fileName = fileName[0].upper() + fileName[1:]

        if isfile(outputDir + '/' + fileName):
            self.window.open_file(outputDir + '/' + fileName)
            return

        tpl = Template(tplStr)
        date = datetime.datetime.now()
        dirStr = tpl.substitute(name=name, user=getpass.getuser(), date=calendar.month_name[date.month]+' '+str(date.day)+'th, '+str(date.year))
        outputFile = open(outputDir + '/' + fileName, 'w')
        outputFile.write(dirStr)
        self.window.open_file(outputDir + '/' + fileName)

    def is_visible(self, dirs):
        return len(dirs) == 1 and dirs[0].endswith('service')

class AchillesSideBarAddNgServiceCommand(AchillesSideBarBase, sublime_plugin.WindowCommand):

    def get_input_panel_caption(self):
        return 'Enter a name for the ngService'

    def get_template_file_name(self):
        return 'NgService.js'

    def run(self, dirs):
        self.show_input_panel(dirs)

    def handle_template(self, tplStr, outputDir, input_string, fileName):
        name = input_string[0].upper() + input_string[1:]
        fileName = fileName[0].upper() + fileName[1:]

        if isfile(outputDir + '/' + fileName):
            self.window.open_file(outputDir + '/' + fileName)
            return

        tpl = Template(tplStr)
        date = datetime.datetime.now()
        dirStr = tpl.substitute(name=name, user=getpass.getuser(), date=calendar.month_name[date.month]+' '+str(date.day)+'th, '+str(date.year))
        outputFile = open(outputDir + '/' + fileName, 'w')
        outputFile.write(dirStr)
        self.window.open_file(outputDir + '/' + fileName)

    def is_visible(self, dirs):
        return len(dirs) == 1 and dirs[0].endswith('service')

class AchillesSideBarAddLangCommand(AchillesSideBarBase, sublime_plugin.WindowCommand):

    def get_input_panel_caption(self):
        return 'Enter a name for the ngLang'

    def get_template_file_name(self):
        return 'NgLang.js'

    def run(self, dirs):
        self.show_quick_panel(dirs, ['English', 'Chinese'])

    def handle_template(self, tplStr, outputDir, input_string, fileName):
        fileName = fileName[0].upper() + fileName[1:]

        if isfile(outputDir + '/' + fileName):
            self.window.open_file(outputDir + '/' + fileName)
            return

        tpl = Template(tplStr)
        date = datetime.datetime.now()
        dirStr = tpl.substitute(name=input_string, user=getpass.getuser(), date=calendar.month_name[date.month]+' '+str(date.day)+'th, '+str(date.year))
        outputFile = open(outputDir + '/' + fileName, 'w')
        outputFile.write(dirStr)
        self.window.open_file(outputDir + '/' + fileName)

    def is_visible(self, dirs):
        return len(dirs) == 1 and dirs[0].endswith('i18n')