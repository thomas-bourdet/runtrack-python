a = int(input("Veuillez entrer un chiffre : "))
b = input("Veuillez entrer l'opération que vous souhaitez réaliser (+, -, *, /) : ")
c = int(input("Veuillez entrer un autre chiffre : "))

def calcule():
    if b == "+":
        print(a + c)
    elif b == "-":
        print(a - c)
    elif b == "*":
        print(a * c)
    elif b == "/":
        if c != 0:  
            print(a / c)
        else:
            print("Erreur : Division par zéro.")

calcule()
