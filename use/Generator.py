import sublime
from os.path import dirname, realpath
from os.path import isdir
from os import makedirs
import os

class Generator():

    def get_input_panel_caption(self):
        return ''

    def get_template_file_name(self):
        return ''

    def get_file_extension(self):
        return ''

    def get_template_type(self):
        return ''

    def show_input_panel(self, dirs):
        outputDir = dirs[0]
        self.input_panel_view = self.window.show_input_panel(
            self.get_input_panel_caption(), "",
            self.get_input_on_done(outputDir, self.handle_template, self.get_file_extension()), self.__update_filename_input, self.clear
        )

    def show_structure_input_panel(self, dirs):
        outputDir = dirs[0]
        self.input_panel_view = self.window.show_input_panel(
            self.get_input_panel_caption(), "",
            self.get_structure_input_on_done(outputDir, self.handle_structure, self.get_template_type()), self.__update_filename_input, self.clear
        )

    def show_quick_panel(self, dirs, items):
        outputDir = dirs[0]
        self.input_panel_view = self.window.show_quick_panel(items,
            self.get_select_on_done(outputDir, items, self.handle_template))

    def handle_template(self, tplStr, outputDir, input_string, fileName):
        self.clear()

    def handle_structure(self, tpl, input_string):
        self.clear()

    def get_input_on_done(self, outputDir, handle_template, extension):

        def on_done(input_string):
            if not input_string:
                self.clear()
                return
            if not input_string.strip():
                self.clear()
                return
            fileName = input_string.strip()
            if not input_string.endswith(extension):
                fileName = fileName + extension

            input = open(sublime.packages_path() + '/Sublime3-Achilles' + '/templates/' + self.get_template_file_name(), "r")
            handle_template(input.read(), outputDir, input_string.strip(), fileName)
            self.clear()

        return on_done

    def get_structure_input_on_done(self, outputDir, handle_structure, templateType):

        def on_done(input_string):
            if not input_string:
                return
            if not input_string.strip():
                return
            outDirName = input_string.strip()
            outDirPath = outputDir + '/' + outDirName

            if isdir(outDirPath):
                return
            
            makedirs(outDirPath)

            templatePath = sublime.packages_path() + '/Sublime3-Achilles' + '/templates/' + templateType

            for dirpath, dirnames, filenames in os.walk(templatePath):
                extraPath = dirpath[(len(templatePath)):]

                for name in filenames:
                    if not isdir(outDirPath + '/' + extraPath):
                        makedirs(outDirPath + '/' + extraPath)
                    
                    if name.startswith('.'):
                        continue

                    input = open(dirpath + '/' + name, mode='r', encoding='utf-8')
                    tplStr = input.read()
                    
                    dirStr = handle_structure(tplStr, outDirName)

                    outputFile = open(outDirPath + '/' + extraPath +'/' + name, mode='w', encoding='utf-8')
                    outputFile.write(dirStr)

        return on_done

    def __update_filename_input(self, path_in):
        new_content = path_in

    def get_select_on_done(self, outputDir, items, handle_template):

        def on_done(index):
            if index == -1:
                return
            item = items[index]
            if item == 'English':
                fileName = 'lang_en.js'
            else:
                fileName = 'lang_zh.js'
            
            input = open(sublime.packages_path() + '/Sublime3-Achilles' + '/templates/' + self.get_template_file_name(), "r")
            handle_template(input.read(), outputDir, item, fileName)
            self.clear()

        return on_done

    def clear(self):
        print("end")

    def is_visible(self, dirs):
        return True
            