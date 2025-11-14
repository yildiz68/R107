BASE = int(4)
fromage = int (800)
eau = int(2)
ail = int(2)
pain = int(400)
nbConvives = int(input("le nombre de convives ?"))
fromage = 800 * nbConvives / BASE
eau = 2 * nbConvives / BASE
ail = 2 * nbConvives / BASE
pain = 400 * nbConvives / BASE
print("entrez le nombre de personne conviées à la fondue :",nbConvives,
      "pour faire une fondue fribourgeoise pour",nbConvives, "personnes, il vous faut :",
      fromage,"gr de fromage"
      ,eau,"dl d'eau"
      ,ail,"gousse(s) d'ail"
      ,pain,"gr de pain")


