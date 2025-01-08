# from tkinter import *
# from time import *

# def update():
#     time_string = strftime("%I:%M:%S %p")
#     time_label.config(text=time_string)

#     day_string = strftime("%A")
#     day_label.config(text=day_string)

#     date_string = strftime("%B %d, %Y")
#     date_label.config(text=date_string)

#     window.after(1000,update)


# window = Tk()

# time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
# time_label.pack()

# day_label = Label(window,font=("Ink Free",25,"bold"))
# day_label.pack()

# date_label = Label(window,font=("Ink Free",30))
# date_label.pack()

# update()

# window.mainloop()

import time
from threading import Thread
from os import system

# Variables globales pour l'heure et l'alarme
heure_actuelle = (0, 0, 0)
alarme = None
horloge_en_marche = True
mode_24h = True
pause = False

# Fonction pour afficher l'heure
def afficher_heure():
    heures, minutes, secondes = heure_actuelle
    if not mode_24h:
        suffixe = "AM" if heures < 12 else "PM"
        heures = heures % 12 or 12
        return f"{heures:02}:{minutes:02}:{secondes:02} {suffixe}"
    return f"{heures:02}:{minutes:02}:{secondes:02}"

# Fonction pour régler l'heure
def regler_heure():
    global heure_actuelle, horloge_en_marche
    horloge_en_marche = False
    try:
        heures = int(input("Heures (0-23) : "))
        minutes = int(input("Minutes (0-59) : "))
        secondes = int(input("Secondes (0-59) : "))
        if 0 <= heures < 24 and 0 <= minutes < 60 and 0 <= secondes < 60:
            heure_actuelle = (heures, minutes, secondes)
        else:
            print("Valeurs invalides.")
    except ValueError:
        print("Entrée invalide.")
    horloge_en_marche = True

# Fonction pour régler l'alarme
def regler_alarme():
    global alarme
    try:
        heures = int(input("Heures de l'alarme (0-23) : "))
        minutes = int(input("Minutes de l'alarme (0-59) : "))
        secondes = int(input("Secondes de l'alarme (0-59) : "))
        if 0 <= heures < 24 and 0 <= minutes < 60 and 0 <= secondes < 60:
            alarme = (heures, minutes, secondes)
            print(f"Alarme réglée à {heures:02}:{minutes:02}:{secondes:02}")
        else:
            print("Valeurs invalides.")
    except ValueError:
        print("Entrée invalide.")

# Fonction pour mettre l'horloge en pause
def mettre_en_pause():
    global pause
    pause = True

# Fonction pour redémarrer l'horloge après la pause
def redemarrer_horloge():
    global pause
    pause = False

# Fonction principale pour mettre à jour l'heure chaque seconde
def horloge():
    global heure_actuelle, horloge_en_marche, pause
    while True:
        if horloge_en_marche and not pause:
            heures, minutes, secondes = heure_actuelle
            secondes += 1
            if secondes == 60:
                secondes = 0
                minutes += 1
            if minutes == 60:
                minutes = 0
                heures += 1
            if heures == 24:
                heures = 0
            heure_actuelle = (heures, minutes, secondes)
            if alarme == heure_actuelle:
                print("\nAlarme ! L'heure actuelle correspond à l'heure de l'alarme !")
        time.sleep(1)

# Lancement de l'horloge dans un thread séparé
if __name__ == "__main__":
    thread_horloge = Thread(target=horloge, daemon=True)
    thread_horloge.start()

    while True:
        system("cls" if system == "nt" else "clear")
        print(f"Heure actuelle : {afficher_heure()}\n")
        print("Menu :")
        print("1- Régler l'heure")
        print("2- Régler l'alarme")
        print("3- Basculer mode 12h/24h")
        print("4- Mettre en pause")
        print("5- Redémarrer l'horloge")
        print("6- Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            regler_heure()
        elif choix == "2":
            regler_alarme()
        elif choix == "3":
            mode_24h = not mode_24h
        elif choix == "4":
            mettre_en_pause()
        elif choix == "5":
            redemarrer_horloge()
        elif choix == "6":
            break
        else:
            print("Option invalide.")

        time.sleep(1)
