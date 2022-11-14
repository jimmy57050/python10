tab = [5,9,8,3,2,7]

n = len(tab)

for i in range(0,len(tab)):
    minimum = tab[i]
    i_min = i

    for j in range(i,n):
        if tab[j] < minimum:
            minimum = tab[j]
            i_min = j
            tmp = tab[i]
            tab[i] = minimum
            tab[i_min]=tmp
            

print (tab)

