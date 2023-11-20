var1=1000
var2=2
var3=(var1*var2/100)

print(f"Montant initial de l'investissement: {var1}€")
print(f"Taux de rendement annuel: {var2}%")
print(f"Gain annuel: {var3}€")

var4=int(input("Somme a ajouter en €: "))

var1 +=var4

if var4>=5000:
	var2+=2
	var3=(var1*var2/100)

print(f"Montant initial de l'investissement: {var1}€")
print(f"Taux de rendement annuel: {var2}%")
print(f"Gain annuel: {var3}€")

var5=int(input("Pourcentage a soustraire du montant total: "))

if var5==10:
	var1*=0.90
	var2-=1
	var3=(var1*var2/100)

print(f"Montant initial de l'investissement: {var1}€")
print(f"Taux de rendement annuel: {var2}%")
print(f"Gain annuel: {var3}€")