a = float(input("Veuillez saisir votre première note :"))
b = float(input("Veuillez saisir votre deuxième note :"))
c = float(input("Veuillez saisir votre troisième note :"))

def moyenne(a,b,c):
    moyenne_etudiant = (a+b+c)/3
    if moyenne_etudiant >= 15 and moyenne_etudiant <= 20:
        print(f"{moyenne_etudiant} Très bon élève")
        return moyenne_etudiant
    
    elif moyenne_etudiant >= 11 and moyenne_etudiant <= 14:
        print(f"{moyenne_etudiant} Bon élève")
        return moyenne_etudiant
    
    elif moyenne_etudiant >= 8 and moyenne_etudiant <= 10:
        print(f"{moyenne_etudiant} Elève moyen")
        return moyenne_etudiant
    
    elif moyenne_etudiant >= 0 and moyenne_etudiant <= 7:
        print(f"{moyenne_etudiant} Elève devant faire des efforts")
        return moyenne_etudiant
    else: print("Moyenne comprise hors des plages spécifées")
    
moyenne(a,b,c)