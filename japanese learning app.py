#japanese learning app created by ashwin tiwary



#importing modules
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

#about info
def About_info():
    root = tk.Tk()
    root.title("About info")
    tk.Label(root, text="DEVELOPER ASHWIN TIWARY").pack(pady=10)
    tk.Label(root, text="after struggle of several days we have came up").pack()
    tk.Label(root, text="with this app.Because of lack of team support").pack()
    tk.Label(root, text="we haven't covered every topic but you'll come").pack()
    tk.Label(root, text="up with an idea of japanese.").pack()
    tk.Label(root, text="best of luck :)").pack(pady=10)
    root.mainloop


#learning words
def learn_words():
    root = tk.Tk()
    root.title("learn words")
    tk.Label(root, text="english to japanese").pack(pady = 20)
    tk.Label(root, text="hello = konńichiwa").pack()
    tk.Label(root, text="bye = sayonara").pack()
    tk.Label(root, text="me = jibun").pack()
    tk.Label(root, text="you = anata").pack()
    tk.Label(root, text="he = kare").pack()
    tk.Label(root, text="she = kanojo").pack()
    tk.Label(root, text="they = karera wa").pack()
    tk.Label(root, text="them = karera").pack()
    tk.Label(root, text="we = watashitachiha").pack()
    tk.Label(root, text="i am = watashi wa").pack()
    tk.Label(root, text="i = watashi").pack()
    tk.Label(root, text="eat = taberu").pack()
    tk.Label(root, text="drink = nomu").pack()
    tk.Label(root, text="drinking = inshu").pack()
    tk.Label(root, text="people = hitobito").pack()
    tk.Label(root, text="ocean = umi").pack()
    tk.Label(root, text="food = tabemoro").pack()
    tk.Label(root, text="japanese = nihongo").pack()
    tk.Label(root, text="english = eigo").pack()
    tk.Label(root, text="speak = hanasu").pack()
    tk.Label(root, text="speaking = hanashuchū").pack()
    tk.Label(root, text="tea = ocha").pack()
    tk.Label(root, text="rice = gohan").pack()
    tk.Label(root, text="bread = pan").pack()
    tk.Label(root, text="curry = karī").pack()
    tk.Label(root, text="vegetable = yasaí").pack()
    tk.Label(root, text="meat = niku").pack()
    tk.Label(root, text="water = mizu").pack()
    tk.Label(root, text="milk = gyūnyū").pack()
    tk.Label(root, text="pudding = puzù").pack()
    root.mainloop()


#learning conversation
def learn_convo():
    root = tk.Tk()
    root.title("learn conversation")
    tk.Label(root, text="english to japanese").pack()
    tk.Label(root, text="").pack(pady=10)
    tk.Label(root, text="hello how are you?").pack()
    tk.Label(root, text="Końnichiwa ogenkidesuka?").pack()
    tk.Label(root, text="").pack()
    tk.Label(root, text="do you speak english?").pack()
    tk.Label(root, text="anatawa eigo o hanashimasu ka?").pack()
    tk.Label(root, text="").pack()
    tk.Label(root, text="i wanna eat").pack()
    tk.Label(root, text="tabetaidesu").pack()
    tk.Label(root, text="").pack()
    tk.Label(root, text="i speak japanese").pack()
    tk.Label(root, text="watashi wa nihongo o hanashimasu").pack()
    tk.Label(root, text="").pack()
    tk.Label(root, text="what are you doing?").pack()
    tk.Label(root, text="nanishiteruno?").pack()
    tk.Label(root, text="").pack()
    tk.Label(root, text="now you can make your own sentences YAY!!").pack()
    
    root.mainloop



#learning hirangana
def hirangana():
    root = tk.Tk()
    root.title("learn hirangana")
    tk.Label(root, text="learn hirangana").pack(pady=10)
    tk.Label(root, text="あa, いi, うu,  おo, えe").pack()
    tk.Label(root, text="かka, きki, くku, こko, けke").pack()
    tk.Label(root, text="さsa, しsi, すsu, そso, せse").pack()
    tk.Label(root, text="たta, ちti, つtu, とto, てte").pack()
    tk.Label(root, text="なna, にni, ぬnu, のno, ねne").pack()
    tk.Label(root, text="まma, みmi, むmu, もmo, めme").pack()
    tk.Label(root, text="alert:-there are some missing letters").pack(pady=10)
    root.mainloop



#thanking for feedback
def Feedback():
    feedback3 = tk.messagebox.showinfo(title="thanks", message="thanks for your feedback :D")


#creating main window
mainscreen = tk.Tk()
mainscreen.title("japanese learning app")
mainscreen.config(bg="#6100b3")


#creating headings
heading = tk.Label(mainscreen, text="LEARN JAPANESE", fg="#ffffff", bg="#6100b3")
heading.pack(pady=100)


#creating buttons
about = tk.Button(mainscreen, text="About", command=About_info)
about.pack(pady=10)
words = tk.Button(mainscreen, text="learn japanese words", command=learn_words)
words.pack(pady=10)
convo = tk.Button(mainscreen, text="learn conversation", command=learn_convo)
convo.pack(pady=10)
hirangana = tk.Button(mainscreen, text="hirangana", command=hirangana)
hirangana.pack(pady=10)


#feedback asking
feedback = tk.Label(mainscreen, text="enter your feedback :)", fg="#ffffff", bg="#6100b3")
feedback.pack(pady=100)
feedback2 = tk.Entry()
feedback2.pack()
i = tk.Button(mainscreen, text="submit", command=Feedback)
i.pack(pady = 5)

mainscreen.mainloop()
#the end:)