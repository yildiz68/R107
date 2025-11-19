l=[]
ecart = []
somme = 0
nombre = int(input("donnez le nombre d'étudiant"))
for i in range(nombre):
    note = int(input("saisissez la note de l'élève"))
    l.append(note)
    somme = somme + l[i]
moy = somme/nombre
for i in range (nombre) :
    ecart.append(l[i] - moy)
for i in range (nombre):
    print("Note étudiant ",i,": ",l[i])
print("Moyenne de la classe :", moy,"\nNuméro de l’Etudiant | note | ecart a la moyenne"
 )
for i in range(nombre):
    print(i," |",l[i]," |",ecart[i])