# -*- coding: utf-8 -*-

import sublime
import sublime_plugin

class RealtimeSaving(sublime_plugin.EventListener):
    def on_modified(self, view):
        view.run_command('save')
        # sublime.status_message("File autosaved")
