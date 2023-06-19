import json
import os

root_dir = os.path.dirname(__file__)
liste_path = os.path.join(root_dir, "liste.json")

liste_food = []


with open(liste_path, "r") as f:
    liste_food = json.load(f)

while True:

    print("Quel est ton choix ?" )
    print("1. Ajouter un élément à la liste de courses")
    print("2. Retirer un élément de la liste de courses")
    print("3. Afficher les éléments de la liste de courses")
    print("4. Vider la liste de courses")
    print("5. Quitter le programme")

    choice = input("")

    valid_answer = ["1", "2", "3", "4", "5"]

    if choice == "1":
        answer = input("Quel aliment veux-tu ajouter ?")
        liste_food.append(answer)
    elif choice == "2":
        answer = input("Quel aliment veux-tu retirer ?")
        liste_food.remove(answer)
    elif choice == "3":
        print(f"Voici la liste {liste_food}")
    elif choice == "4":
        liste_food.clear()
    elif choice == "5":
        print("Bye")
        break
    elif choice != valid_answer:
        print("Veuillez choisir un chiffre parmi la liste")

with open(liste_path, "w") as f:
    json.dump(liste_food, f)
    print(liste_food)
