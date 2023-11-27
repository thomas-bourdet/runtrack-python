def arrondir_notes(liste_notes):
    notes_arrondies = []

    for note in liste_notes:
        if note < 40:
            # Échec, la note reste inchangée
            notes_arrondies.append(note)
        else:
            # Réussite, arrondir à la hausse si nécessaire
            difference = 5 - (note % 5)  # Calcul de la différence par rapport au prochain multiple de 5
            if difference < 3:
                note_arrondie = note + difference
            else:
                note_arrondie = note

            notes_arrondies.append(note_arrondie)

    return notes_arrondies

# Exemple d'utilisation
liste_notes = [37, 54, 82, 65, 28, 43, 73, 91]
notes_arrondies = arrondir_notes(liste_notes)

# Affichage du résultat
print("Notes d'origine :", liste_notes)
print("Notes arrondies :", notes_arrondies)