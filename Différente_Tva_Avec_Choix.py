prixHT = int(input("veuillez saisir votre prix HT. "))

print ("Les taux de TVA possible sont : ")
print ("pour une TVA de 5,5  : saisissez 1")
print ("pour une TVA de 19.6 : saisissez 2")
print ("pour une TVA de 33   : saisissez 3")

TVA = int(input("veuillez saisir votre code. "))

if TVA == 1 :
    print ("Le prix HT est de",prixHT,"€","La TVA est de 5.5","et Le prix TTC est de",prixHT * 1.055,"€" ) 
elif TVA == 2 : 
    print ("Le prix HT est de",prixHT,"€","La TVA est de 19.6","et Le prix TTC est de",prixHT * 1.196,"€" )
elif TVA == 3 :
    print ("Le prix HT est de",{prixHT},"€","La TVA est de 33","et Le prix TTC est de",prixHT * 1.33,"€" )







