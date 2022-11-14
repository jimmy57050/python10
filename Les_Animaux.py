
a = int(input("L'animal est-il mammifère ou ovipare ( 1 pour mammifère, 2 pour ovipare) ? "))

if a == 2 : 
    print ("l'animal est un ovipare. ")
    b = int(input("Est-il a plume ou à écaille ? ( 1 pour plume , 2 pour écaille ) "))  

    if b == 1 :
        print ("C'est un oiseau. ")
    elif b == 2 : 
        c =  int(input("Vit-il dans l'eau ? ( 1 pour oui , 2 pour non ) "))

        if c == 2 : 
            print("C'est un reptile. ")

if a == 1 : 
    d = int(input("Vit-il sur terre ou dans l'eau ? ( 1 pour terre , 2 pour eau ) "))
    
    if d == 2 : 
        print("C'est un cétacé. ")

    if d == 1 :
        e =  int(input("Fait-il 'miaou' ou 'waf-waf' ( 1 pour miaou , 2 pour waf-waf )"))

    if  e == 1 :
        print("C'est un chat ! ")
    





    






