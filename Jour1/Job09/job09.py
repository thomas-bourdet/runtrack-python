nom="Briquet"
prix_unitaire=2
quantité_en_stock=100

print(nom)
print(f"{prix_unitaire}€")
print(quantité_en_stock)

quant_aj=int(input("Entrée la quantité de produit que vous voulez ajouter au stock :"))
quantité_en_stock +=quant_aj
print(quantité_en_stock)

quant_achat=int(input("Entrée la quantité de produit que vous voulez acheter :"))

quantité_en_stock -=quant_achat

print(quantité_en_stock)

prix_unitaire *=1.10

print(nom)
print(prix_unitaire)
print(quantité_en_stock)