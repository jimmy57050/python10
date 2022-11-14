TTC = int(input("veuillez saisir votre montant. "))

if 500<=TTC<=1000 :
    print ("Votre montant est de ", TTC * 1.02)
elif    1000<=TTC<=2000 :
    print ("Votre montant est de ", TTC * 1.05)
elif TTC>=2000 :
    print ("Votre montant est de ", TTC * 1.10)
