from Système_de_banque import Banque

def afficher_menu():
    print("******** Gestion de Banque *********")
    print("1. Ajouter un compte")
    print("2. lister les comptes")
    print("3. Supprimer un livre")
    print("4: Quitter")

def main():
    banque = Banque()    
    
    while True:
        afficher_menu()
        choix = input("Entrez votre choix : ")
        print("-"*50)
        if choix == "1":
            num_compte = input("numero du compte : ")
            titulaire = input("Nom du titulaire : ")
            solde = input("Le solde initial : ")
            compte = f"{num_compte} - {titulaire} - {solde}"

            Banque.ajouter_compte(banque,compte)
        elif choix == "2":
            banque.afficher_comptes()    
    
main()    