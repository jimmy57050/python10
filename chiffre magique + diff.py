from random import *

d = int(input("Veuillez saisir la difficulté : 1, 2 ou 3. "))
n = 0
if d == 1 : 
    
    while random != n  :
        random = randint(1,10)
        n = int(input("Veuillez saisir votre nombre. "))
elif n <= 0 :
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
            
if d == 2 : 
    while random != n  :
        int(input("Veuillez saisir votre nombre. "))
        random = randint(1,100)
        if n <= 0 :
            print ("Valeur non permise")
            n = int(input("Veuillez saisir un nombre plus grand. "))
        elif n >= 101 :
            print ("Valeur non permise")
            n = int(input("Veuillez saisir un nombre plus petit. "))
        elif n < random :
            print ("Trop petit. ") 
            n = int(input("Veuillez saisir un nombre plus grand. "))
        elif n > random : 
            print ("Trop grand. ")
            n = int(input("Veuillez saisir un nombre plus petit. "))  


if d == 3 :
    while random != n  : 
        int(input("Veuillez saisir votre nombre. "))
        random = randint(1,1000)
        if n <= 0 :
            print ("Valeur non permise")
            n = int(input("Veuillez saisir un nombre plus grand. "))
        elif n >= 1001 :
            print ("Valeur non permise")
            n = int(input("Veuillez saisir un nombre plus petit. "))
        elif n < random :
            print ("Trop petit. ") 
            n = int(input("Veuillez saisir un nombre plus grand. "))
        elif n > random : 
            print ("Trop grand. ")
            n = int(input("Veuillez saisir un nombre plus petit. "))

print ("Gagné.")


        