import sys
import os
import tkinter as tk
from tkinter import Toplevel
from tkinter import filedialog
from tkinter import font as tkfont

print("Note: running this app in pyw or pythonw is more recommended than in py or python!")

def program_version():
    bigfont = tkfont.Font(size=25, weight="bold")
    ver = Toplevel(root)
    version_label = tk.Label(ver, text="Program version: notepy.ver(\"1.3\")\n\n")
    version_label.pack()
    madeby = tk.Label(ver, text="made by orca.pet", font=bigfont)
    madeby.pack()

def workings_help():
    top = Toplevel(root)
    label1 = tk.Label(top, text="In the commands menu you will\nfind \"New\", \"Open\", \"Save\" and \"Exit\".\nWhat these actually do is:\n\"New\" basically makes a new empty file;\n\"Open\" opens another file WITHOUT saving it,\n\"Save\" writes data you wrote and\n\"Exit\" exits ALSO WITHOUT saving contents.")
    label1.pack()

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(parent=root, filetypes=[("Normal text files", "*.txt"), ("Python files", "*.py"), ("No console python files", "*.pyw")])  # This gets the file path
    if file_path:
        with open(file_path, mode='r', encoding='utf-8', errors='replace') as file:
            content = file.read()
            text_area.insert(1.0, content)
    root.title(f"Notepy - {file_path}")
    if file_path == "":
        root.title("Notepy - untitled")

def save_file():
    file_path = filedialog.asksaveasfilename(parent=root, filetypes=[("Normal text files", "*.txt"), ("Python files", "*.py"), ("No console python files", "*.pyw")])  # This gets the file path
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
root.title("Notepy - untitled")
root.iconbitmap('%~dp0\fileicon.ico')
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
help_menu = tk.Menu(menu)
vers_menu = tk.Menu(menu)

menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="Help", menu=help_menu)

help_menu.add_command(label="Help", command=workings_help)
help_menu.add_separator()
help_menu.add_command(label="About Notepy...", command=program_version)

text_area = tk.Text(root)
text_area.pack(fill=tk.BOTH, expand=1)

root.mainloop()