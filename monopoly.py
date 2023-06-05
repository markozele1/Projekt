from tkinter import *
from tkinter import messagebox
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
p1 = {"polje":0,"pare":1500,"vlasnistvo":[],"u_zatvoru":False,"bankrot":False, "ime": "p1"}
p2 = {"polje":0,"pare":1500,"vlasnistvo":[],"u_zatvoru":False,"bankrot":False, "ime": "p2"}
p3 = {"polje":0,"pare":1500,"vlasnistvo":[],"u_zatvoru":False,"bankrot":False, "ime": "p3"}
p4 = {"polje":0,"pare":1500,"vlasnistvo":[],"u_zatvoru":False,"bankrot":False, "ime": "p4"}

#*lista u kojoj se spremaju igraci i varijabla u kojoj se prati trenutni igrac
igraci = [p1,p2,p3,p4]
trenutni_igrac = 0

#*pokazi profile ljudi, uljepsano
def showPlayerStats(igrac):
    frameStats = Frame(root, width = 250, height = 300)
    frameStats.pack()
    frameStats.place(anchor = 'center', relx = 0.83, rely = 0.25)
    stats = "Pare: " + str(igrac["pare"]) + "\nBroj vlasnistva: " + str(len(igrac["vlasnistvo"])) + "\nPolje: " + str(igrac["polje"])
    labelStats = Label(frameStats, text=stats, font=("Calibri", 16))
    labelStats.pack()
    showButton = Button(root, text = "Prikaz vlasnistva", font = ("Calibri", 16), command = lambda: showVlasnistvo(igrac) )
    showButton.place(x = 670, y = 250)
def showVlasnistvo(igrac):
    messagebox.showinfo("Info",f'{igrac["vlasnistvo"]}')
    
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
        poljeAction(igrac,trenutno_polje)
    elif(not(trenutno_polje["vlasnik"])):
        if(messagebox.askyesno('Kupnja', f'Hoces li kupiti ovo polje? \n {trenutno_polje["ime"]}')):
            kupiPolje(igrac, trenutno_polje)
            print(trenutno_polje["ime"])
    elif(trenutno_polje["vlasnik"] != trenutni_igrac["ime"]):
        for x in trenutno_polje:
            if (x == "ime" or x == "vlasnik" or x == "cijenaKuce" or x == "cijena"):
                continue
            if (trenutno_polje[x][0] and trenutni_igrac["pare"] > trenutno_polje[x][0]):
                trenutni_igrac["pare"] -= trenutno_polje[x][1]
                trenutno_polje["vlasnik"]["pare"] += trenutno_polje[x][1]
            else:
                messagebox.showerror("Rip bozo", "Nemas prebijenih parica brat moj")
                igraci.remove(trenutni_igrac)

#* provjerava posebne kartice
#TODO napravit sve sto pise TODO u printovima

def kupiPolje(igrac, trenutno_polje):
    if igrac["pare"] >= trenutno_polje["cijena"]:
        igrac["vlasnistvo"].append(trenutno_polje["ime"])
        trenutno_polje["vlasnik"] = igrac["ime"]
        igrac["pare"] -= trenutno_polje["cijena"]
    # ne stane sav tekst u window, pa sam izbacio
    # prikazivanje vlasnistva


def poljeAction(igrac,trenutno_polje):
    action = trenutno_polje[1]
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
    # jel fali taxing na tudim zemljistima?
    # if so reci pa cu onda dodati taj dio

def showDice(diceNumber1, diceNumber2):
    diceFrame1 = Frame(root, width=85, height=85)
    diceFrame2 = Frame(root, width=85, height=85)
    diceFrame1.pack()
    diceFrame2.pack()
    diceFrame1.place(anchor='se', relx=0.9, rely=0.95)
    diceFrame2.place(anchor='sw', relx=0.9, rely=0.95)
    dice1_image = Image.open(str(diceNumber1) + ".png")
    dice2_image = Image.open(str(diceNumber2) + ".png")
    dice1 = ImageTk.PhotoImage(dice1_image)
    dice2 = ImageTk.PhotoImage(dice2_image)
    diceLabel1 = Label(diceFrame1, image=dice1)
    diceLabel2 = Label(diceFrame2, image=dice2)
    diceLabel1.Image = dice1
    diceLabel2.Image = dice2
    diceLabel1.pack()
    diceLabel2.pack()


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

#TODO placanje vlasniku ako naletis na kupljeno polje
