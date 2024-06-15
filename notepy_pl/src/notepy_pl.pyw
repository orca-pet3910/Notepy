import sys
import os
import tkinter as tk
from tkinter import Toplevel
from tkinter import filedialog
from tkinter import font as tkfont

print("Uruchamianie tej aplikacji jest zalecane poprzez pythonw lub pyw bardziej niż w python lub py!")

def program_version():
    bigfont = tkfont.Font(size=25, weight="bold")
    ver = Toplevel(root)
    version_label = tk.Label(ver, text="Wersja: 1.4\n\n")
    version_label.pack()
    madeby = tk.Label(ver, text="stworzone przez orca.pet", font=bigfont)
    madeby.pack()

def workings_help():
    top = Toplevel(root)
    label1 = tk.Label(top, text="Opcja 'nowy' tworzy nowy plik bez zapisywania,\nopcja 'zapisz' zapisuje plik, opcja 'otwórz' otwiera plik bez zapisywania poprzedniego pliku")
    label1.pack()

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(parent=root, filetypes=[("Dokument tekstowy nieformatowany", "*.txt"), ("Plik Python", "*.py"), ("Plik Python bez konsoli", "*.pyw")])  # This gets the file path
    if file_path:
        with open(file_path, mode='r', encoding='utf-8', errors='replace') as file:
            content = file.read()
            text_area.insert(1.0, content)
    if not file_path == "":
        root.title(f"Notepy - {file_path}")
    else:
        pass

def save_file():
    file_path = filedialog.asksaveasfilename(parent=root, filetypes=[("Dokument tekstowy nieformatowany", "*.txt"), ("Plik Python", "*.py"), ("Plik Python bez konsoli", "*.pyw")])  # This gets the file path
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
root.title("Notepy - bez tytułu")
root.iconbitmap('fileicon.ico')
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
help_menu = tk.Menu(menu)
vers_menu = tk.Menu(menu)

menu.add_cascade(label="Plik", menu=file_menu)

file_menu.add_command(label="Nowy", command=new_file)
file_menu.add_command(label="Otwórz", command=open_file)
file_menu.add_command(label="Zapisz", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Wyjdź", command=root.quit)

menu.add_cascade(label="Pomoc", menu=help_menu)

help_menu.add_command(label="Pomoc", command=workings_help)
help_menu.add_separator()
help_menu.add_command(label="O Notepy...", command=program_version)

text_area = tk.Text(root)
text_area.pack(fill=tk.BOTH, expand=1)

root.mainloop()