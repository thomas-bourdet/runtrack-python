reflist = [2, 12, 21, 42, 24, 6, 18, 92, 7, 48, 3]

print("Avant :", reflist)

def tri(liste):
    n = 0

    for i in liste:
        n += 1

    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]


tri(reflist)

print("Après :", reflist)