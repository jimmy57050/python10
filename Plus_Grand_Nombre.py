z = 0
a = 1
b = 0

while a != 0 : 
    nombre = int(input("Veuillez saisir un nombre."))
    if nombre == b :
        break
    if nombre > z :  # Si le chiffre est plus grand que 0, Z prend la place du nombre, puis si un chiffre plus grand viens, il le remplace etc..
        z = nombre 
print ("Votre nombre le plus grand est : ", z)
