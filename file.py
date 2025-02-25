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

# Matrices de l'automate
cellule = [[None] * hauteur for i in range(largeur)]
state = [[ARBRE if random.random() < 0.6 else VIDE for j in range(hauteur)] for k in range(largeur)] #Placement des arbres : On suppose que la forêt est remplie de 60% d'arbres et le reste n'est que du vide
running = False

#Allumer le feu initial
def init_fire() :
  for i in range(hauteur) :
    if random.random() <= 0.1 : # en 10%
      state[i][0] = FEU #On suppose ici que l'incendie débute au niveau de ka première ligne au dessus et se déplace en parallèle

def transform() :
  for sx , sy in [(0,1),(0,-1),(-1,0)] :
    if state[x][y] == ARBRE and any(state[(x+sx)%hauteur][(y+sy)%largeur]) == FEU :
      state[x][y] = FEU
    elif state[x][y] == FEU :
      state[x][y] = VIDE
      
  
