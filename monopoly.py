from tkinter import *
from PIL import ImageTk, Image
import random

# root window, not resizable
root =  Tk()
root.geometry("900x600+200+200")
root.resizable(False, False)

#slika ploce
framePloce = Frame(root, width=600, height=600)
framePloce.pack()
framePloce.place(anchor='nw', relx=0, rely=0)
ploca = ImageTk.PhotoImage(Image.open("ploca.png"))
label = Label(framePloce, image=ploca)
label.pack()

#buttoni za playere
p1Button = Button(root)
p1Button.config(text="1", font=("Calibri", 16)) #ide image= za sliku
p2Button = Button(root)
p2Button.config(text="2", font=("Calibri", 16))
p3Button = Button(root)
p3Button.config(text="3", font=("Calibri", 16))
p4Button = Button(root)
p4Button.config(text="4", font=("Calibri", 16))

p1Button.place(x=610, y=10)
p2Button.place(x=690, y=10)
p3Button.place(x=770, y=10)
p4Button.place(x=850, y=10)


#pokazi profile ljudi
def showPlayerStats(igrac):
    frameStats = Frame(root, width=250, height=300)
    frameStats.pack()
    frameStats.place(anchor='center', relx=0.83, rely=0.25)
    stats = "Pare: " + str(igrac["pare"]) + "\nVlasnistvo: " + str(igrac["vlasnistvo"])
    labelStats = Label(frameStats, text=stats, font=("Calibri", 16))
    labelStats.pack()
    
#pokazi rezultat kocke
def showDice(diceNumber1, diceNumber2):
    
    

#kocke duh
def kocke(igrac):
    diceNumber1 = random.randint(1,6)
    diceNumber2 = random.randint(1,6)
    igrac["polje"] += (diceNumber1 + diceNumber2)
    if (igrac["polje"] >= 40):
        igrac["polje"] == 0
        igrac["pare"] += 200
    showDice(diceNumber1, diceNumber2)
    

#igraci i pocetno stanje
p1 = {"polje":0,"pare":1500,"vlasnistvo":[],"u_zatvoru":False,"bankrot":False}
p2 = {"polje":0,"pare":1500,"vlasnistvo":[],"u_zatvoru":False,"bankrot":False}
p3 = {"polje":0,"pare":1500,"vlasnistvo":[],"u_zatvoru":False,"bankrot":False}
p4 = {"polje":0,"pare":1500,"vlasnistvo":[],"u_zatvoru":False,"bankrot":False}

showPlayerStats(p2)
mainloop()
