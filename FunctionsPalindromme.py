def is_palindrome(a):               #on parcourt la moitié de la chaîne de caractères “a”. Ici, “len(a) désigne
    for i in range(len(a)//2):      # la longueur de la chaîne, et len(a)//2 représente le quotient de la division 
        if a[i] != a[-i-1]:         # euclidienne de cette longueur par 2.
            return False            # Ainsi, si “a” a une longueur impaire, on s’arrête au caractère juste avant celui du milieu;
        return True
                                    # dans la boucle for, on teste si le caractère de rang i est différent du caractère de rang –i-1.
car = {                             # Il faut ici faire attention au fait que, par exemple, a[0] représente le 1er caractère alors que a[-1] représente le dernier, d’où le décalage
    "à" : "a",                      # on ne marque pas a[-i] mais a[-i-1].
    "ä" : "a",                      # Si les caractères sont différents alors la chaîne n’est pas un palindrome.
    "â" : "a",                      # On retourne donc False, ce qui stoppe la boucle;
    "ç" : "c",                      # on finit par retourner True si False n’a pas été retourné.
    "é" : "e",
    "è" : "e",
    "ë" : "e",                      
    "ï" : "i",
    "ô" : "o",
    "ù" : "u",
    "ü" : "u",                      # Ici on supprime tout les caractères spéciaux pour ne pas avoir d'erreurs.
    "û" : "u",
    " " : "",
    "-" : "",
    "," : "",
    "'" : "",
    "?" : "",
    "!" : "",
    "." : ""
}

def lowerCaps(a):                           # Ici on crée une fonction qui se charge de tout mettre en minuscules 
    a = a.lower()                           # et d'effectuer les changements de caractère 
    for cle,valeur in car.items():
        a = a.replace(cle,valeur)
    return a 


