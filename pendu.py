#!/usr/bin/env python3

from random import*
import os
import sys

score = 0

def dessinPendu(nb):
    tab=[
    """
       +-------+
       |       |
       |
       |
       |
       |
    ==============
    """
        ,
    """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """
        ,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """
    ]
    return tab[nb]

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def restart():
    continuer = input("Voulez-vous faire encore une partie [y/N] : ").lower()
    if continuer == 'y':
        pendu()
    else:
        exit()

def pendu():
    global score
    lettres_utilisees = []
    mots = []
    nb_erreurs = 0
    lettres = [chr(i) for i in range(65, 91)]
    with open("dico.txt", "r", encoding="utf-8") as filin:
        for ligne in filin:
            mots.append(ligne)
    for mot in range(len(mots)):
        mots[mot] = mots[mot].rstrip('\n')

    nb = randint(0,len(mots))
    mot_choisi = mots[nb]
    #print(mot_choisi)

    print("JEU DU PENDU")
    mot_cache = ["_" for c in range(len(mot_choisi))]
    for i in range(len(mot_cache)-1):
        print(f"{mot_cache[i]} ", end="")
    print(mot_cache[-1])

    while nb_erreurs <= 7:
        lettre = input("Saississez une lettre : ").upper()
        if lettre in lettres_utilisees:
            print("Tu as déjà utilisé cette lettre !")
        else :
            if lettre == '':
                print("Veuillez saisir une lettre.")
            if lettre not in lettres:
                print("Veuillez saisir un caractère valide. Dommage pour vous !")
            elif lettre not in lettres_utilisees:
                lettres_utilisees.append(lettre)
            # print(lettres_utilisees)
            if lettre in mot_choisi:
                for i in range(len(mot_choisi)):
                    if mot_choisi[i] == lettre:
                        mot_cache[i] = lettre
                        #print(mot_cache)
                        if "_" not in mot_cache:
                            score += 1
                            print(f"Félicitations, vous avez gagné ! Le mot à deviner était {mot_choisi}.")
                            print(f"Votre score est désormais de {score}.")
                            restart()
            else:
                print(dessinPendu(nb_erreurs))
                nb_erreurs = nb_erreurs+1
                if nb_erreurs == 7:
                    print(f"Vous avez perdu ! Le mot à trouver était : {mot_choisi}. Réessayez et peut-être que vous réussirez !")
                    print(f"Votre score était de {score}. Il a été maintenant réinitialisé à 0.")
                    score = 0
                    restart()
            for i in range(len(mot_cache)-1):
                print(mot_cache[i], end="")
                print(" ", end="")
            print(mot_cache[-1])

pendu()
