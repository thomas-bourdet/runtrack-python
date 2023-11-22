def fonction(nombre):
    if nombre <= 0:
        print(f"Le nombre {nombre} est négatif")
    else:
        print(f"Le nombre {nombre} est positif")

input = int(input("Veuillez entrer un nombre : "))
fonction(input)
