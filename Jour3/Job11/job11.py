def time_to_text(minutes):
    if not isinstance(minutes, int) or minutes < 0:
        print("Veuillez fournir un nombre entier positif.")
        return

    heures = minutes // 60 
    minutes_restantes = minutes % 60 

    heures_str = "heure" if heures == 1 else "heures"
    minutes_str = "minute" if minutes_restantes == 1 else "minutes"

    print(f"{heures} {heures_str} et {minutes_restantes} {minutes_str}.")

time_to_text(126)
time_to_text(75)
time_to_text(280)