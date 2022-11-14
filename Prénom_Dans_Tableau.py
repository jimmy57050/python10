#prénoms = ["hugo","Flora","Jp","Céline"]

prénoms = []

for i in range (5) :
    prénoms += [str(input("Veuillez saisir votre prénom.  ")).upper()]


indice = []

for prénom in range(len(prénoms)) :
    if prénoms[prénom] == "HUGO" :
        indice.append(prénom)
        print ("l'indice est de : ",indice )
    if prénoms[prénom] != "hugo " : 
        print ("Le prénom n'est pas dans le tableau. ")


