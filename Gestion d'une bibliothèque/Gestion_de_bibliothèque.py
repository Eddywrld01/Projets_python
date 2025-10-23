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
class livre:
    def __init__(self,titre,auteur,annee_publication):
        self.titre = titre
        self.auteur=auteur
        self.annee_publication=annee_publication
        self.disponible=True

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print(f"Vous avez emprunté '{self.titre}'")
        else:
            print("Ce livre a déjà été emprunté ")

    def retourner(self):
        self.disponible = True
        print(f"'{self.titre}' a été retourné") 

class bibliotheque:
    def __init__(self):
        self.liste_livres = []

    def ajouter_livre(self,livre):
        self.liste_livres.append(livre)    
    
    def afficher_livres_disponibles(self):
        for element in self.liste_livres:
            if element.disponible:
                print(f"{element.titre} - ({element.auteur})")

    def rechercher(self, titre):
        for livre in self.liste_livres:
            if livre.titre.lower() == titre.lower():
                print(livre.titre)
        
            

Livre1 = livre("1984", "George Orwell", 1949)
Livre2 = livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
bibli = bibliotheque()

"""bibli.ajouter_livre(Livre1)
bibli.ajouter_livre(Livre2)
bibli.afficher_livres_disponibles()

Livre1.emprunter()
bibli.afficher_livres_disponibles()

Livre1.retourner()
bibli.afficher_livres_disponibles()"""

print(bibli.rechercher(1984)
)