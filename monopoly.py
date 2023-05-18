# from tkinter import *
import random
# root =  Tk()
# root.geometry("600x600+200+200")



#kocke duh
def kocke(igrac):
    igrac["polje"] += random.randint(2,12);


#igraci i pocetno stanje
p1 = {"polje":0,"pare":1500,"vlasnistvo":[],"u_zatvoru":False,"bankrot":False}
p2 = {"polje":0,"pare":1500,"vlasnistvo":[],"u_zatvoru":False,"bankrot":False}
p3 = {"polje":0,"pare":1500,"vlasnistvo":[],"u_zatvoru":False,"bankrot":False}
p4 = {"polje":0,"pare":1500,"vlasnistvo":[],"u_zatvoru":False,"bankrot":False}

#mainloop()
