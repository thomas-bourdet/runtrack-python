def my_long_word(lm, chaine):
    mot_actuel = '' 
    result = [] 

    for caractere in chaine:
        if caractere.isalpha() or caractere == chaine[-1]:
            mot_actuel += caractere
        else:
            lmot = 0
            for _ in mot_actuel:
                lmot += 1
            
            if lmot > lm:
                result.append(mot_actuel)

            mot_actuel = ''

    rf = ' '.join(result)
    
    return rf

lm = 3
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

resultat = my_long_word(lm, phrase)
print("Output :", resultat)