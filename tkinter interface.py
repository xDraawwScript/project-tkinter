import tkinter as tk
from tkinter import messagebox

# fonction appelée lorsque le bouton est cliqué
def rechercher():
    messagebox.showinfo("configuration recommandée",...) # A FAIRE : se servir des données rentrées par l'utilisateur pour effectuer la recherche
                                                        
# créer la fenêtre principale
root = tk.Tk()
root.title("Build Master Mania")
root.minsize(600,50)

# liste déroulante pour la catégorie d'utilisation
categories = tk.StringVar(root)
categories.set("Choisissez votre utilisation")
categorie_menu = tk.OptionMenu(root, categories, "gaming", "3d", "montage")
categorie_menu.pack(side=tk.LEFT, padx=10, pady=10)

# zone de saisie du prix
nombre_label = tk.Label(root, text="Budget :")
nombre_label.pack(side=tk.LEFT, padx=10, pady=10)
nombre_entry = tk.Entry(root)
nombre_entry.pack(side=tk.LEFT, padx=10, pady=10)

# bouton pour faire la recherche
rechercher_button = tk.Button(root, text="Rechercher", command=rechercher)
rechercher_button.pack(side=tk.RIGHT, padx=10, pady=10)

# fonctions pour vérifier si le nombre rentré par l'utilisateur est supérieur à 700, à compléter, les fonctions devraient marcher mais j'ai pas le code jpp tester

def rechercher():
        option = option_var.get()
        number = int(number_entry.get())
        if number >= 700:
            ... # on execute le programme de recherche 
        else:
            print("Le nombre doit être supérieur ou égal à 700")

def nb_valide(nouvelle_val):    # pas forcément utile mais j'l'ai faite au cas ou vous voudriez la connecter ( si vous voulez la connecter c'est dans nombre entry ( nombre_entry.config(nb_value=(...)) ) )
        if not nouvelle_val:
            return True
        try:
            value = int(nouvelle_val)
            return value >= 700
        except ValueError:
            return False

# lancer la fenêtre
root.mainloop()