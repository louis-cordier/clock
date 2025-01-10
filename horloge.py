import time
import threading
from datetime import datetime, timedelta
import os
import msvcrt  # Pour gérer les entrées non bloquantes sur Windows


class HorlogeMaman:
    def __init__(self):
        self.heure_actuelle = datetime.now()
        self.heure_alarme = None
        self.est_en_cours = True
        self.est_mode_24h = True

    # Méthode principale pour exécuter l'horloge
    def executer_horloge(self):
        while self.est_en_cours:
            self.heure_actuelle += timedelta(seconds=1)
            self.verifier_alarme()
            time.sleep(1)

    # Méthode pour afficher l'heure
    def afficher_heure(self):
        while True:
            self.effacer_ecran()
            if self.est_mode_24h:
                print(self.heure_actuelle.strftime("%H:%M:%S"))
            else:
                print(self.heure_actuelle.strftime("%I:%M:%S %p"))
            print("Appuyez sur une touche pour accéder au menu.")

            if msvcrt.kbhit():  # Vérifie si une touche a été appuyée
                msvcrt.getch()
                break

    # Méthode pour régler l'heure
    def regler_heure(self, tuple_heure):
        heures, minutes, secondes = tuple_heure
        self.heure_actuelle = self.heure_actuelle.replace(hour=heures, minute=minutes, second=secondes)
        self.effacer_ecran()
        print(f"L'heure a été réglée sur {self.heure_actuelle.strftime('%H:%M:%S')}")
        print("Appuyez sur Ctrl+C pour revenir.")
        try:
            while True:
                pass
        except KeyboardInterrupt:
            pass

    # Méthode pour régler l'alarme
    def regler_alarme(self, tuple_alarme):
        heures, minutes, secondes = tuple_alarme
        self.heure_alarme = self.heure_actuelle.replace(hour=heures, minute=minutes, second=secondes)
        self.effacer_ecran()
        print(f"L'alarme a été réglée pour {self.heure_alarme.strftime('%H:%M:%S')}")
        print("Appuyez sur Ctrl+C pour revenir.")
        try:
            while True:
                pass
        except KeyboardInterrupt:
            pass

    # Méthode pour vérifier l'alarme
    def verifier_alarme(self):
        if self.heure_alarme and self.heure_actuelle == self.heure_alarme:
            print("\n\n⏰ ALARME! Il est temps de se réveiller! ⏰")
            self.heure_alarme = None

    # Méthode pour changer le mode d'affichage de l'heure
    def changer_mode_heure(self):
        self.est_mode_24h = not self.est_mode_24h
        mode = "24 heures" if self.est_mode_24h else "12 heures AM/PM"
        self.effacer_ecran()
        print(f"Le format de l'heure a été changé en mode {mode}.")
        print("Appuyez sur Ctrl+C pour revenir.")
        try:
            while True:
                pass
        except KeyboardInterrupt:
            pass

    # Méthode pour effacer l'écran
    def effacer_ecran(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    # Méthode pour arrêter l'horloge
    def arreter_horloge(self):
        self.est_en_cours = False
        self.effacer_ecran()
        print("L'horloge a été arrêtée.")


# Fonction principale contenant la boucle principale et le menu
def menu():
    horloge = HorlogeMaman()
    thread_horloge = threading.Thread(target=horloge.executer_horloge)
    thread_horloge.daemon = True
    thread_horloge.start()

    while True:
        horloge.afficher_heure()
        horloge.effacer_ecran()
        print("\n\n--- Menu ---")
        print("1. Afficher l'heure")
        print("2. Régler l'heure")
        print("3. Régler l'alarme")
        print("4. Changer le format de l'heure")
        print("5. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == '1':
            horloge.afficher_heure()
        elif choix == '2':
            temps = tuple(map(int, input("Entrez l'heure (hh mm ss) : ").split()))
            horloge.regler_heure(temps)
        elif choix == '3':
            temps = tuple(map(int, input("Régler l'alarme pour (hh mm ss) : ").split()))
            horloge.regler_alarme(temps)
        elif choix == '4':
            horloge.changer_mode_heure()
        elif choix == '5':
            horloge.arreter_horloge()
            break  # Quitter la boucle lorsque l'horloge est arrêtée
        else:
            print("Choix incorrect. Veuillez choisir un numéro entre 1 et 5.")

    thread_horloge.join()


if __name__ == '__main__':
    menu()
