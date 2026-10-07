import random 

print("Bienvenue dans le jeu du Nombre Mystère !")

nombre_mystere = random.randint(1, 20)

essais = 0

while True:
    choix = int(input("Devine un nombre entre 1 et 20 : "))
    essais += 1

    if choix < nombre_mystere:
        print("C'est plus grand ↑")
    elif choix > nombre_mystere:
        print("C'est plus petit ↓")
    else:
        print(f"Bravo 🎉 ! Tu as trouvé en {essais} essais.")
        break
