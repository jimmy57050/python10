mot1 = input("Saisir un premier mot: ").upper().replace(" ", "")      # .replace ( pour remplacer )
while mot1.isnumeric()==True :                                        # .upper ( pour mettre tout en maj)
    mot1 = input("Veuillez saisir un mot ")                           # .lower (en miniscule)
mot2 = input("Saisir un deuxième mot: ").upper().replace(" ","")
while mot2.isnumeric()==True :
    mot2 = input("Veuillez saisir un mot ")             # on rentre nos mots

tab1 = [] 
tab2 = []                                               # on crée nos 2 tableaux

for i in range(len(mot1)):     
    if mot1[i] != " ":                                 
        tab1 += mot1 

for j in range(len(mot2)):                              # on rentre nos mots dans les tableaux 
    if mot2[j] !=  " ":         
        tab2 += mot2   

if len(tab1) == len(tab2):    
    for i in range(len(tab1)):         
        for j in range(len(tab2)):             
            if tab1[i] == tab2[j]:         
                tab1[i]= " * "              
                tab2[j]= " * "               
            
if tab2 == tab1:    
    print("anagramme")
else:     
    print("pas anagramme")
