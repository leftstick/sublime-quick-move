import sublime
from os.path import dirname, realpath

class AchillesSideBarBase():

    def get_input_panel_caption(self):
        return ''

    def get_template_file_name(self):
        return ''

    def show_input_panel(self, dirs):
        outputDir = dirs[0]
        self.input_panel_view = self.window.show_input_panel(
            self.get_input_panel_caption(), "",
            self.get_input_on_done(outputDir, self.handle_template), self.__update_filename_input, self.clear
        )

    def show_quick_panel(self, dirs, items):
        outputDir = dirs[0]
        self.input_panel_view = self.window.show_quick_panel(items,
            self.get_select_on_done(outputDir, items, self.handle_template))

    def handle_template(self, tplStr, outputDir, input_string, fileName):
        self.clear()

    def get_input_on_done(self, outputDir, handle_template):

        def on_done(input_string):
            if not input_string:
                self.clear()
                return
            if not input_string.strip():
                self.clear()
                return
            fileName = input_string.strip()
            if not input_string.endswith('.js'):
                fileName = fileName + '.js'
            
            input = open(dirname(realpath(__file__)) + '/templates/' + self.get_template_file_name(), "r")
            handle_template(input.read(), outputDir, input_string.strip(), fileName)
            self.clear()

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
            
            input = open(dirname(realpath(__file__)) + '/templates/' + self.get_template_file_name(), "r")
            handle_template(input.read(), outputDir, item, fileName)
            self.clear()

        return on_done

    def clear(self):
        print("end")

    def isStrictMode(self):
        settings = sublime.load_settings('Preferences.sublime-settings')
        if settings.has('strict_mode'):
            return settings.get('strict_mode')
        settings = sublime.load_settings('Sublime3-Achilles.sublime-settings')
        return settings.get('strict_mode', True)

    def is_visible(self, dirs):
        return True
            