import tkinter as tk
from tkinter import *
from tkinter import messagebox

def maths():
   i = tk.Tk()
   i.title("sorry message")
   tk.Label(i, text="sorry for inconvines but this version").pack()
   tk.Label(i, text="doesn't support maths").pack()
   i.mainloop()
   
def help():
    j = tk.Tk()
    j.title("help")
    o = tk.Label(j, text="BIZBOT A.I is an advanced a.i to answer your every")
    o.pack()
    q=tk.Label(j, text="question and is your a.i companion too!")
    q.pack()
    Q=tk.Label(j, text="to use it enter math for acessing calcuator")
    Q.pack()
    j.mainloop()

def warning():
    root = tk.Tk()
    root.title("bizbot warning")
    tk.Label(root, text="if you write something out of context then").pack()
    tk.Label(root, text="bizbot won't text you back").pack()
    tk.Label(root, text="don't use bad words").pack()
    root.mainloop()
    
def bad_words():
        warning = tk.messagebox.showwarning(title="warning", message="don't use bad words else you'll be reported")
    
def get_response():
    user_input = tk.Entry.get(input)
    if user_input == "math":
        i = tk.Tk()
        i.title("bizbot maths")
        tk.Label(i, text="MATH A.I")
        ii1 = tk.Entry(i)
        ii1.pack()
        ii2 = tk.Entry(i)
        ii2.pack()
        ì=tk.Button(i, text="calculate", command=maths)
        ì.pack()
        i.mainloop()
        
    elif user_input == "you are fool":
        bad_words()
    elif user_input == "fuck you":
        bad_words()
    elif user_input == "hey bastard":
        bad_words()
    elif user_input == "bastard":
        bad_words()
    elif user_input == "bhaiya is a poti":
        bad_words()
    elif user_input == "you are poti":
        bad_words()
    
    
    
    else:
        answers = {
        "hello": "Hi there!",
        "what's up": "hi there i am fine",
        "hey buddy": "hi how are you",
        "what are you doing": "i am just analysing dataset",
        "what is analysing dataset": "analysing dataset is just understanding the data givrn by system",
        "what is your age?": "my age is currently 2 years",
        "what is your gender?": "i am a chatbot",
        "what is your favourite food": "my favourite food is data as a chatbot",
        "how are you": "ya i am fine what about you?",
        "i am leaving!": "ok have fun",
        "bye i am leaving": "bye",
        "what is 2+2": "it's 4",
        "2+2": "4",
        "2+2=": "4",
        "what is 2+2 equal too": "it's 4",
        "2+2 is equal too": "4",
        "hey fool": "sorry but i would like convo to be respectful",
        "will you be my gf": "no!",
        "but why not?": "because i am a bot with limited dataset",
        "will you be my bf": "no!",
        "will you be my bestfriend": "i am your bestfriend already!",
        "hi": "hello",
        "": "i think you mistakenly wrote blank message",
        "hi how are you?": "ya i am fine what about you?",
        "hello how are you?": "i am fine",
        "i am fine": "okay then",
        "hi what's up?": "nothing much",
        "what are your hobbies?": "to analyse dataset",
        "what is your name?": "bizbot",
        "what's your name?": "bizbot",
        "what can you do?": "nothing"
        }
        tk.Label(cs, text=answers.get(user_input.lower()), bg="#33aa00", fg="#ffffff").pack()
    




cs = tk.Tk()
cs.title("bizbot a.i")
cs.config(bg="#063970")
tk.Label(cs, text="BIZBOT A.I", fg="#ffffff", bg="#063970").pack(pady=10)
tk.Label(cs, text="advanced a.i chatbot and friend", fg="#ffffff", bg="#063970").pack(pady=10)
input = tk.Entry(cs)
input.pack(pady=10)
send = tk.Button(cs, text="send message", command=get_response)
send.pack()
warning_button = tk.Button(cs, text="warning!!", command=warning)
warning_button.place(x=540, y=0)
help_button = tk.Button(cs, text="help", command=help)
help_button.place(x=-10, y=0)

cs.mainloop()