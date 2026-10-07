import random

choix_possibles = ["rock", "paper", "scissor"]

print("Welcome in the game Rock - Paper - Scissor !")

joueur = input("Your choice ? (rock, paper ou scissor) : ").lower()

ordi = random.choice(choix_possibles)

print("L'ordinateur a choisi :", ordi)

if joueur == ordi:
    print("Match nul")
elif (joueur == "rock" and ordi == "scissor") \
     or (joueur == "paper" and ordi == "rock") \
     or (joueur == "scissor" and ordi == "paper"):
    print("T'as gagné pour cette fois")
else:
    print("T'as perdu sale nul")
