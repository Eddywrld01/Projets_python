"""1. Crée une classe `CompteBancaire` avec :
    - `numero_compte`, `titulaire`, `solde`
    - méthodes `deposer(montant)` et `retirer(montant)`
    - méthode `afficher_solde()`
2. Crée une sous-classe `CompteEpargne` qui hérite de `CompteBancaire` :
    - attribut `taux_interet`
    - méthode `ajouter_interets()`
3. Gère les erreurs (ex : retrait supérieur au solde).
4. Crée une classe `Banque` qui gère plusieurs comptes."""

class CompteBancaire:
    def __init__(self,numero_compte,titulaire,solde):
        self.numero_compte = numero_compte
        self.titulaire = titulaire
        self.solde = solde

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

    
class CompteEpargne(CompteBancaire):
    def __init__(self,numero_compte,titulaire,solde,taux_interet=0.02):
        super().__init__(numero_compte,titulaire,solde)    
        self.taux_interet = taux_interet

    def ajouter_interets(self):
        interets = self.solde * self.taux_interet
        self.solde += interets
        print(f"Intérêts ajoutés : {interets:.2f} FCFA")


class Banque:
    def __init__(self):
        self.liste_compte = []

    def ajouter_compte(self, compte):
        self.liste_compte.append(compte)

    def afficher_comptes(self):
        print("\n💰 Liste des comptes :")
        for c in self.liste_compte:
            c.afficher_solde()

    
"""banque = Banque()
c1 = CompteBancaire("C001", "Edmond", 5000)
c2 = CompteEpargne("C002", "Koffi", 10000, 0.05)

banque.ajouter_compte(c1)
banque.ajouter_compte(c2)

c1.deposer(2000)
c2.ajouter_interets()
c2.retirer(3000)

banque.afficher_comptes()"""

    
