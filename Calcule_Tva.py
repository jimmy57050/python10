a = int(input("Prix HT "))
b = int(input("Quantité "))
ht = a*b
remise = 15
somme = ht*remise/100
somme2 = ht-somme
tva = somme2*20/100
somme3 = somme2+tva
print ("le résultat est",somme3)