def isEven(n:int)-> bool :
    """
    Vérifie si le nombre est paire ou impaire.
    """
    
    return int(n % 2) == 0 

n = int(input('saisir un nombre: '))

nIsEvent = f"le nombre {n} est paire." if isEven(n) else f"le nombre {n} est impaire."
print (nIsEvent)


###########################################################
#################### correction ###########################
###########################################################

# fontions : 

# def isEven(n:int) -> bool :
#   """
#   Vérifie si un nombre est paire.
#   """

#  if n % 2 == 0 :                                  return int(n % 2) == 0 :
#       return True                 ou 
#  else : 
#       return False


# main 

#n = int(input('saisir un nombre: '))

#if isEven(n):                                         print (f"le nombre {n} est paire.") if isEven(n) else print(f"le nombre {n} est impaire".)
#   print(f"le nombre {n} est paire.")             ou 
#else :
#   print (f"le nombre {n} est impaire.")

#                                            ou 

# nIsEvent = f"le nombre {n} est paire." if isEven(n) else f"le nombre {n} est impaire."
#print (nIsEvent)

#def checkIfUserInputIsEvent():


def printHeader(title:str, count: int = 1 ):

 l = len(title)
 d = (l + count * 2 + 2) * '#'
 c = '#' * count
 print (d)
 print (f"{c} {title} {c}")
 print (d)
