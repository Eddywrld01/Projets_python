"""1. Crée une classe `Livre` avec :
    - `titre` (str)
    - `auteur` (str)
    - `annee_publication` (int)
    - `disponible` (bool, True par défaut)
2. Ajoute une méthode `emprunter()` qui change l’état du livre en **non disponible**.
3. Ajoute une méthode `retourner()` pour remettre le livre en **disponible**.
4. Crée une classe `Bibliotheque` contenant :
    - une liste de livres
    - une méthode `ajouter_livre(livre)`
    - une méthode `afficher_livres_disponibles()`
    - une méthode `rechercher(titre)` qui renvoie le livre s’il existe."""

class Livre:
    def __init__(self,titre,auteur,annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
        self.disponible = True

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print(f"Vous avez recupéré '{self.titre}'")
        else:
            print("Ce livre a déjà été emprunté")    

    def retourner(self):
        self.disponible = True
        print(f"'{self.titre}' a été retouné")   

class bibliotheque:
    def __init__(self):
        self.liste_livres = []           

    def ajouter_livre(self,Livre):
        self.liste_livres.append(Livre)   

    def retirer_livre(self,Livre):
        self.liste_livres.remove(Livre)   

    def afficher_livres_disponibles(self):
        print("La liste des livres : ")
        for c,element in enumerate(self.liste_livres):
            if element.disponible:
                print(f"{c+1} - '{element.titre}' - ({element.auteur}) - {element.annee_publication}")

    def rechercher(self):
        titre = input("Entrez le titre du livre : ")
        for element in self.liste_livres:
            if element.titre.lower() == titre.lower():
                print(f"{element.titre}' - ({element.auteur}) - {element.annee_publication}")
            else:
                print("Livre introuvable")    


def menu():
    biblio = bibliotheque()
    while True:
        print("******Gestion d'une bibliothèque******")
        print("1- Ajouter un livre")
        print("2- Retirer un livre")
        print("3- Afficher les livres disponibles : ")
        print("4- Rechercher un livre : ")
        print("5- Quitter")
        choix = input("Faites un choix : ")
        print("-"*50)
        
        if choix == "1":
            titre = input("Entrez le titre du livre : ")
            auteur = input("Le nom de l'auteur : ")
            annee_publication = input("La date de parution : ")
            book = Livre(titre,auteur,annee_publication)
            biblio.ajouter_livre(book)
        elif choix == "2":
            titre = input("Entrez le titre du livre à retirer : ")
            for c in biblio.liste_livres: 
                if c.titre.lower() == titre.lower():
                    print(f"Vous avez retiré {c.titre}")
                    biblio.retirer_livre(c)
                else:
                    print("Livre introuvable")  
        elif choix == "3":
            biblio.afficher_livres_disponibles()  
        elif choix == "4":
            biblio.rechercher()
        elif choix == "5":
            break
        print("-"*50)    
        print("-"*50)    
                 

    

if __name__ == "__main__":
    menu()                     