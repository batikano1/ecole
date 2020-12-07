import math
import random
import time
from threading import Thread

def example1():
    for i in range(3):
        try:
            x = int(input("enter a number: "))
            y = int(input("enter another number: "))
            print(x, '/', y, '=', x / y)
        except ZeroDivisionError as txt:
            print("erreur:", txt)
        except ValueError as txt:
            print("erreur:", txt)
        except:
            print("pas de chance ")


def example2(L):
    print("\n\nExample 2")
    sum = 0
    sumOfPairs = []
    for i in range(len(L)):
        try:
            sumOfPairs.append(L[i] + L[i + 1])
        except IndexError as txt:
            print("erreur", txt)
        except TypeError as txt:
            print("erreur", txt)

    print("sumOfPairs = ", sumOfPairs)


def printUpperFile(fileName):
    file = open(fileName, "r")
    for line in file:
        print(line.upper())
    file.close()


def main():
    example1()
    L = [10, 3, 5, 6, 9, 3]
    example2(L)
    example2([10, 3, 5, 6, "NA", 3])
    try:
        example3([10, 3, 5, 6])
    except NameError as name:
        print("erreur", name)
    try:
        printUpperFile("doesNotExistYest.txt")
    except FileNotFoundError as file:
        print("erreur", file)

    try:
        printUpperFile("./Dessssktop/misspelled.txt")
    except FileNotFoundError as file:
        print("file:", file)


# main()

"""
Activité 1:
    1:
        PROMIS JURÉ J'AI BOSSÉ !!!
    2:
        try:
            qqch
        except:
            qqch
    3:
         c'est les assert
         b=1
         ASSERT b==2
         
    4:
        nous les appelons les effect de bords
"""


def saisie(question):
    while True:
        try:
            a = int(input(question))
            return a
        except ValueError as value:
            print("erreur de valeur", value)
            continue
        except TypeError as type:
            print("erruer de type", type)
            continue


#print(saisie(("entier ou mort: ")))

print("\n===================================================\n")


def saisie_du_prof_qui_chipote(question, debut, fin):
    while True:
        try:
            a = int(input(question))
            debut = int(input(debut))
            fin = int(input(fin))
            if debut < a < fin:
                return a
        except ValueError as value:
            print("erreur de valeur", value)
            continue
        except TypeError as type:
            print("erreur de type", type)
            continue


#print(saisie_du_prof_qui_chipote("entrer qqch: ","debut: ","fin: "))

print("\n================================================\n")

def racine_carré_du_flemmard(question):
    while True:
        try:
            question = int(input(question))
            return print(math.sqrt(question))
        except ValueError as value:
            print("erreur de valeur", value)
            continue
        except TypeError as type:
            print("erreur de type", type)
            continue
#racine_carré_du_flemmard('voulez vous admirer la racine carré du flemmard ? alors entrer un entier: ')

print("\n================================================\n")

def ouveture_du_grimoire_ancestrale_de_Windows(fichier):
    try:
        fichier = str(input(fichier))
        print(open(fichier,"r"))
    except FileNotFoundError:
        print("le fichier n'est pas trouvé")
    except IOError as io:
        print("erreur{}".format(io))

#ouveture_du_grimoire_ancestrale_de_Windows("entrer la localition:")
print("\n================================================\n")

def jeu_de_la_mort():
    try:
        x = random.randint(0,100)
        print("vous devez arrêter le programme sur {}".format(x))
        print("Pour arrêter le programme il faut appuyer sur espace")
        b=input()
        i=0
        score = 0
        while i<100:
            i+=1
            score +=1
            print(i)
            time.sleep(1)
    except KeyboardInterrupt:
        if score == x:
            print("votre score {},youppi vous avez gagné".format(score))
        else:
            print("votre score {},dommage il vous fallait {}".format(score,x))
#jeu_de_la_mort()

print("\n================================================\n")

def le_roi_des_addition():
    nomb1   = random.randint(0,100)
    nomb2   = random.randint(0,100)
    reponse = nomb1+nomb2
    print("vous aller additionner les deux nombre qu'il vous resont donné")
    print("appuyer sur enter pour lancer ....(rester sur le vide et non a la fin de cette phrase")
    B=input()
    calcul = (str(nomb1) + "+" + str(nomb2) + "=")
    try:
        reponse1 = int(input((calcul)))
        if reponse == reponse1:
            print("bravo")

    except ValueError:
        pass

#le_roi_des_addition()
def timer():
    i = 0
    show= 0
    while i<10:
        try:
            i+=1
            show +=1
            if show == 10:
                i= 2/0
            time.sleep(1)
        except ZeroDivisionError:
            print("j'avais pas d'idée donc j'ai utilisé ma créativité mais ca fonctionne")
def le_jeux_tellement_compliqué_a_faire_que_je_ne_veux_plus_travailler():
    Thread(target=le_roi_des_addition()).start()
    Thread(target=timer()).start()

le_jeux_tellement_compliqué_a_faire_que_je_ne_veux_plus_travailler()
