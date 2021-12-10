from colorama import Fore, Back, Style
()
import random
motAleatoire = ("arbres","bijoux","etudes","gagner","glisse","visite","soeurs","cuivre","joueur","budget")
mot =random.choice(motAleatoire)
motADeviner = mot
tentatives = 1

while tentatives<8:
    for i in range(len(tentatives)):
        tentatives=input("choisi un mot composer de 6 lettres")
        i=tentatives
        for i in (len(tentatives)):
            if tentatives(i) == mot:
                print(Back.RED+tentatives)
                break
            elif tentatives(i) != mot:
                print(Back.BLUE+tentatives)
                break

