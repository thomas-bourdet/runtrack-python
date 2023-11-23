def tri(liste):
    if not liste:
        return liste

    pivot = liste[0]
    inferieurs = [x for x in liste[1:] if x <= pivot]
    superieurs = [x for x in liste[1:] if x > pivot]

    return tri(inferieurs) + [pivot] + tri(superieurs)

L = [9, 75, 35, 49, 3, 16, 17, 12, 62, 90]

listri= tri(L)

print(listri)
