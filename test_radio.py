from tkinter import *

fen=Tk()

def colorer():
    val=fruit.get()
    if val == "cerise":
        lab['bg']="red"
    if val == "banane":
        lab['bg']="yellow"
    if val == "orange":
        lab['bg']="orange"
fruit=StringVar()
fruit.set("cerise")

cerise = Radiobutton(fen, text="Cerise", variable=fruit, value="cerise")
cerise.pack(anchor=W, padx=20, pady=20)

banane = Radiobutton(fen, text="Banane", variable=fruit, value="banane")
banane.pack(anchor=W, padx=20, pady=20)

orange = Radiobutton(fen , text="Orange", variable=fruit, value="orange")
orange.pack(anchor=W, padx=20, pady=20)

lab=Label(fen, width=10, height=5)
lab.pack(anchor=W, padx=10, pady=10)

bout=Button(fen, text="colorer", command=colorer)
bout.pack(anchor=W, pady=20, padx=20)
fen.mainloop()