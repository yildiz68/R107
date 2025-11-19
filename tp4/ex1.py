reel = float(input("Vous cherchez la table de multiplication de quelle nombre"))
tab = []
for i in range(10):
    tab.append(reel*i)

print("resu : ",tab)
for i in range(10):
    print(reel , "* ",i , " = ",tab[i],"\n")