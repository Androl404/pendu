from random import*

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

def restart():
    continuer=input("Voulez-vous faire encore une partie ('y' ou 'n') : ")
    if continuer=='y':
        pendu()
    else:
        exit()

def pendu():
    global score
    lettres_utilisees=[]
    mots=[]
    nb_erreurs=0
    lettre_min = [chr(i) for i in range(97, 123)]
    lettre_maj = [chr(i) for i in range(65, 91)]
    with open("dico.txt", "r", encoding="utf-8") as filin:
        for ligne in filin:
            mots.append(ligne)
    for mot in range(len(mots)):
        mots[mot] = mots[mot].rstrip('\n')

    nb=randint(0,len(mots))
    mot_choisi=mots[nb]
    #print(mot_choisi)

    print("JEU DU PENDU")
    #mot_cache ="_ "*len(mot_choisi)
    mot_cache = ["_" for c in range(len(mot_choisi))]
    for i in range(len(mot_cache)-1):
        print(mot_cache[i], end="")
        print(" ", end="")
    print(mot_cache[-1])

    while nb_erreurs<=7:
        lettre=input("Saississez une lettre :")
        if lettre in lettres_utilisees:
            print("Tu as déjà utilisé cette lettre !")
        else :
            if lettre == '':
                print("Veuillez saisir une lettre.")
            if lettre not in lettre_maj and lettre not in lettre_min:
                print("Veuillez saisir un caractère valide. Dommage pour vous !")
            elif lettre not in lettres_utilisees:
                if lettre not in lettre_min:
                    lettres_utilisees.append(lettre)
                    for i in range(len(lettre_maj)):
                        if chr(i+65)==lettre:
                            lettres_utilisees.append(chr(i+97))
                else:
                    lettres_utilisees.append(lettre)
                    for i in range(len(lettre_min)):
                        if chr(i+97)==lettre:
                            lettres_utilisees.append(chr(i+65))
            if lettre in lettre_min:
                for i in range(len(lettre_min)):
                    if lettre_min[i]==lettre:
                        lettre = chr(i+65)
            # print(lettres_utilisees)
            if lettre in mot_choisi:
                for i in range(len(mot_choisi)):
                    if mot_choisi[i]==lettre:
                        mot_cache[i]=lettre
                        #print(mot_cache)
                        if "_" not in mot_cache:
                            score += 1
                            print("Félicitations, vous avez gagné ! Le mot à deviner était " + mot_choisi + ".")
                            print("Votre score est désormais de " + str(score) + ".")
                            restart()
                            #exit()
                # print("ok")
            else:
                print(dessinPendu(nb_erreurs))
                nb_erreurs=nb_erreurs+1
                if nb_erreurs==7:
                    print("Vous avez perdu ! Le mot à trouver était : " + mot_choisi + ". Réessayez et peut-être que vous réussirez !")
                    print("Votre score était de " + str(score) + ". Il a été maintenant réinitialisé à 0.")
                    score = 0
                    restart()
            for i in range(len(mot_cache)-1):
                print(mot_cache[i], end="")
                print(" ", end="")
            print(mot_cache[-1])

pendu()
