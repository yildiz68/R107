nbinf10 = 0
nb1015 = 0
nbsup15 = 0
for i in range(10):
    valeur = int(input("entrez une valeur entre 0 et 20 : "))
    while valeur > 20 or valeur < 0:
        valeur = int(input("entrez une valeur entre 0 et 20 : "))
    if valeur < 10:
            nbinf10 = nbinf10 + 1
    elif 10 <= valeur and valeur >15:
            nb1015 = nb1015 + 1
    else :
         nbsup15 = nbsup15 + 1
print("le nombre de valeur inférieur a 10 est :",nbinf10,
                "\n le nombre de valeur entre 10 et 15 est : ",nb1015,
                "\n le nombre de valeur supérieur a 15 est : ",nbsup15,)

