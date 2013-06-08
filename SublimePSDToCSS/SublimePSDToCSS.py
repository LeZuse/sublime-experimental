
import sublime
import sublime_plugin

import os, re

class SublimePSDToCSS(sublime_plugin.EventListener):
    def on_load(self, view):
        ext =  os.path.basename(view.file_name().split('.')[-1])
        if not re.match('\.psd', ext, flags=re.IGNORECASE):
            return

        # Do the magic
        css = """#header {
    color: red;
    border: 5px;
}
"""
        # Display CSS
        # NOTE: close command not working?
        e = view.begin_edit()
        # Delete contents
        view.run_command('select_all')
        view.run_command('left_delete')
        # Insert css
        view.insert(e, 0, css)
        view.end_edit(e)
        # Syntax highilght
        view.set_syntax_file('Packages/CSS/CSS.tmLanguage')
        # Do not show unsaved changes
        view.set_scratch(True)
