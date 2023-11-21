a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("C'est un triangle équilatéral.")
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            print("C'est un triangle rectangle isocèle.")
        else:
            print("C'est un triangle isocèle.")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        print("C'est un triangle rectangle.")
    else:
        print("C'est un triangle quelconque.")
else:
    print("Longueurs incorrecte.")
