def FruitLegume(type,saison):
    if type == "fruit" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruit" and saison == "ete":
        print("poire, fraise et cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")
    else: print("valeurs non conforme")

FruitLegume("fruit","hiver")
FruitLegume("fruit","ete")
FruitLegume("legume","hiver")
FruitLegume("legume","ete")
FruitLegume("legume","fruit")