#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 08:09:21 2019
@author: sku35268
"""

import random

def mala():
    inName = input(" Zadejte jméno souboru:  ")
    inFile = open(inName,"r")
    outName = input(" Zadejte jméno výstupního souboru:  ")
    outFile = open(outName, "w")
    while 1:
        radek=inFile.readline()
        if radek =="":
            break
        outFile.write(radek.lower())
    inFile.close()
    outFile.close()
    print()
    print("Hotovo")
    print("--------------------------------------")
    

def nahrazeni():  
    inName = input(" Zadejte jméno souboru:  ")
    inFile = open(inName,"r")
    outName = input(" Zadejte jméno výstupního souboru:  ")
    outFile = open(outName, "w")
    znakStary = input(" Zadejte znak, který chcete nahradit:  ")
    znakNovy = input(" Zadejte znak, kterým ho chcete nahradit:  ")
    while 1:
        radek = inFile.readline()
        if radek=="":
            break
        outFile.write(radek.replace(znakStary, znakNovy))
    print()
    print("Hotovo")
    print("--------------------------------------")
    
    
def statistika():
    inName = input(" Zadejte jméno souboru:  ")
    inFile = open(inName,"r")
    pocetradku=0
    pocetznaku=0
    pocetslov=0
    cetnostznaku={}
    while 1:
        radek=inFile.readline()
        if radek =="":
            break
        pocetradku+= 1
        delka=len(radek)
        pocetznaku += delka
        pocetslov +=len(radek.split())
        for znak in radek:
            if znak in(" ","\t", "\n"):
                continue
            if znak in cetnostznaku:
                cetnostznaku[znak]+=1
            else:
                cetnostznaku[znak]=1
    print()
    print("-------------statistika---------------")
    for item in cetnostznaku.items():print("{}\t{}".format(*item))
    print("--------------------------------------")
    print ("počet řádků:", pocetradku)
    print ("počet slov:", pocetslov)
    print ("počet znaků:", pocetznaku)
    print("--------------------------------------")

   
def nahodny_text(pocetslov):
    def slovo():
        SAMOHLASKY="aeiou"
        SOUHLASKY="bcčdďfghjklmnňoprřsštťvzžchdž"
        delkaslova = random.randint(3,8)
        zacatek= random.randint(1,2) #začínám samohláskou nebo souhláskou
        vystup=""
        for i in range(delkaslova):
            if zacatek:
                vystup+= random.choice(SOUHLASKY)
            else:
                vystup+= random.choice(SAMOHLASKY)
            zacatek=not(zacatek)
        return vystup
    vysledek = tuple()
    for i in range(pocetslov):
        vysledek=vysledek+(slovo(), )
    return " ".join(vysledek)

       

while True:
    print("1) Převod na malá písmena")
    print("2) Nahrazení znaků")
    print("3) Statistika souboru ")
    print("4) Generování náhodného textu")
    print("5) Konec")
    try:
        volba = int(input("1-5> "))
        if volba == 1:
            mala()
        elif volba == 2: 
            nahrazeni()
        elif volba == 3: 
            statistika()
        elif volba == 4:
            pocet_slov=int(input("Zadej počet slov: "))
            print("\n",nahodny_text(pocet_slov),"\n")
        elif volba == 5: 
            exit(0)
        else:
            print("\n>>>> Zadej číslo od 1 do 5\n")
    except ValueError: 
        print("\n>>>> Zadej číslo od 1 do 5\n")
    except EOFError: 
        exit(0) 
