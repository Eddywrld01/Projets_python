import sys
import json
import os

"""🏦 Classe CompteBancaire

Représente un compte bancaire classique.

Attributs :

numero_compte : identifiant unique du compte

titulaire : nom du propriétaire

solde : montant disponible sur le compte

Méthodes principales :

deposer(montant) → ajoute de l’argent au compte

retirer(montant) → retire une somme (avec vérification du solde)

afficher_solde() → affiche le solde actuel

to_dict() → convertit le compte en dictionnaire pour la sauvegarde JSON

---

💰 Classe CompteEpargne (hérite de CompteBancaire)

Ajoute un taux d’intérêt au compte bancaire.

Attributs supplémentaires :

taux_interet : taux de rémunération du compte (ex : 0.05 = 5 %)

Méthode spécifique :

ajouter_interets() → calcule et ajoute les intérêts au solde

---

🏛️ Classe Banque

Gère l’ensemble des comptes.

Attributs :

liste_compte : liste des comptes créés

fichier : chemin du fichier JSON utilisé pour la sauvegarde

Méthodes principales :

ajouter_compte(compte) → ajoute un compte à la banque

rechercher_compte(numero) → trouve un compte par son numéro

afficher_comptes() → affiche tous les comptes

sauvegarder_compte() → enregistre les comptes dans le fichier JSON

charger_comptes() → charge les comptes existants au démarrage

---

🧭 Fonctionnement du menu principal

Lors de l’exécution du programme (python banque.py), un menu interactif s’affiche :

****** Gestion d'une banque ******
1- Créer un compte bancaire
2- Créer un compte épargne
3- Déposer de l'argent
4- Retirer de l'argent
5- Ajouter des intérêts (épargne)
6- Afficher tous les comptes
7- Rechercher un compte
8- Sauvegarder les comptes
9- Quitter

Chaque option permet d’interagir avec les objets de la banque en temps réel.

---

⚙️ Fonctionnalités principales

Fonction	Description

🏦 Création de comptes	Crée un compte bancaire ou épargne avec solde initial
💵 Dépôt / Retrait	Gère les transactions avec vérification de validité
💹 Intérêts	Ajoute automatiquement les intérêts aux comptes épargne
🔍 Recherche	Recherche un compte à partir de son numéro
💾 Sauvegarde	Enregistre tous les comptes dans un fichier banque.json
❌ Suppression (optionnelle)	Supprime un compte après confirmation"""

class CompteBancaire:
    def __init__(self,numero_compte,titulaire,solde):
        self.numero_compte = numero_compte
        self.titulaire = titulaire
        self.solde = solde

    def __str__(self):
        return(f"Type de compte : Compte bancaire\n"f"Numéro : {self.numero_compte}\n"f"Titulaire : {self.titulaire}\n"f"Solde actuel : {self.solde} FCFA")    

    def deposer(self,montant):
        self.solde += montant
        return self.solde
    
    def retirer(self,montant):
        if montant>self.solde:
            print("Solde insuffisant❌")
            return False
        else:
            self.solde -= montant
            return self.solde
    
    def afficher_solde(self):
        print(f"Compte {self.numero_compte} : Solde = {self.solde} FCFA")

    def to_dict(self):
        return {
            "type de compte" : "bancaire",
            "numero du compte" : self.numero_compte,
            "nom du titulaire" : self.titulaire,
            "solde" : self.solde
        }    

    
class CompteEpargne(CompteBancaire):
    def __init__(self,numero_compte,titulaire,solde,taux_interet=0.02):
        super().__init__(numero_compte,titulaire,solde)    
        self.taux_interet = taux_interet

    def __str__(self):
        return(f"Type de compte : Compte epargne\n"f"Numéro : {self.numero_compte}\n"f"Titulaire : {self.titulaire}\n"f"Solde actuel : {self.solde} FCFA"f"Taux d'interêts : {self.taux_interet*100:.2f}%")        

    def ajouter_interets(self):
        interets = self.solde * self.taux_interet
        self.solde += interets
        print(f"Intérêts ajoutés : {interets:.2f} FCFA")

    def to_dict(self):
        data =  super().to_dict()  
        data["type de compte"] = "épargne"
        data["taux d'interets"] = self.taux_interet
        return data 


class Banque:
    def __init__(self,fichier = "banque.json"):
        self.liste_compte = []
        self.fichier = fichier

    def ajouter_compte(self, compte):
        self.liste_compte.append(compte)

    def rechercher_compte(self,numero):
        for c in self.liste_compte:
            if c.numero_compte.lower() == numero.lower():
                return c  
            
    def sauvegarder_compte(self):
        anciens = []
        if os.path.exists(self.fichier):
            with open(self.fichier,"r") as f:
                try:
                    anciens = json.load(f)
                except json.JSONDecodeError:
                    anciens = []    
        data = anciens+[c.to_dict() for c in self.liste_compte]
                    
        with open(self.fichier,"w") as f:
            json.dump(data,f,indent = 4)  
        print("Données sauvegardées avec succès")    


    def supprimer_compte(self,compte):
        self.liste_compte.remove(compte)


    def afficher_comptes(self):
        print("\n💰 Liste des comptes :")
        for c in self.liste_compte:
            c.afficher_solde()

    

def menu():
    banque = Banque()

    while True:
        print("****** Gestion d'une banque ******")
        print("1- Créer un compte bancaire")
        print("2- Créer un compte épargne")
        print("3- Déposer de l'argent")
        print("4- Retirer de l'argent")
        print("5- Ajouter des interêts (épargne)")
        print("6- afficher tous les comptes")
        print("7- Rechercher un compte")
        print("8- Sauvegarder les comptes")
        print("9- Supprimer un compte")
        print("10- Quitter")

        choix = input("Faites votre choix : ")
        print("-"*50)
        if choix == "1":
            numero = input("Numero du compte : ")
            nom_titulaire = input("Nom du titulaire : ")
            solde = float(input("Le montant initial : "))
            compte=CompteBancaire(numero,nom_titulaire,solde)
            banque.ajouter_compte(compte)
            print("Compte bancaire ajouté avec succès👌")
        elif choix == "2":
            numero = input("Numero du compte : ")
            nom_titulaire = input("Nom du titulaire : ")
            solde = float(input("Le montant initial : "))
            taux_interêts = float(input("Taux d'interêts (ex: 0.05 pour 5%) :  "))
            compteE = CompteEpargne(numero,nom_titulaire,solde,taux_interêts)
            banque.ajouter_compte(compteE)
            print("Compte épargne ajouté avec succès👌")
        elif choix == "3":
            numero = input("Entrez le numero du compte : ")
            compte = banque.rechercher_compte(numero)
            if compte:
                montant = float(input("Entrez le montant à déposer : "))
                compte.deposer(montant)
            else:
                print("Compte introuvable❌")
        elif choix == "4":
            numero = input("Entrez le numero du compte : ")
            compte = banque.rechercher_compte(numero)
            if compte:
                montant = float(input("Entrez le montant à retirer : "))
                compte.retirer(montant)
            else:
                print("Compte introuvable❌")   
        elif choix == "5":
            numero = input("Entrez le numéro du compte epargne : ")
            compte = banque.rechercher_compte(numero)
            if  isinstance(compte,CompteEpargne):
                compte.ajouter_interets()    
            else:
                print("Ce compte n'est pas un compte epargne")    
        elif choix == "6":
            banque.afficher_comptes()        
        elif choix == "7":
            numero = input("Entrez le numero du compte à rechercher : ")
            print(banque.rechercher_compte(numero))
        elif choix == "8":
            banque.sauvegarder_compte()
        elif choix == "9":
            numero = input("Entrez le numero du compte")
            compte = banque.rechercher_compte(numero)
            if compte:
                banque.supprimer_compte(compte)
            else:
                print("Compte introuvable")    

            
        elif choix == "10":
            sys.exit()
    
        print("-"*50)
        print("-"*50)

if __name__ == "__main__":
    menu()