import os.path
import subprocess
import tkinter as tk

from PIL import ImageTk, Image

import gui


def execute_file():
    subprocess.Popen(['C:\\Users\\HannesAdminBackUp\\AppData\\Local\\Microsoft\\WindowsApps\\python3.10.exe', 'main.py'])


#window = tk.Tk()
window = tk.Toplevel()
window.title("Execute File")
window.attributes("-fullscreen", True)

logo_image = Image.open(os.path.join('images', 'start.png'))
#gui.resize(logo_image, 30, 30)  # Resize the image as needed
logo_image = ImageTk.PhotoImage(logo_image)


# Button
button = tk.Button(window, text="Start", image=logo_image, command=execute_file, height=200, width=200, anchor="center")
button.pack(pady=100, padx=100)


# tkinter main
window.mainloop()
