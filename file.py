from tkinter import *
import random

# Paramètres de la grille
hauteur = int(input("Entrez la hauteur de la grille : "))
largeur = int(input("Entrez la largeureur de la grille : "))
cote = int(input("Entrez la taille d'une cellule en pixel : "))

# États des cellules
VIDE = 0
ARBRE = 1
FEU = 2
couleurs = {VIDE: "white", ARBRE: "green", FEU: "red"}

# Matrices de l'automate
cellule = [[None] * hauteur for i in range(largeur)]
state = [[ARBRE if random.random() < 0.6 else VIDE for j in range(hauteur)] for k in range(largeur)] #Placement des arbres : On suppose que la forêt est remplie de 60% d'arbres et le reste n'est que du vide
running = False #Variable qui signale si le programme est en marche ou pas

#Mise à jour l'affichage graphique de la grille
def draw() :
  for x in range(hauteur) :
    for y in range(largeur) :
      canvas.itemconfig(cellule[x][y],fill=couleurs[state[x][y]])

#Allumer le feu initial
def init_fire() :
  for i in range(hauteur) :
    if random.random() <= 0.1 : # feu à 10%
      state[i][0] = FEU #On suppose ici que l'incendie débute au niveau de la première ligne au dessus 

#Conditions de l'incendie de la forêt
def transform() :
  global state
  if running:
    new_state = [[state[x][y] for y in range(hauteur)] for x in range(largeur)]
    for x in range(hauteur) :
      for y in range(largeur) :
          if state[x][y] == ARBRE and any(state[(x+dx) % largeur][(y+dy) % hauteur] == FEU for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]): #Un arbre prend feu si l'arbre qui est est son voisin prend feu sachant que dx et dy constituent les voisins directs des arbres ie gauche,droite,haut, bas
              new_state[x][y] = FEU
          elif state[x][y] == FEU : #Sinon si l'arbre est déjà en feu, on aura que du vide ou de la cendre
              new_state[x][y] = VIDE
    state = new_state #On actualise à chaque fois l'état de chaque cellules de la grille
    draw()
    window.after(100, transform) # on met à 100ms pour voir la simulation en un click

#Gérer l'arrêt du programme
def start_stop():
  global running
  running = not running 
  if running :
    transform()

#Réinitialiser le programme
def reset() :
  global running
  running = False
  for x in range(hauteur) :
    for y in range(largeur) :
      state[x][y] = ARBRE if random.random() < 0.6 else VIDE 
  init_fire()
  draw()

# Création de la fenêtre
window = Tk()
window.title("Automate Cellulaire de type feu de forêt")
canvas = Canvas(window, width = cote*largeur, height = cote*hauteur)
canvas.pack()

#Création des cellules
for x in range(hauteur) :
  for y in range(largeur) :
    cellule[x][y] = canvas.create_rectangle(x*cote , y*cote , (x+1)*cote , (y+1)*cote , outline = "black" , fill = "white")

# Interface de contrôle
frame = Frame(window)
frame.pack()
Button(frame, text="Commencer / Arrêter" , command = start_stop).pack(side=LEFT)
Button(frame, text = "Réinitialiser" , command = reset).pack(side=RIGHT)

init_fire()
draw()
window.mainloop()
