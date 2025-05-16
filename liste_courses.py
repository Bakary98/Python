import sys
liste_courses = []
while True:
    texte = """Choisissez parmi les 5 options suivantes : 
     1: Ajouter un élément à la liste de courses
     2: Retirer un élément de la liste de courses
     3: Afficher les éléments de la liste de courses 
     4: Vider la liste de courses
     5: Quitter le programme """
    
    print (texte)
    user_input = input("Votre choix :")
    while  not int(user_input.isdigit())== 0  and 1 <= user_input < 6:
        print("Choisissez bien un nombre ent 1, 2, 3, 4 et 5")
        print(texte)
        user_input = input("Votre choix :")
    if  user_input == "1":
        element_to_add= input(" Entrer le nom d'un élément à ajouter à la liste de course: ") 
        liste_courses.append(element_to_add)
        print(f"Elément ajouté : {element_to_add}")
    elif  user_input == "2":
        item_to_remove = input(" Entrer le nom d'un élément à retirer à la liste de course: ") 
        if item_to_remove in liste_courses:
            liste_courses.remove(b)
        else:
            print(f"Votre liste ne contien pas l'élément {item_to_remove}")
        print(f"Elément retiré : {b}")
    elif  user_input == "3":
        if liste_courses:
            print(f"Voilà la liste de courses: " )
            for i, element in enumerate(liste_courses):
                print(i, element)
        else :
            print("Votre panier est vide")
    elif user_input == "4":
        c = input("Souhaites -tu vider la liste de course ? 'o' pour continuer ou'n' pour annuler ")
        if (c == 'o'):
            liste_courses.clear()
            print ("La liste de course a été vidé.")
        elif (c == 'n'): 
            print (" Opération annulée ")
        else: 
            print ("Choix invalides")
    elif user_input == "5":
        print("Quitter le programmme")
        sys.exit()

### Correction 

import sys

LISTE = []

MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
? Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]



while True:
    user_choice = input(MENU)
    if user_choice not in MENU_CHOICES:
        print("Veuillez choisir une option valide...")
        continue

    if user_choice == "1":  # Ajouter un élément
        item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        LISTE.append(item)
        print(f"L'élément {item} a bien été ajouté à la liste.")
    elif user_choice == "2":  # Retirer un élément
        item = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"L'élément {item} a bien été supprimé de la liste.")
        else:
            print(f"L'élément {item} n'est pas dans la liste.")
    elif user_choice == "3":  # Afficher la liste
        if LISTE:
            print("Voici le contenu de votre liste :")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucun élément.")
    elif user_choice == "4":  # Vider la liste
        LISTE.clear()
        print("La liste a été vidée de son contenu.")
    elif user_choice == "5":  # Quitter
        print("À bientôt !")
        sys.exit()

    print("-" * 50)
