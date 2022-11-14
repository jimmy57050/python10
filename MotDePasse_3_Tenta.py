mdp = str(input("veuillez saisir votre mot de passe. "))

b = "bonjour"
a = 1 
c = "minou"
if mdp == b : 
    print("Bienvenue. ")

while mdp != b :
    print ("Veuillez réessayer.")
    mdp = str(input("Veuillez saisir votre mot de passe."))
    a = a + 1
    if mdp == b :
        print("Bienvenue. ")
        break

    if a == 3 : 
        print("Votre compte est bloqué. trop d'authentification.") 
        réponse = str(input("Quel est la Réponse à votre question secrète ? "))
        if réponse == c : 
            print("Bienvenue. ")
            break
        else : 
            print("Accès réfusé. ")
            break
    
    

    

    