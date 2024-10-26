import tkinter as tk
from tkinter.messagebox import showinfo
import time
from threading import Thread

agec = tk.Tk()
agec.geometry("350x150")
agec.title("Calcul d'âge")

def show_loading():
    loading = tk.Toplevel()  # Crée une nouvelle fenêtre (Toplevel)
    loading.title("Chargement en cours...")
    loading.geometry("300x100")
    label = tk.Label(loading, text="Chargement, veuillez patienter...")
    label.pack(expand=True)
    # Ferme la fenêtre de chargement après 3 secondes
    loading.after(1500, loading.destroy)
    # Empêche l'utilisateur d'interagir avec la fenêtre principale
    loading.transient(agec)
    loading.grab_set()
    agec.wait_window(loading)

# Fonction simulant une tâche longue
def long_task():
    show_loading()  # Affiche la fenêtre de chargement
    time.sleep(1)
    res = myEntry.get()    # Simule une tâche prenant du temps
    showinfo("Calcul d'âge", f"Tu as {res} ans !")  # Message de fin de tâche

# Fonction pour exécuter la tâche dans un thread séparé
def start_task():
    # Lancer la tâche longue dans un thread pour éviter de bloquer l'interface
    thread = Thread(target=long_task)
    thread.start()
    
myLabel = tk.Label(agec, text="Entrez votre âge :", font=("Arial", 16))
myLabel.pack()

myEntry = tk.Entry(agec, width=40)
myEntry.pack(pady=20)

btn = tk.Button(agec, height=1, width=10, text="Calculer", command=long_task, fg="white", bg="red")
btn.pack()
      
agec.mainloop()