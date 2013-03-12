#!/usr/bin/python
__authors__ = ["kurian.os"]
__version__ = '$Revision: 71504 $'.split()[1]
__revision__ = __version__ # For pylint
__date__ = '$Date:  July 5, 2012 12:00:00 PM$'.split()[1]
__copyright__ = '2011'
__license__ = "Copyright 2011 Kurian"
__contact__ = "kurianos@gmail.com"
__status__ = "Development"
#this code is based on Eric Martel stackoverflow search
import sublime
import sublime_plugin

import subprocess
import webbrowser

def SearchFor(text):
    url = 'http://pyqt.sourceforge.net/Docs/PyQt4/%s.html'%text.lower()
    webbrowser.open_new_tab(url)

class RiverbankSearchCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            if selection.empty():
                text = self.view.word(selection)
            text = self.view.substr(selection)
            SearchFor(text)
