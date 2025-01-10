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
# day_label.pack()cls

# date_label = Label(window,font=("Ink Free",30))
# date_label.pack()

# update()

# window.mainloop()
# -------------------------- end first try --------------
# ----------------beginning program ok but french --------------------

# import time
# from threading import Thread
# from os import system

# # Variables globales pour l'heure et l'alarme
# heure_actuelle = (0, 0, 0)
# alarme = None
# horloge_en_marche = True
# mode_24h = True
# pause = False

# # Fonction pour afficher l'heure
# def afficher_heure():
#     heures, minutes, secondes = heure_actuelle
#     if not mode_24h:
#         suffixe = "AM" if heures < 12 else "PM"
#         heures = heures % 12 or 12
#         return f"{heures:02}:{minutes:02}:{secondes:02} {suffixe}"
#     return f"{heures:02}:{minutes:02}:{secondes:02}"

# # Fonction pour régler l'heure
# def regler_heure():
#     global heure_actuelle, horloge_en_marche
#     horloge_en_marche = False
#     try:
#         heures = int(input("Heures (0-23) : "))
#         minutes = int(input("Minutes (0-59) : "))
#         secondes = int(input("Secondes (0-59) : "))
#         if 0 <= heures < 24 and 0 <= minutes < 60 and 0 <= secondes < 60:
#             heure_actuelle = (heures, minutes, secondes)
#         else:
#             print("Valeurs invalides.")
#     except ValueError:
#         print("Entrée invalide.")
#     horloge_en_marche = True

# # Fonction pour régler l'alarme
# def regler_alarme():
#     global alarme
#     try:
#         heures = int(input("Heures de l'alarme (0-23) : "))
#         minutes = int(input("Minutes de l'alarme (0-59) : "))
#         secondes = int(input("Secondes de l'alarme (0-59) : "))
#         if 0 <= heures < 24 and 0 <= minutes < 60 and 0 <= secondes < 60:
#             alarme = (heures, minutes, secondes)
#             print(f"Alarme réglée à {heures:02}:{minutes:02}:{secondes:02}")
#         else:
#             print("Valeurs invalides.")
#     except ValueError:
#         print("Entrée invalide.")

# # Fonction pour mettre l'horloge en pause
# def mettre_en_pause():
#     global pause
#     pause = True

# # Fonction pour redémarrer l'horloge après la pause
# def redemarrer_horloge():
#     global pause
#     pause = False

# # Fonction principale pour mettre à jour l'heure chaque seconde
# def horloge():
#     global heure_actuelle, horloge_en_marche, pause
#     while True:
#         if horloge_en_marche and not pause:
#             heures, minutes, secondes = heure_actuelle
#             secondes += 1
#             if secondes == 60:
#                 secondes = 0
#                 minutes += 1
#             if minutes == 60:
#                 minutes = 0
#                 heures += 1
#             if heures == 24:
#                 heures = 0
#             heure_actuelle = (heures, minutes, secondes)
#             if alarme == heure_actuelle:
#                 print("\nAlarme ! L'heure actuelle correspond à l'heure de l'alarme !")
#         time.sleep(1)

# # Lancement de l'horloge dans un thread séparé
# if __name__ == "__main__":
#     thread_horloge = Thread(target=horloge, daemon=True)
#     thread_horloge.start()

#     while True:
#         system("cls" if system == "nt" else "clear")
#         print(f"Heure actuelle : {afficher_heure()}\n")
#         print("Menu :")
#         print("1- Régler l'heure")
#         print("2- Régler l'alarme")
#         print("3- Basculer mode 12h/24h")
#         print("4- Mettre en pause")
#         print("5- Redémarrer l'horloge")
#         print("6- Quitter")
#         choix = input("Choisissez une option : ")

#         if choix == "1":
#             regler_heure()
#         elif choix == "2":
#             regler_alarme()
#         elif choix == "3":
#             mode_24h = not mode_24h
#         elif choix == "4":
#             mettre_en_pause()
#         elif choix == "5":
#             redemarrer_horloge()
#         elif choix == "6":
#             break
#         else:
#             print("Option invalide.")

#         time.sleep(1)


# --------------fin programm ok but french --------------
# ----------begining programm ok and english ------------

import time
from threading import Thread
from os import system

# Global variables for the clock and alarm
current_time = (0, 0, 0)
alarm = None
clock_running = True
mode_24h = True
paused = False

# Function to display the current time
def display_time():
    hours, minutes, seconds = current_time
    if not mode_24h:
        suffix = "AM" if hours < 12 else "PM"
        hours = hours % 12 or 12
        return f"{hours:02}:{minutes:02}:{seconds:02} {suffix}"
    return f"{hours:02}:{minutes:02}:{seconds:02}"

# Function to set the time
def set_time():
    global current_time, clock_running
    clock_running = False
    try:
        hours = int(input("Hours (0-23): "))
        minutes = int(input("Minutes (0-59): "))
        seconds = int(input("Seconds (0-59): "))
        if 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60:
            current_time = (hours, minutes, seconds)
        else:
            print("Invalid values.")
    except ValueError:
        print("Invalid input.")
    clock_running = True

# Function to set the alarm
def set_alarm():
    global alarm
    try:
        hours = int(input("Alarm hours (0-23): "))
        minutes = int(input("Alarm minutes (0-59): "))
        seconds = int(input("Alarm seconds (0-59): "))
        if 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60:
            alarm = (hours, minutes, seconds)
            print(f"Alarm set for {hours:02}:{minutes:02}:{seconds:02}")
        else:
            print("Invalid values.")
    except ValueError:
        print("Invalid input.")

# Function to pause the clock
def pause_clock():
    global paused
    paused = True

# Function to resume the clock after pause
def resume_clock():
    global paused
    paused = False

# Main function to update the time every second
def clock():
    global current_time, clock_running, paused
    while True:
        if clock_running and not paused:
            hours, minutes, seconds = current_time
            seconds += 1
            if seconds == 60:
                seconds = 0
                minutes += 1
            if minutes == 60:
                minutes = 0
                hours += 1
            if hours == 24:
                hours = 0
            current_time = (hours, minutes, seconds)
            if alarm == current_time:
                print("\nAlarm! The current time matches the alarm time!")
        time.sleep(1)

# Start the clock in a separate thread
if __name__ == "__main__":
    clock_thread = Thread(target=clock, daemon=True)
    clock_thread.start()

    while True:
        system("cls" if system == "nt" else "clear")
        print(f"Current time: {display_time()}\n")
        print("Menu:")
        print("1- Set time")
        print("2- Set alarm")
        print("3- Toggle 12h/24h mode")
        print("4- Pause clock")
        print("5- Resume clock")
        print("6- Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            set_time()
        elif choice == "2":
            set_alarm()
        elif choice == "3":
            mode_24h = not mode_24h
        elif choice == "4":
            pause_clock()
        elif choice == "5":
            resume_clock()
        elif choice == "6":
            break
        else:
            print("Invalid option.")

        time.sleep(1)


# -----------end programm ok and english ---------------