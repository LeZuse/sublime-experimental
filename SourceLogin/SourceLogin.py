# -*- coding: utf-8 -*-

import sublime
import sublime_plugin

settings = sublime.load_settings('source')
class SourceLoginCommand(sublime_plugin.WindowCommand):
    def is_enabled(self):
        return not settings.get('logged', False)

    def run(self):
        sublime.active_window().show_input_panel('Source login:', '', self.on_login, None, None)

    def on_login(self, login):
        settings.set('login', login)
        sublime.active_window().show_input_panel('Password for %s:' % login, '', self.on_proceed, None, None)
        pass

    def on_proceed(self, password):
        settings.set('logged', True)
        # sublime.message_dialog('Authenticated')
        sublime.status_message('Logged in Source as ' + settings.get('login'))
        pass

class SourceLogoutCommand(sublime_plugin.WindowCommand):
    def is_enabled(self):
        return settings.get('logged', False)

    def run(self):
        settings.set('logged', False)
        sublime.status_message('Logged out of Source')
