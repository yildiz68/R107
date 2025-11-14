valeur = int(input("saisissez votre valeur"))
nombre = 0
N = 1
while (valeur - nombre) > 0:
    valeur -= nombre
    nombre = nombre + nombre + 1
    N = N + 1
print("le nombre N est :",N,)