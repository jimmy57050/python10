f = int(input("Veuillez saisir la moyenne de français. "))    
while f > 20 :
    while f.isnumeric()==False:
        print ("Valeur incorrect ")
    f = int(input("Veuillez saisir un chiffre plus petit. "))
while f < 0 : 
        print ("Valeur incorrect ")
        f = int(input("Veuillez saisir un chiffre plus grand. "))


coeff = int(input("Veuillez saisir la Coef français. "))
while coeff > 20 :
    print ("Valeur incorrect ")
    coeff = int(input("Veuillez saisir un chiffre plus petit. "))
while coeff < 1 : 
        print ("Valeur incorrect ")
        coeff = int(input("Veuillez saisir un chiffre plus grand. "))



m = int(input("Veuillez saisir la moyenne de math. "))
while m > 20 :
    print ("Valeur incorrect ")
    m = int(input("Veuillez saisir un chiffre plus petit. "))
while m < 0 : 
        print ("Valeur incorrect ")
        m = int(input("Veuillez saisir un chiffre plus grand. "))



coefm = int(input("Veuillez saisir la coef de math. "))
while coefm > 20 :
    print ("Valeur incorrect ")
    coefm = int(input("Veuillez saisir un chiffre plus petit. "))
while coefm < 0 : 
        print ("Valeur incorrect ")
        coefm = int(input("Veuillez saisir un chiffre plus grand. "))




i = int(input("Veuillez saisir la moyenne de info. "))
while i > 20 :
    print ("Valeur incorrect ")
    i = int(input("Veuillez saisir un chiffre plus petit. "))
while i < 0 : 
        print ("Valeur incorrect ")
        i = int(input("Veuillez saisir un chiffre plus grand. "))



coefi = int(input("Veuillez saisir la coef d'info. "))
while coefi > 20 :
    print ("Valeur incorrect ")
    coefi = int(input("Veuillez saisir un chiffre plus petit. "))
while coefi < 0 : 
        print ("Valeur incorrect ")
        coefi = int(input("Veuillez saisir un chiffre plus grand. "))



g = int(input("Veuillez saisir la moyenne de géo. "))
while g > 20 :
    print ("Valeur incorrect ")
    g = int(input("Veuillez saisir un chiffre plus petit. "))
while g < 0 : 
        print ("Valeur incorrect ")
        g = int(input("Veuillez saisir un chiffre plus grand. "))


coefg = int(input("Veuillez saisir la coef de géo. "))
while coefg > 20 :
    print ("Valeur incorrect ")
    coefg = int(input("Veuillez saisir un chiffre plus petit. "))
while coefg < 0 : 
        print ("Valeur incorrect ")
        coefg = int(input("Veuillez saisir un chiffre plus grand. "))



moyfr = f * coeff 
moymath = m * coefm
moygeo = g * coefg
moyinfo = i * coefi 

moyenne = (moyfr + moymath + moygeo + moyinfo)
coef = (coeff + coefm + coefg + coefi)


if moyenne / coef <= 4 :
    print ("la moyenne est de", moyenne / coef,"," "mention nul.")

if moyenne / coef <= 8 > 4 :
    print ("la moyenne est de", moyenne / coef,"," "mention Insuffisant.")

if moyenne / coef <= 12 > 8 :
    print ("la moyenne est de", moyenne / coef,"," "mention assez bien.")

if moyenne / coef <= 16 > 12 :
    print ("la moyenne est de", moyenne / coef,"," "mention bien.")

if moyenne / coef <= 20 >16 :
    print ("la moyenne est de", moyenne / coef,"," "mention trés bien.")











