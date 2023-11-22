def check(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            return f"{nombre} est un nombre pair."
        else:
            return f"{nombre} est un nombre impair."
    else:
        return "Veuillez fournir un nombre entier positif."

t1 = check(100)
t2 = check(55)
t3 = check(5.5)

print(t1)
print(t2)
print(t3)

