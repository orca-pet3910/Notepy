# Copyright (C) 2024 Notepy
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import sys
import os
import tkinter as tk
from tkinter import Toplevel
from tkinter import StringVar
from tkinter import ttk
from tkinter import filedialog
from tkinter import font as tkfont
import gettext
import langcodes
from configparser import ConfigParser
import re
config = ConfigParser()
config.read('notepy.ini')
if os.path.isfile("notepy.ini"):
    themeclr = config.get('main', 'theme')
    lang_cfg = config.get('main', 'language')
else:
    themeclr = "dark"
    lang_cfg = "en"
    config.add_section('main')
    config.set('main', 'language', 'en')
    config.set('main', 'theme', 'dark')
    with open('notepy.ini', 'w') as f:
        config.write(f)
languages = [x[0] for x in os.walk("locales")]
print(languages)
lngs = []
for lang in languages:
    if not lang == "locales":
        try:
            if not "LC_MESSAGES" in lang:
                language = lang.replace('locales/', '')
                language = lang.replace('locales\\\\', '')
                language_list = re.findall('(?<=locales/).+', language)
                for lng in language_list:
                    lngs.append(lng)
                language_list = re.findall('(?<=locales\\\\).+', language)
                for lng in language_list:
                    lngs.append(lng)
        except:
            lngs.append(lang)
print(lngs)
if lang_cfg == "en":
    _ = gettext.gettext
elif lang_cfg in lngs:
    translt = gettext.translation('base', localedir='locales', languages=[lang_cfg])
    translt.install()
    _ = translt.gettext
print(_("Note: running this app in pyw or pythonw is more recommended than in py or python!"))
def program_version():
    bigfont = tkfont.Font(size=25, weight="bold")
    ver = Toplevel(root)
    version_label = ttk.Label(ver, text="Program version: notepy.ver(\"1.3\")\n\n")
    version_label.pack()
    madeby = ttk.Label(ver, text=_("made by orca.pet"), font=bigfont)
    madeby.pack()

def workings_help():
    top = Toplevel(root)
    label1 = ttk.Label(top, text=_("In the commands menu you will\nfind \"New\", \"Open\", \"Save\" and \"Exit\".\nWhat these actually do is:\n\"New\" basically makes a new empty file;\n\"Open\" opens another file WITHOUT saving it,\n\"Save\" writes data you wrote and\n\"Exit\" exits ALSO WITHOUT saving contents."))
    label1.pack()

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(parent=root, filetypes=[(_("Normal text files"), "*.txt"), (_("Python files"), "*.py"), (_("No console python files"), "*.pyw")])  # This gets the file path
    if file_path:
        with open(file_path, mode='r', encoding='utf-8', errors='replace') as file:
            content = file.read()
            text_area.insert(1.0, content)
    if not file_path == "":
        root.title(f"Notepy - {file_path}")
    else:
        pass

def save_file():
    file_path = filedialog.asksaveasfilename(parent=root, filetypes=[(_("Normal text files"), "*.txt"), (_("Python files"), "*.py"), (_("No console python files"), "*.pyw")])  # This gets the file path
    if file_path:
        with open(file_path, mode='w', encoding='utf-8', errors='replace') as file:
            data = text_area.get(1.0, tk.END)
            file.write(data)
if getattr(sys, 'frozen', False):
    # The application is frozen
    bundle_dir = sys._MEIPASS
else:
    # The application is not frozen
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

# Use the bundled icon path
icon_path = os.path.join(bundle_dir, 'fileicon.ico')
root = tk.Tk()
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", themeclr)
root.title(_("Notepy - untitled"))
try:
	root.iconbitmap('fileicon.ico')
except:
	pass
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
help_menu = tk.Menu(menu)
vers_menu = tk.Menu(menu)
def change_theme():
    if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
        root.tk.call("set_theme", "light")
        config.set('main', 'theme', 'light')
        with open('notepy.ini', 'w') as f:
            config.write(f)
    else:
        root.tk.call("set_theme", "dark")
        config.set('main', 'theme', 'dark')
        with open('notepy.ini', 'w') as f:
            config.write(f)
def language_switch():
    global _
    global translt
    chooser = Toplevel(root)
    chooser.title(_("Choose a language"))
    chooser.geometry("200x100")
    choices = ['English']
    for lang in lngs:
        choices.append(langcodes.Language.make(language=lang).display_name())
    variable = StringVar(chooser)
    def save():
        lang = dialog.get()
        print(lang)
        langcode = langcodes.find(lang)
        print(langcode)
        config.set('main', 'language', str(langcode))
        with open('notepy.ini', 'w') as f:
            config.write(f)
        chooser.destroy()
        chooser.update()
    dialog = ttk.Combobox(chooser, values = choices)
    btn = ttk.Button(chooser, text=_('Save'), command=save)
    dialog.pack()
    btn.pack()
menu.add_cascade(label=_("File"), menu=file_menu)

file_menu.add_command(label=_("New"), command=new_file)
file_menu.add_command(label=_("Open"), command=open_file)
file_menu.add_command(label=_("Save"), command=save_file)
file_menu.add_command(label=_("Switch theme color"), command=change_theme)
file_menu.add_command(label=_("Switch language"), command=language_switch)
file_menu.add_separator()
file_menu.add_command(label=_("Exit"), command=root.quit)

menu.add_cascade(label=_("Help"), menu=help_menu)

help_menu.add_command(label=_("Help"), command=workings_help)
help_menu.add_separator()
help_menu.add_command(label=_("About Notepy..."), command=program_version)

text_area = tk.Text(root)
text_area.pack(fill=tk.BOTH, expand=1)

root.mainloop()
