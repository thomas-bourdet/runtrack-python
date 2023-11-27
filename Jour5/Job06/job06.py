marches = int(input("Entrez le nombre de marche: "))
hauteur_marche_cm = int(input("Entrez la hauteur d'une marche en cm: "))

def calculer_distance(marches, hauteur_marche):
    hauteur_marche_m = hauteur_marche / 100

    hauteur_phare_m = marches * hauteur_marche_m

    distance_jour_m = 5 * 2 * hauteur_phare_m

    distance_semaine_m = 7 * distance_jour_m

    return distance_semaine_m

distance_semaine_m = calculer_distance(marches, hauteur_marche_cm)

print(f"Pour {marches} marches de {hauteur_marche_cm} cm, le gardien parcourt {distance_semaine_m:.2f} m par semaine.")
