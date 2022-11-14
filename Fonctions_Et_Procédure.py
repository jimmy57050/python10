def maFonction() :
    print("hello")

def maFonction2():
   return "cc"

maFonction()
res = maFonction2()
print (res)


def sum(a,b):
    return a +b


res2 = sum(2,5)
print(res2)

res3 = sum(9,9)
print (res3)

print(sum(5,5))              # on peux print diréctement une fonction


def isGood (moy:float)->bool:
    "verifie si un élève est bon"
    if moy >16:
        return True
    else :
        return False



# exemple : trouver un nombre paire ou impaire.

cc=int(input('veuillez saisir le chiffre:  '))

def test(cc):
    """
    Vérifie si le nombre est paire ou impaire.
    """
    
    if cc % 2 == 0:
        return True     
    else :
        return False

if test(cc) :
    print ('paire')
else :
    print ('impaire')


