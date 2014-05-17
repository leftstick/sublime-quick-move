import sublime
from os.path import dirname, realpath
from os.path import isdir
from os import makedirs

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

    def handle_structure(self, outputDir, input_string, templatePath):
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
                self.clear()
                return
            if not input_string.strip():
                self.clear()
                return
            dirName = input_string.strip()
            dirPath = outputDir + '/' + dirName

            if isdir(dirPath):
                self.clear()
                return
            
            makedirs(dirPath)

            templatePath = sublime.packages_path() + '/Sublime3-Achilles' + '/templates/' + templateType

            handle_structure(dirPath, dirName, templatePath)

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
            