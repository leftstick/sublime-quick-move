import sublime, sublime_plugin
from .use.Generator import Generator
from .use.SettingsManager import SettingsManager
from string import Template
import getpass
import datetime
import calendar
from os.path import isfile
from os.path import isdir
from os import makedirs
import os

class AchillesSideBarAddNgCtrlCommand(Generator, SettingsManager, sublime_plugin.WindowCommand):

    def get_input_panel_caption(self):
        return 'Enter a name for the ngController'

    def get_template_file_name(self):
        return 'NgController.js'

    def get_file_extension(self):
        return '.js'

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
            
class AchillesSideBarAddNgDirCommand(Generator, SettingsManager, sublime_plugin.WindowCommand):

    def get_input_panel_caption(self):
        return 'Enter a name for the ngDirective'

    def get_template_file_name(self):
        return 'NgDirective.js'

    def get_file_extension(self):
        return '.js'

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
        if self.isStrictMode():
            return len(dirs) == 1 and dirs[0].endswith('directive')
        else:
            return True

class AchillesSideBarAddNgFactoryCommand(Generator, SettingsManager, sublime_plugin.WindowCommand):

    def get_input_panel_caption(self):
        return 'Enter a name for the ngFactory'

    def get_template_file_name(self):
        return 'NgFactory.js'

    def get_file_extension(self):
        return '.js'

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
        if self.isStrictMode():
            return len(dirs) == 1 and dirs[0].endswith('service')
        else:
            return True

class AchillesSideBarAddNgServiceCommand(Generator, SettingsManager, sublime_plugin.WindowCommand):

    def get_input_panel_caption(self):
        return 'Enter a name for the ngService'

    def get_template_file_name(self):
        return 'NgService.js'

    def get_file_extension(self):
        return '.js'

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
        if self.isStrictMode():
            return len(dirs) == 1 and dirs[0].endswith('service')
        else:
            return True

class AchillesSideBarAddLangCommand(Generator, SettingsManager, sublime_plugin.WindowCommand):

    def get_input_panel_caption(self):
        return 'Enter a name for the ngLang'

    def get_template_file_name(self):
        return 'NgLang.js'

    def get_file_extension(self):
        return '.js'

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
        if self.isStrictMode():
            return len(dirs) == 1 and dirs[0].endswith('i18n')
        else:
            return True


class AchillesSideBarAddProjectCommand(Generator, SettingsManager, sublime_plugin.WindowCommand):

    def get_input_panel_caption(self):
        return 'Enter a name for the project'

    def get_template_type(self):
        return 'project'

    def handle_structure(self, outputDir, input_string, templatePath):
        for dirpath, dirnames, filenames in os.walk(templatePath):
            extraPath = dirpath[(len(templatePath)):]

            self.emptyFolderOut(outputDir, extraPath, filenames)

            for name in filenames:
                self.templateOut(input_string, outputDir, extraPath, dirpath, name)

    def templateOut(self, input_string, outputDir, extraPath, templateFullPath, fileName):
        input = open(templateFullPath + '/' + fileName, mode='r', encoding='utf-8')
        tpl = Template(input.read())
        date = datetime.datetime.now()
        dirStr = tpl.substitute(project=input_string, user=getpass.getuser(), date=calendar.month_name[date.month]+' '+str(date.day)+'th, '+str(date.year))

        if not isdir(outputDir + '/' + extraPath):
            makedirs(outputDir + '/' + extraPath)
        
        if fileName.startswith('.'):
            return
        outputFile = open(outputDir + '/' + extraPath +'/' + fileName, mode='w', encoding='utf-8')
        outputFile.write(dirStr)

    def emptyFolderOut(self, outputDir, extraPath, filenames):
        if len(filenames) > 0:
            return

        if not isdir(outputDir + '/' + extraPath):
            makedirs(outputDir + '/' + extraPath)

    def run(self, dirs):
        self.show_structure_input_panel(dirs)

    
    def is_visible(self, dirs):
        if self.isStrictMode():
            return len(dirs) == 1 and dirs[0].endswith('business')
        else:
            return True