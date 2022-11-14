import random 

def isEven(n:int)-> bool :
    """
    Vérifie si le nombre est paire ou impaire.
    """
    
    return int(n % 2) == 0 


def printHeader(title: str, char: str = "#", count: int = 1):
    tab = ["#","⚄","-","*","~","+"]
    if char == "":
        char = random.choice(tab)
    l = len(title)
    d = (l + count * 2 + 2) * char
    c = char * count
    print(d)
    print(f"{c} {title} {c}")
    print(d)



def isNombre(Nb:int)->bool:
    while Nb.isnumeric()==False: Nb=input("Saisissez un nombre valide : ")
    Nb=int(Nb)
    return Nb

#Empêche d'écrire du caractère uniquement des nombres

def isCarac(Car:str)->bool:
    while Car.isnumeric()==True: Car=input("Saisissez une phrase sans nombre : ")
    Car=str(Car)
    return Car



