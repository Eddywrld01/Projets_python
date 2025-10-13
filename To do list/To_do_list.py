import sys
MENU = """\nChoisissez parmi les 5 options suivantes : 
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
👉 Votre choix : """

choix_utilisateur = ""
STOCK = []
MENU_CHOICE = ["1","2","3","4","5"]

while True:
    choix_utilisateur = input(MENU)
    while not choix_utilisateur in MENU_CHOICE:
        print("Faites une commande valide...")
        break
    if choix_utilisateur in MENU_CHOICE:
        if choix_utilisateur == "1":
            item = input("Entrez l'élément que vous voulez ajouter : ").lower()
            STOCK.append(item)
            print(f"L'élément {item} à été ajouté à la liste")
        elif choix_utilisateur == "2":
            if item in STOCK:
                item = input("Entrez l'élément que vous voulez retirer : ").lower()
                STOCK.remove(item)
                print(f"L'élément '{item}' a bien été retirée de la liste")
            else:
                print(f"L'élément '{item}' n'existe pas dans la liste")
        elif choix_utilisateur == "3":
            if STOCK:
                for i,item in enumerate(STOCK,1):
                    print(f"{i}. {item}")     
            else:
                print("Votre liste est vide...")      
        elif choix_utilisateur == "4":
            v=input("Voulez vous vraiment vider toute la liste? oui/non :")
            if v == "oui":
                STOCK.clear()
                print("Votre liste à été vidée...")
            else:
                print("Commande annulée...")    
        elif choix_utilisateur == "5":
            print("Au revoir !")
            sys.exit()    
    print("-"*50)                         


    