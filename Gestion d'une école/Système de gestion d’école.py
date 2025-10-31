"""1. Crée une classe `Personne` avec `nom`, `prenom`, et `age`.
2. Crée une classe `Etudiant` qui hérite de `Personne`, avec :
    - un `identifiant`
    - une `liste_de_notes`
    - une méthode `ajouter_note(note)`
    - une méthode `moyenne()`
3. Crée une classe `Professeur` (héritant aussi de `Personne`), avec :
    - une matière enseignée
4. Crée une classe `Ecole` :
    - qui contient une liste d’étudiants et de professeurs
    - méthodes pour ajouter / afficher les membres.
    
"""

import json
class Personne:
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

class Etudiant(Personne):
    def __init__(self,nom,prenom,age,identifiant):
        super().__init__(nom,prenom,age)
        self.identifiant = identifiant
        self.liste_notes = []

    def ajouter_note(self,note):
        self.liste_notes.append(note)

    def moyenne(self):
       moy = sum(self.liste_notes)/len(self.liste_notes)
       return moy
    
    def to_dict(self):
        return {
            "type" : "Etudiant",
            "nom" : self.nom,
            "prenom" : self.prenom,
            "age" : self.age,
            "id" : self.identifiant
        }
    
class Professeur(Personne):
    def __init__(self,nom,prenom,age,matiere):
        super().__init__(nom,prenom,age)
        self.matiere = matiere

    def to_dict(self):
        return {
            "type" : "professeur",
            "nom" : self.nom,
            "prenom" : self.prenom,
            "age" : self.age,
            "matière enseignée" : self.matiere
        }    

class Ecole:
    def __init__(self,nom,fichier = "Ecole.json"):
        self.nom = nom
        self.fichier = fichier
        self.liste_etudiants = []
        self.liste_professeurs = []

    def ajouter_etudiant(self,Etudiant):
        self.liste_etudiants.append(Etudiant)    

    def retirer_etudiant(self,Etudiant):
        self.liste_etudiants.remove(Etudiant)    
        
    def ajouter_professeur(self,Professeur):
        self.liste_professeurs.append(Professeur)  

    def retirer_professeur(self,Professeur):
        self.liste_professeurs.remove(Professeur)  

    def afficher_etudiants(self):
        for element in self.liste_etudiants:
            print(f"{element.identifiant} - {element.nom} {element.prenom} - {element.age}")      

    def afficher_professeurs(self):
        for element in self.liste_professeurs:
            print(f"Mr/Mme/Mlle {element.nom} {element.prenom} - {element.age} ans - Professeur(e) de {element.matiere}")

    def sauvegarder(self):
        data = []   
        for c in self.liste_etudiants:
            data.append(c.to_dict())

        for i in self.liste_professeurs:
            data.append(i.to_dict())

        """with open(self.fichier,"r") as f:
            anciens = json.load(f)
        
        anciens.append(data)"""
        
        with open(self.fichier,"w") as f:
            json.dump(data,f,indent = 4)
 
#Menu interactif
def menu():
    ecole = Ecole("Le domaine des codeurs")
    while True:
        print("*****Gestion d'une école*****")
        print("1- Ajouter un(e) etudiant(e)")
        print("2- retirer un(e) etudiant(e)")
        print("3- Ajouter un(e) professeur(e)")
        print("4- Retirer un(e) professeur(e)")
        print("5- Afficher la liste des etudiants")
        print("6- Afficher la liste des professeurs")
        print("7- Sauvegarder la liste des etudiants")
        print("8- Quitter")
        choix = input("Faites votre choix : ")
        print("-"*50)

        if choix == "1":
            nom = input("Entrez le nom de l'Etudiant(e) : ")
            prenom = input("Entrez le prenom de l'Etudiant(e) : ")
            age = input("Entrez l'âge de l'Etudiant(e) : ")
            identifiant = input("Entrez l'identifiant de l'Etudiant(e) : ")
            Etud = Etudiant(nom,prenom,age,identifiant)
            ecole.ajouter_etudiant(Etud)
            print(f"L'etudiant(e) {Etud.nom} s'est inscrit(e) dans votre etablissement")
        elif choix == "2":
            identifiant = (input("Entrez l'identifiant de l'Etudiant(e) : "))
            for element in ecole.liste_etudiants:
                if element.identifiant.lower() == identifiant.lower():
                    ecole.retirer_etudiant(Etud)
                    print(f"L'etudiant(e) {Etud.nom} est retirée de votre etablissement")
                else:
                    print("Etudiant(e) introuvable")
        elif choix == "3":
            nom = input("Entrez le nom du professeur(e) : ")
            prenom = input("Entrez le prenom du professeur(e) : ")
            age = input("Entrez l'âge du professeur(e) : ")    
            matiere = input("Entrez la matière enseignée : ")
            Prof = Professeur(nom,prenom,age,matiere)
            ecole.ajouter_professeur(Prof)
            print(f"Mr/Mme/Mlle {Prof.nom} est admis(e) à votre etablissement")
        elif choix == "4":
            nom = input("Entrez le nom du professeur(e) à retirer : ")
            for element in ecole.liste_professeurs:
                if element.nom.lower() == nom.lower():
                    ecole.retirer_professeur(Prof)
                else:
                    print("Professeur introuvable")   
        elif choix == "5":
            ecole.afficher_etudiants()
        elif choix == "6":
            ecole.afficher_professeurs()
        elif choix == "7":
            ecole.sauvegarder()
            print("sauvegardé avec succès")
        elif choix == "8":
            print("Au revoir ! ")
            break    
        
        
        print("-"*50)    
        print("-"*50)    
            

if __name__ == "__main__":
    menu()