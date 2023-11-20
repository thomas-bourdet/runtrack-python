#subprocess utiliser afin de montré que les jobs 1 et 2 fonctionne tout en ayant uniquement a run le job 3
import subprocess
import os

#Défini le chemin du script actuel
current_directory = os.path.dirname(os.path.abspath(__file__))

#Défini le chemin des différents scripts
script1_path = os.path.join(current_directory, "..", "Job01", "job01.py")
script2_path = os.path.join(current_directory, "..", "Job02", "main.py")

#Run job01.py et récupere le résultat
result_job01 = subprocess.run(["python", script1_path], stdout=subprocess.PIPE, text=True)

#Run main.py et récupere le résultat
result_job02 = subprocess.run(["python", script2_path], stdout=subprocess.PIPE, text=True)


print("Result from job01.py:")
print(result_job01.stdout)

print("\nResult from job02.py:")
print(result_job02.stdout)
