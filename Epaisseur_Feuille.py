feuille = float(input("Veuillez saisir l'épaisseur de la feuille. "))
plis = float(input("Veuillez saisir un nombre de plis. "))

x = 0 
c = 0 
x = feuille

while c != plis :
    x = x * 2
    c = c + 1

print (f"L'épaisseur de la feuille est de {x}")