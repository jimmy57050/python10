password = "Bonjour"
attemptCount = 3
userPassword = ""

while attemptCount != 0 and userPassword != password:
    userPassword = input(f"Veuillez saisir votre mot de passe ({attemptCount} essai.s restant.s) : ")
    attemptCount = attemptCount - 1

# Ici on est sorti de la boucle si mot de passe est valide ou nombre d'essais épuisé
# Soit attemptCount == 0
# Soit userPassword == password
if attemptCount == 0:
    print("Vous n'avez plus d'essais disponibles, votre compte est désormais bloqué.")
    isUserAnswerYes = input("Voulez vous répondre à votre question secrète ? (oui/non) : ").lower() == "oui"
    if isUserAnswerYes:
        isTheGoodAnswer = input("Quel est le nom de votre chat ? ").lower() == "minou"      # lower pour tout en minscule  // upper pour tout en maj
        if isTheGoodAnswer:
            print("Accès autorisé.")
        else:
            print("Votre compte est bloqué.")
    else:
        print("Votre compte est bloqué.")
else:
    print("Accès autorisé.")