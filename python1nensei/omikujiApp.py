import tkinter as tk
import random

def dispLabel():
    kuji = ['大吉','中吉','小吉','凶']
    lbl.configu

    re(text = random.choice(kuji))

root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text = "LABEL")
btn = tk.Button(text = "PUSH",command = dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()
