from tkinter import *

mlist=["football","basketball","tenis"]*5
color=["green","orange3","gray"]*5
n=len(mlist)
fen=Tk()
lbox=Listbox(fen, width=10, height=5, selectbackground="purple", background="blue",font="verdana 10 bold")
lbox.pack(padx=20, pady=20, side=LEFT)
lbox.focus_set()

for item in mlist:
    lbox.insert(END,item)
#associer chaque choix de la listebox a une fonction lorsuqu'on clique dessus
def show(event) :
    index=lbox.curselection()[0]
    can['bg']=color[index]
can=Canvas(fen,height=50,width=50,bg="lightyellow" )
can.pack(padx=20, pady=20,side=RIGHT)
lbox.bind('<<ListboxSelect>>', show)
#inserer une scroll bar sur la list box(barre de defilement)
sbar=Scrollbar(fen,command=lbox.yview )
sbar.pack(side=LEFT, expand=True, fill=Y)
lbox.config(yscrollcommand=sbar.set)

fen.mainloop()