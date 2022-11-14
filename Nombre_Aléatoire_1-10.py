from random import *
random = randint(1,10)

n = int(input("Veuillez saisir un chiffre entre 1 et 10. "))

if n == random : 
    print("Gagné. ")

while random != n  :
        if n < 0 :
            print ("Valeur non permise")
            n = int(input("Veuillez saisir un nombre plus grand. "))
        elif n >= 11 :
            print ("Valeur non permise")
            n = int(input("Veuillez saisir un nombre plus petit. "))
        elif n < random :
            print ("Trop petit. ") 
            n = int(input("Veuillez saisir un nombre plus grand. "))
        elif n > random : 
            print ("Trop grand. ")
            n = int(input("Veuillez saisir un nombre plus petit. "))
               
print ("Gagné.")