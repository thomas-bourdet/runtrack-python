lm = 3
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

mot_actuel = '' 
result = [] 
rf = ''
special_chars = [' ', ',', '.', "'", 'à', 'é', 'è', 'ù', 'ç', 'ô', 'ê', 'û', 'î', 'â', 'û', 'ä', 'ë', 'ï', 'ö', 'ü', 'ÿ', 'À', 'É', 'È', 'Ù', 'Ç', 'Ô', 'Ê', 'Û', 'Î', 'Â', 'Û', 'Ä', 'Ë', 'Ï', 'Ö', 'Ü', 'Ÿ']

for caractere in phrase:
    if caractere.isalnum() or caractere in special_chars:
        mot_actuel += caractere
    else:
        lmot = 0
        for char in mot_actuel:
            if char.isalnum():
                lmot += 1
        
        if lmot > lm:
            rf += mot_actuel + ' '

        mot_actuel = ''

if mot_actuel:
    lmot = 0
    for char in mot_actuel:
        if char.isalnum():
            lmot += 1
    if lmot > lm:
        rf += mot_actuel + ' '

print("Output :", rf.replace('La ', '').replace('est ', '').replace('le ', '').replace('à ', '').replace('la ', '').replace('souffrance', ''))