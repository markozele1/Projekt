from tkinter import *
from PIL import ImageTk, Image
import random
from zemlje import *

#* root window, not resizable
root =  Tk()
root.geometry("900x600+200+200")
root.resizable(False, False)

#*igraci i pocetno stanje
p1 = {"polje":0,"pare":1500,"vlasnistvo":["1"],"u_zatvoru":False,"bankrot":False}
p2 = {"polje":0,"pare":1500,"vlasnistvo":["2"],"u_zatvoru":False,"bankrot":False}
p3 = {"polje":0,"pare":1500,"vlasnistvo":["3"],"u_zatvoru":False,"bankrot":False}
p4 = {"polje":0,"pare":1500,"vlasnistvo":["4"],"u_zatvoru":False,"bankrot":False}

players = [p1,p2,p3,p4]

#*pokazi profile ljudi, svaki ima zasebnu funkciju jer jbg, bitno da radi
#TODO uljepsat ovo sranje
def showPlayerStats_1():
    frameStats = Frame(root, width = 250, height = 300)
    frameStats.pack()
    frameStats.place(anchor = 'center', relx = 0.83, rely = 0.25)
    stats = "Pare: " + str(p1["pare"]) + "\nVlasnistvo: " + str(p1["vlasnistvo"])
    labelStats = Label(frameStats, text=stats, font=("Calibri", 16))
    labelStats.pack()

def showPlayerStats_2():
    frameStats = Frame(root, width = 250, height = 300)
    frameStats.pack()
    frameStats.place(anchor = 'center', relx = 0.83, rely = 0.25)
    stats = "Pare: " + str(p2["pare"]) + "\nVlasnistvo: " + str(p2["vlasnistvo"])
    labelStats = Label(frameStats, text=stats, font=("Calibri", 16))
    labelStats.pack()

def showPlayerStats_3():
    frameStats = Frame(root, width = 250, height = 300)
    frameStats.pack()
    frameStats.place(anchor = 'center', relx = 0.83, rely = 0.25)
    stats = "Pare: " + str(p3["pare"]) + "\nVlasnistvo: " + str(p3["vlasnistvo"])
    labelStats = Label(frameStats, text=stats, font=("Calibri", 16))
    labelStats.pack()
    
def showPlayerStats_4():
    frameStats = Frame(root, width = 250, height = 300)
    frameStats.pack()
    frameStats.place(anchor = 'center', relx = 0.83, rely = 0.25)
    stats = "Pare: " + str(p4["pare"]) + "\nVlasnistvo: " + str(p4["vlasnistvo"])
    labelStats = Label(frameStats, text=stats, font=("Calibri", 16))
    labelStats.pack()


#*kocke duh
def dice(igrac):
    diceNumber1 = random.randint(1,6)
    diceNumber2 = random.randint(1,6)
    igrac["polje"] += (diceNumber1 + diceNumber2)
    if (igrac["polje"] >= 40):
        igrac["polje"] = 0
        igrac["pare"] += 200
    showDice(diceNumber1, diceNumber2)

#TODO pokazi rezultat kocke
def showDice(diceNumber1, diceNumber2):
    pass
    
#* sve je roknuto u main jer je tak lakse neke stvari napravit
def main():
    #*slika ploce
    framePloce = Frame(root, width = 600, height = 600)
    framePloce.pack()
    framePloce.place(anchor = 'nw', relx = 0, rely = 0)
    ploca = ImageTk.PhotoImage(Image.open("ploca.png"))
    label = Label(framePloce, image=ploca)
    label.pack()


    #* buttoni za playere, sve se moze na pocetku iskazat, netreba .config();
    #! command priziva funkciju, al neda da stavis args pa je zato 4 funkcije za ljude
    #TODO ide image= za sliku
    p1Button = Button(root, text = "1", font=("Calibri", 16), command = showPlayerStats_1)
    p2Button = Button(root, text = "2", font=("Calibri", 16), command = showPlayerStats_2)
    p3Button = Button(root, text = "3", font=("Calibri", 16), command = showPlayerStats_3)
    p4Button = Button(root, text = "4", font=("Calibri", 16), command = showPlayerStats_4)
    #* placeanje koordinata za buttone
    p1Button.place(x = 610, y = 10)
    p2Button.place(x = 690, y = 10)
    p3Button.place(x = 770, y = 10)
    p4Button.place(x = 850, y = 10)

    mainloop()
#* mjesto gdje main pocinje
#TODO NAPRAVI NES JBT, probaj 
if(__name__ == "__main__"):
    test_fn() #!provjerava jel radi file link
    main()