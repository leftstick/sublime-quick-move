import sublime

class SettingsManager():

    def isStrictMode(self):
        settings = sublime.load_settings('Preferences.sublime-settings')
        if settings.has('strict_mode'):
            return settings.get('strict_mode')
        settings = sublime.load_settings('Sublime3-Achilles.sublime-settings')
        return settings.get('strict_mode', True)
