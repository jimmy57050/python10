tab=[10,15,21,26,34,46,58,64,99]
elem=21
deb=0
fin=len(tab)-1
m=(deb+fin)//2
trouve=False
while deb<=fin:
    if tab[m]==elem:
        trouve=True
        break
    elif tab[m]>elem:
        fin=m-1
    else:
        deb=m+1
    m=(deb+fin)//2
if trouve:
    print('L\'indice de d\'élement recherché est '+str(m))
else:
    print('Elément introuvable')