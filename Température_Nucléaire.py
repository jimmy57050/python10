ambiante = int(input("Température ambiante. "))
refroidissement = int(input("Température du bassin . "))

if ambiante < refroidissement :
    t= refroidissement-ambiante
elif ambiante>refroidissement : 
    t=ambiante-refroidissement
if  t<=20 :
    print("alarme")
elif t>=40 : 
    print ("alarme")
else : 
    print ("Tout va bien")


    