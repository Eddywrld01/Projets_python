"""TM python

Soit la classe appelée Compte qui est caractérisée par:

Compte

- code: Entier

- solde: Réel

+ Constructeur avec paramètres

+ Getters

+ Setters

+ verser(mt)

+ retirer(mt)

+ afficher()

1- Ecrire un programme Python permettant de définir la classe Compte avec ses attributs et ses méthodes, sachant que:

→ La méthode verser(mt) permet d'augmenter le solde avec le paramètre mt

a méthode retirer(mt) permet de réduire le solde avec le paramètre mt

La méthode afficher() permet d'afficher le texte: Code-valeur -Solde-valeur

2- Créer 2 objets compte1 et compte2 de la classe Compte avec les valeurs suivantes:

Compte1: code 1, solde = 9000.00

Compte2: code = 2, solde = 13000.00

3- Verser un montant de 5000.00 pour le compte1

-Retirer un montant de 3000.00 pour le compte2

5- Afficher les informations relatives au compte2"""




class Compte:
    # Constructeur
    def __init__(self,code:int,solde:float):
        self.code = code
        self.solde = solde

    #les getters
    def get_code(self)-> int:
        return self.code

    def get_solde(self)-> float:
        return self.solde

    #Les setters
    def set_code(self,code):
        self.code = code

    def set_solde(self,solde):
        self.solde = solde

    #verser
    def verser(self,mt:float):
        self.solde += mt
        
    #retirer
    def retirer(self,mt:float):
        self.solde -= mt
   
    #afficher
    def afficher(self):
        print(f"code = {self.code} - Solde = {self.solde}")

