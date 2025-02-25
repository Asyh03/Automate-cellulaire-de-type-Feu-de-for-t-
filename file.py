from tkinter import *
import random

# Paramètres de la grille
hauteur = int(input("Entrez la hauteur de la grille : "))
largeur = int(input("Entrez la largeureur de la grille : "))  # Taille de la grille
cote = int(input("Entrez la taille d'une cellule en pixel : "))

# États des cellules
VIDE = 0
ARBRE = 1
FEU = 2
couleurs = {VIDE: "white", ARBRE: "green", FEU: "red"}
