départ = int(input("Veuillez saisir un chiffre de départ. "))
arrivée = int(input("Veuillez saisir un chiffre d'arrivée. "))
pas = int(input("Veuillez saisir un pas. "))

while départ < arrivée : 
    print(départ) # end=" " pour ne pas aller a la ligne
    départ += pas      