lm = 3
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

mot_actuel = '' 
result = [] 
rf = ''

for caractere in phrase:
    if ('a' <= caractere <= 'z' or 'A' <= caractere <= 'Z') or ('0' <= caractere <= '9') or caractere in [' ', ',', '.', "'", 'à', 'é', 'è', 'ù', 'ç', 'ô', 'ê', 'û', 'î', 'â', 'û', 'ä', 'ë', 'ï', 'ö', 'ü', 'ÿ', 'À', 'É', 'È', 'Ù', 'Ç', 'Ô', 'Ê', 'Û', 'Î', 'Â', 'Û', 'Ä', 'Ë', 'Ï', 'Ö', 'Ü', 'Ÿ']:
        mot_actuel += caractere
    else:
        lmot = 0
        for _ in mot_actuel:
            if ('a' <= _ <= 'z' or 'A' <= _ <= 'Z') or ('0' <= _ <= '9') or _ in ['à', 'é', 'è', 'ù', 'ç', 'ô', 'ê', 'û', 'î', 'â', 'û', 'ä', 'ë', 'ï', 'ö', 'ü', 'ÿ', 'À', 'É', 'È', 'Ù', 'Ç', 'Ô', 'Ê', 'Û', 'Î', 'Â', 'Û', 'Ä', 'Ë', 'Ï', 'Ö', 'Ü', 'Ÿ']:
                lmot += 1
        
        if lmot > lm:
            rf += mot_actuel + ' '

        mot_actuel = ''

print("Output :", rf)