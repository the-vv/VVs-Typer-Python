import sys
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

try:
    import pyautogui
except ModuleNotFoundError:
    print('use \'pip install pyautogui\' for installing library, then restart')
    input()
    sys.exit()

def write():
    pyautogui.click(x=500, y=500)
    global text
    pyautogui.write(text)

text = ''
win = tk.Tk()  # Application Name
win.resizable(False, False)
win.title("VVs Typer")  # Label
lbl = tk.ttk.Label(win, text="Enter the Text (make sure Notepad window is opened behind this window and is fullscreen)").grid(
    column=0, row=0)  # Click event

text = ScrolledText(win)
text.grid(
    column=0, row=1)

def submit():
    # print("Hi," + text.get("1.0",tk.END))
    global text
    text = text.get("1.0",tk.END)
    win.quit()
    messagebox.showinfo(title='Ready', message='Open your notepad behind this window and maximize it before starting.')
    win.destroy()
    write()


name = tk.StringVar()
button = tk.ttk.Button(win, text="submit", command=submit).grid(column=0, row=2,)
win.mainloop()