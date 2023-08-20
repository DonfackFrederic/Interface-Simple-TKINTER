from tkinter import *

fen=Tk()
can=Canvas(fen, height=400, width=400, bg='lightyellow')
can.pack()

def rouge():
    can['bg']="red"
def violet():
    can['bg']="purple"
def bleu():
    can["bg"]="blue"
def orange():
    can["bg"]="orange"
mon_menu=Menu(fen)
fen.config(menu=mon_menu)

legumes = Menu(mon_menu, tearoff=0)
legumes.add_command(label="Radis", command=bleu)
legumes.add_separator()
legumes.add_command(label="Tomate", command=rouge)
mon_menu.add_cascade(label="Légumes", menu=legumes)

fruits = Menu(mon_menu, tearoff=0)
fruits.add_command(label="Raisin", command=violet)
fruits.add_separator()
fruits.add_command(label="Orange", command=orange)
mon_menu.add_cascade(label="fruits",menu=fruits)

fen.mainloop()