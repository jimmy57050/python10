
                                         # Exercice calcule de la moyenne d'un élève : 
                    #len = prend tout dans un tableau
                    # .append(variable a ajouter)
                    #sum aditionne tout les variables dans le tableau 

fr = int(input("Veuillez saisir la note de français. "))
math = int(input("Veuillez saisir la note de math. "))
géo = int(input("Veuillez saisir la note de géo. "))
info = int(input("Veuillez saisir la note d'info. "))
# nouvelle matière = int(input("Veuillez saisir la note de ?nouvelle matière? "))

moyenne = fr + math + géo + info # rajouter une matière ici si voulu 
moyenne2 = moyenne / 4   # augmenter le diviseur de 1 par matière ajouté 
choix = 0 

tab = ["             ", "      ### Mon Tableau ###","                ","   1. Afficher les notes    ","   2. Afficher les notes de français    ","   3. Afficher les notes de maths    ","   4. Afficher la note de Géométrie    ","   5. Afficher la note d'informatique    ","   6. Calculer la moyenne    ","   7. Nouvelle moyenne    ","   0. Quitter   ","              "]
for element in tab : 
    print (element)


choix = int(input("#########  Qu'elle est votre choix   ##########? "))
while choix != 0 :
    if choix == 1 : 
        print ("                  ")
        print ("note de français : ", fr)
        print ("note de math : ", math)
        print ("note de géo : ", géo)
        print ("note d'info : ", info )
        for element in tab : 
            print (element)
        choix = int(input("#########  Qu'elle est votre choix   ##########? "))
    if choix == 2 : 
        print (            )
        print ("la moyenne de français est de : ",fr)
        for element in tab : 
            print (element)
        choix = int(input("#########  Qu'elle est votre choix   ##########? "))
    if choix == 3 : 
        print (                )
        print ("la moyenne de math est de : ",math)
        for element in tab : 
            print (element)
        choix = int(input("#########  Qu'elle est votre choix   ##########? "))
    if choix == 4 :
        print (                 )
        print("la moyenne de géo est de : ",géo)
        for element in tab : 
            print (element) 
        choix = int(input("#########  Qu'elle est votre choix   ##########? "))
    if choix == 5 :
        print (                 )
        print("la moyenne d'informatique est de : ",info)
        for element in tab : 
            print (element)
        choix = int(input("#########  Qu'elle est votre choix   ##########? ? ")) 
    if choix == 6 :
        print (                 )
        print ("la moyenne globale est de : ", moyenne2)
        for element in tab : 
            print (element)
        choix = int(input("#########  Qu'elle est votre choix   ##########? "))
    if choix == 7 : 
        print (                 )
        print ("la moyenne de '' est de : ")
        for element in tab : 
            print (element)
        choix = int(input("#########  Qu'elle est votre choix   ##########? "))

print ("          🔫🔫 Asta la vista 🔫🔫         ")

