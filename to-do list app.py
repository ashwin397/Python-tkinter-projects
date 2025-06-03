import tkinter as tk
from tkinter import *
def todo():
    task = tk.Entry.get(input)
    checkbox = tk.Checkbutton(screen, text=task, bg="#ffffff")
    checkbox.pack(pady=10)
screen = tk.Tk()
screen.config(bg="#ffffff")
heading = tk.Label(screen, text="to-do task manager", bg="#ffffff")
heading.pack()
input = tk.Entry(screen)
input.pack()
button = tk.Button(screen, text="create task", command=todo, bg="#ffffff")
button.pack()
screen.mainloop()