#Calcul de l'indemnité journalière pendant le remplacement
NmbrJ = int(input("veuillez saisir le nombre de jours "))
distance = int(input("Veuillez saisir la distance entre le lieu de résidence et le lieu ou s'effectue le remplacement "))
TauxIndemRep = 15 * NmbrJ *2

if distance <15 :
    TauxIndemJ = 12.50 * NmbrJ
elif distance <30 : 
        TauxIndemJ=23.50 * NmbrJ
elif distance<45 :
         TauxIndemJ=30.00 * NmbrJ
elif distance<65 :
         TauxIndemJ=37.00 * NmbrJ
elif distance<85 : 
         TauxIndemJ=44.00 * NmbrJ
elif distance<105 :
         TauxIndemJ=50.00 * NmbrJ
elif distance<1000 : 
        TauxIndemJ=50.00 * NmbrJ


print  ("le taux d'indemnité pour la durée du remplacement est de", TauxIndemJ+TauxIndemRep )


