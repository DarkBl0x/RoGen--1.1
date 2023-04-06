import random
import string
import tkinter as tk
from tkinter import ttk

def generate_random_string():
    """Génère une chaîne de 15 caractères aléatoires (lettres majuscules et chiffres)
    et l'insère un tiret toutes les 5 caractères."""
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
    formatted_string = '-'.join([random_string[i:i+5] for i in range(0, len(random_string), 5)])
    return formatted_string

def generate_button_clicked():
    """Fonction appelée lorsque le bouton est cliqué."""
    random_string = generate_random_string()
    result_label.configure(text=random_string)

# Crée une fenêtre principale
root = tk.Tk()
root.title("RoGen v1.1")
root.geometry("400x200")

# Utilise un style de thème ttk
style = ttk.Style(root)
style.theme_use("clam")

# Crée un cadre pour contenir le bouton et l'étiquette de résultat
frame = ttk.Frame(root, padding=20)
frame.pack(fill=tk.BOTH, expand=True)

# Crée le bouton de génération de phrase
generate_button = ttk.Button(frame, text="Générer", command=generate_button_clicked)
generate_button.pack(pady=10)

# Crée l'étiquette de résultat initial
result_label = ttk.Label(frame, text="Appuyez sur le bouton pour générer un code.", font=("Arial", 16))
result_label.pack(pady=20)

# Lance la boucle principale de la fenêtre
root.mainloop()
