imm = str(input("êtes vous le chef de famille. (o pour oui, n pour non) "))
n = 0
if imm == "n":
    print("vous n'êtes pas élligible au allocs")
elif imm == "o" :
    print ("vous êtes elligible au allocs ")

nmbrht = int(input("Veuillez saisir le nombres d'heures de travail du chef de foyer pendant le mois "))
Mensualité = 0 

Charge = str(input("Avez vous des enfants a charges. (o pour oui, n pour non) "))

if Charge == "o" : 
    nmbrenf =  int(input("Combien avez vous d'enfants. "))



while nmbrenf > n : 
    AgeFinMois = int(input("quel age a l'enfant "))
   
    if AgeFinMois <= 3 : 
        Mensualité = 120.60
    elif AgeFinMois <= 6 :
        Mensualité = 180.90
    elif AgeFinMois <= 10 : 
        Mensualité = 217.00
    elif AgeFinMois <= 21 :
        Mensualité = 253.20
    if 75 < nmbrht < 144 : 
        aloc = (Mensualité /145 * nmbrht)
    elif nmbrht >= 145 :
        aloc = Mensualité 
    elif nmbrht < 75 :
        aloc = Mensualité * 0
    print(aloc)
    n= n+1


print ("LE montant des allocations familiales est.", aloc  )



