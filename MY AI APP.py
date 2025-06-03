import tkinter as tk
from tkinter  import *
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def result():
    i = tk.Entry.get(age)
    j = tk.Entry.get(gender)
    music_preference = {'age' : [2, 2, 10, 10, 30, 30, 40, 40], 'gender' : [1, 0, 1, 0, 1, 0, 1, 0], 'genre' : ['nothing', 'nothing', 'pop music', 'piano', 'guitar', 'dance', 'classical music', 'voilin']}
    hf = pd.DataFrame(music_preference)
    x = hf.drop(columns=['genre'])
    y = hf['genre']
    myai = DecisionTreeClassifier()
    myai.fit(x.values, y)
    prediction = myai.predict([ [i, j] ])
    hj = tk.Label(root, text=prediction)
    hj.pack()

root = tk.Tk()
tk.Label(root, text="MY AI").pack()
tk.Label(root, text="this app will predict your musical interests based on data").pack()
tk.Label(root, text="enter your age").pack()
age = tk.Entry(root)
age.pack()
tk.Label(root, text="enter your gender").pack()
gender = tk.Entry(root)
gender.pack()
button = tk.Button(root, text="submit", command=result)
button.pack()
root.mainloop()