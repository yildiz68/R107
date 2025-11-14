nbinf10 = 0
nb1015 = 0
nbsup15 = 0
for i in range(10):
    valeur = int(input("entrez une valeur entre 0 et 20 : "))
    while valeur > 20 or valeur < 0:
        valeur = int(input("entrez une valeur entre 0 et 20 : "))
