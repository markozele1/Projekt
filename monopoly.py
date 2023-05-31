from tkinter import *
from PIL import ImageTk, Image
import random
from zemlje import *

#* root window, not resizable
root =  Tk()
root.title("Monopoly")
root.geometry("900x600+200+200")
root.resizable(False, False)

#*slika ploce
framePloce = Frame(root, width = 600, height = 600)
framePloce.pack()
framePloce.place(anchor = 'nw', relx = 0, rely = 0)
ploca = ImageTk.PhotoImage(Image.open("ploca.png"))
label = Label(framePloce, image=ploca)
label.pack()

#*igraci i pocetno stanje
p1 = {"polje":0,"pare":1500,"vlasnistvo":["1"],"u_zatvoru":False,"bankrot":False}
p2 = {"polje":0,"pare":1500,"vlasnistvo":["2"],"u_zatvoru":False,"bankrot":False}
p3 = {"polje":0,"pare":1500,"vlasnistvo":["3"],"u_zatvoru":False,"bankrot":False}
p4 = {"polje":0,"pare":1500,"vlasnistvo":["4"],"u_zatvoru":False,"bankrot":False}

#*lista u kojoj se spremaju igraci i varijabla u kojoj se prati trenutni igrac
igraci = [p1,p2,p3,p4]
trenutni_igrac = 0

#*pokazi profile ljudi, uljepsano
def showPlayerStats(igrac):
    frameStats = Frame(root, width = 250, height = 300)
    frameStats.pack()
    frameStats.place(anchor = 'center', relx = 0.83, rely = 0.25)
    stats = "Pare: " + str(igrac["pare"]) + "\nVlasnistvo: " + str(igrac["vlasnistvo"]) + "\nPolje: " + str(igrac["polje"])
    labelStats = Label(frameStats, text=stats, font=("Calibri", 16))
    labelStats.pack()

#*kocke, daju broj za kolko ici, premjestaju na sljedeceg igraca
def dice(igrac):
    global trenutni_igrac
    diceNumber1 = random.randint(1,6)
    diceNumber2 = random.randint(1,6)
    #TODO ako igrac ode u zatvor
    if(igrac["u_zatvoru"]):
        poljeCheck(igrac)
    igrac["polje"] += (diceNumber1 + diceNumber2)
    if (igrac["polje"] >= 40):
        igrac["polje"] -= 40
        igrac["pare"] += 200
    poljeCheck(igrac)
    if(trenutni_igrac < len(igraci)-1):
        trenutni_igrac += 1
    else:
        trenutni_igrac = 0
    showDice(diceNumber1, diceNumber2)
    showPlayerStats(igrac)

#* provjerava trenutno polje na kojem se igrac nalazi
def poljeCheck(igrac):
    trenutno_polje = polja[igrac["polje"]]
    if("nonbuy" in trenutno_polje):
        poljeAction(igrac,trenutno_polje[1])
    else:
        #TODO kupnja nonbuy polja
        print(trenutno_polje["ime"])

#* provjerava posebne kartice
#TODO napravit sve sto pise TODO u printovima
def poljeAction(igrac,action):
    if(action == "tax"):
        igrac["pare"] -= 200
    elif(action == "luxtax"):
        igrac["pare"] -= 100
    elif(action == "pickComm"):
        print("TODO commchest karte")
    elif(action == "pickChance"):
        print("TODO chance karte")
    elif(action == "jailCheck"):
        print("TODO jail check")
    elif(action == "gotoJail"):
        igrac["polje"] = 10
        igrac["u_zatvoru"] = True
    elif(action == "parkingCheck"):
        print("TODO parking")

#TODO pokazi rezultat kocke
def showDice(diceNumber1, diceNumber2):
    pass
    
#* sve je roknuto u main jer je tak lakse neke stvari napravit
def main():
    #* buttoni za playere, sve se moze na pocetku iskazat, netreba .config();
    #! command priziva funkciju, al neda da stavis args pa je zato 4 funkcije za ljude
    #TODO ide image= za sliku
    p1Button = Button(root, text = "1", font = ("Calibri", 16), command = lambda: showPlayerStats(p1))
    p2Button = Button(root, text = "2", font = ("Calibri", 16), command = lambda: showPlayerStats(p2))
    p3Button = Button(root, text = "3", font = ("Calibri", 16), command = lambda: showPlayerStats(p3))
    p4Button = Button(root, text = "4", font = ("Calibri", 16), command = lambda: showPlayerStats(p4))
    diceButton = Button(root,text = "Roll!", font = ("Calibri", 16), command = lambda: dice(igraci[trenutni_igrac]))
    
    #* placeanje koordinata za buttone
    p1Button.place(x = 610, y = 10)
    p2Button.place(x = 690, y = 10)
    p3Button.place(x = 770, y = 10)
    p4Button.place(x = 850, y = 10)
    diceButton.place(x = 610, y = 550)
    mainloop()


#* mjesto gdje main pocinje
#TODO NAPRAVI NES JBT, probaj 
if(__name__ == "__main__"):
    test_fn() #!provjerava jel radi file link
    main()