from random import randint

from time import sleep

import sys, os

zahl = randint(1, 100)

name1 = input("Spieler 1 gebe deinen Namen ein: ")
name2 = input("Spieler 2 gebe deinen Namen ein: ")

while True:

    while True:
        try:
            zahl1 = int(input("- " + name1 + " gebe deine Zahl ein: "))
        except ValueError:
            print(name1 + ", du musst eine Ganzzahl eingeben.")
        else:
            break
	
    if zahl > zahl1:
        print("Die gesuchte Zahl ist größer als ", zahl1)   
        sleep(2.0)
        os.system("clear")         
    elif zahl < zahl1:
        print("Die gesuchte Zahl ist kleiner als ", zahl1)
        sleep(2.0)
        os.system("clear")
    else:
        print("Die Gesuchte Zahl ist ", zahl)
        print(name1, " gewinnt!")
        break
    
    while True:
        try:
            zahl2 = int(input("- " + name2 + " gebe deine Zahl ein: "))
        except ValueError:
            print(name2 + ", du musst eine Ganzzahl eingeben.")
        else:
            break
    
    if zahl > zahl2:            
        print("Die gesuchte Zahl ist größer als ", zahl2)      
        sleep(2.0)
        os.system("clear")      
    elif zahl < zahl2:
        print("Die gesuchte Zahl ist kleiner als ", zahl2)
        sleep(2.0)
        os.system("clear")
    else:
        print("Die Gesuchte Zahl ist ", zahl)         
        print(name2, " gewinnt!")
        break
