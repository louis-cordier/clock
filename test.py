# Premier test -------------------------------------#
import time
from datetime import datetime

while True:
    # Obtain current hour
    c = datetime.now()
    
    # Setting current time
    current_time = c.strftime('%H:%M:%S')
    
    # Erase previous message onboard for clearer display in terminal 
    print('\rCurrent Time is:', current_time, end='')
    
    # Wait a second before reload
    time.sleep(1)
#-----------------------------------------------#

#-------------deuxième test --------------------
# import time

# def afficher_heure(heure):
#     """
#     Met à jour et affiche l'heure sous la forme hh:mm:ss

#     :param heure: tuple contenant l'heure sous la forme (heures, minutes, secondes)
#     """
#     global heures, minutes, secondes

#     heures, minutes, secondes = heure

# # Initialisation de l'heure par défaut
# heures, minutes, secondes = 0, 0, 0

# try:
#     while True:
#         # Affiche l'heure sous le format hh:mm:ss
#         print(f"{heures:02}:{minutes:02}:{secondes:02}")
        
#         # Attendre une seconde avant d'actualiser
#         time.sleep(1)

#         # Incrémenter les secondes
#         secondes += 1
#         if secondes == 60:
#             secondes = 0
#             minutes += 1
#         if minutes == 60:
#             minutes = 0
#             heures += 1
#         if heures == 24:
#             heures = 0

# except KeyboardInterrupt:
#     print("\nProgramme arrêté par l'utilisateur.")

# -------------fin deuxième test ---------------------------

# -------------début 3ème test ----------------

# import time
# from threading import Thread

# # Variables globales pour l'heure et l'alarme
# heure_actuelle = (0, 0, 0)
# alarme = None

# # Fonction pour afficher l'heure
# def afficher_heure():
#     global heure_actuelle
#     while True:
#         # Formater et afficher l'heure
#         print(f"{heure_actuelle[0]:02}:{heure_actuelle[1]:02}:{heure_actuelle[2]:02}", end="\r")
#         time.sleep(1)
#         incrementer_heure()

# # Fonction pour mettre à jour l'heure
# def regler_heure(nouvelle_heure):
#     global heure_actuelle
#     if verifier_heure_valide(nouvelle_heure):
#         heure_actuelle = nouvelle_heure

# # Fonction pour incrémenter l'heure chaque seconde
# def incrementer_heure():
#     global heure_actuelle
#     heures, minutes, secondes = heure_actuelle
#     secondes += 1
#     if secondes >= 60:
#         secondes = 0
#         minutes += 1
#     if minutes >= 60:
#         minutes = 0
#         heures += 1
#     if heures >= 24:
#         heures = 0
#     heure_actuelle = (heures, minutes, secondes)
#     verifier_alarme()

# # Fonction pour vérifier et afficher un message si l'heure correspond à l'alarme
# def verifier_alarme():
#     global heure_actuelle, alarme
#     if alarme and heure_actuelle == alarme:
#         print("\n\u23F0 Alarme ! Il est l'heure !")
#         alarme = None  # Désactiver l'alarme après qu'elle ait sonné

# # Fonction pour régler l'alarme
# def regler_alarme(heure_alarme):
#     global alarme
#     if verifier_heure_valide(heure_alarme):
#         alarme = heure_alarme
#         print(f"\u23F0 Alarme réglée pour {heure_alarme[0]:02}:{heure_alarme[1]:02}:{heure_alarme[2]:02}")

# # Fonction pour vérifier si une heure est valide
# def verifier_heure_valide(heure):
#     if not (0 <= heure[0] < 24):
#         print("Heure invalide : Les heures doivent être entre 0 et 23.")
#         return False
#     if not (0 <= heure[1] < 60):
#         print("Heure invalide : Les minutes doivent être entre 0 et 59.")
#         return False
#     if not (0 <= heure[2] < 60):
#         print("Heure invalide : Les secondes doivent être entre 0 et 59.")
#         return False
#     return True

# # Lancer l'affichage de l'heure dans un thread séparé
# affichage_thread = Thread(target=afficher_heure)
# affichage_thread.daemon = True
# affichage_thread.start()

# # Fonction pour afficher les options du menu
# def afficher_menu():
#     print("\nOptions :")
#     print("1. Régler l'heure")
#     print("2. Régler l'alarme")
#     print("3. Quitter")

# # Exemple d'utilisation
# if __name__ == "__main__":
#     print("\nBienvenue dans l'horloge interactive !")
#     regler_heure((16, 30, 0))
#     regler_alarme((16, 30, 10))

#     while True:
#         afficher_menu()
#         choix = input("Choisissez une option : ")

#         if choix == "1":
#             heure_str = input("Entrez l'heure (hh:mm:ss) : ")
#             try:
#                 if ":" not in heure_str:
#                     raise ValueError("Le format de l'heure est incorrect. Assurez-vous d'utiliser hh:mm:ss.")
#                 heures, minutes, secondes = map(int, heure_str.split(":"))
#                 regler_heure((heures, minutes, secondes))
#             except ValueError as e:
#                 print(f"Erreur : {e}")
#         elif choix == "2":
#             alarme_str = input("Entrez l'heure de l'alarme (hh:mm:ss) : ")
#             try:
#                 if ":" not in alarme_str:
#                     raise ValueError("Le format de l'heure est incorrect. Assurez-vous d'utiliser hh:mm:ss.")
#                 heures, minutes, secondes = map(int, alarme_str.split(":"))
#                 regler_alarme((heures, minutes, secondes))
#             except ValueError as e:
#                 print(f"Erreur : {e}")
#         elif choix == "3":
#             print("\nAu revoir !")
#             break
#         else:
#             print("Option invalide. Veuillez choisir à nouveau.")


# --------- fin troisième test ----------------------------------#