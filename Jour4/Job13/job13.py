L = [10,20,30,20,10,50,60,40,80,50,40]
L2 = []
for i in L:
    found = False
    for x in L2:
        if x == i:
            found = True
            break
    if not found:
        L2 = L2 + [i]
print(L2)