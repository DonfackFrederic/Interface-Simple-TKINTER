from tkinter import *
from math import *
def evaluer(event):
    chaine.configure(text="resultat = " + str(eval(entree.get())))
fen=Tk()
entree=Entry(fen)
entree.bind("<Return>",evaluer)
lab=Label(fen, text="entrer une operation puis\n appuyer la touche Enter")
lab.pack()
chaine=Label(fen)
entree.pack(padx=50, pady=50)
chaine.pack()
mainloop()