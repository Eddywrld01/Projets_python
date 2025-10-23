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
    - méthodes pour ajouter / afficher les membres."""

class Personne:
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age


class Etudiant(Personne):
    def __init__(self,nom,prenom,age,identifiant):
        super().__init__(nom,prenom,age)
        self.identifiant = identifiant
        self.liste_de_note = []

    def ajouter_note(self,note):
        self.liste_de_note.append(note)

    def moyenne(self):
        somme = 0
        if not self.liste_de_note:
            return 0
        else:
            for i in self.liste_de_note:
                somme += i
            return somme/len(self.liste_de_note)

class Professeur(Personne):
    def __init__(self,nom,prenom,age,matiere):
        self.matiere = matiere
        super().__init__(nom,prenom,age)


class Ecole:
    def __init__(self,nom):
        self.nom = nom
        self.liste_Etudiants = []
        self.liste_Professeurs = []

    def ajouter_etudiant(self,Etudiant):
        self.liste_Etudiants.append(Etudiant)

    def ajouter_professeur(self,Professeur):
        self.liste_Professeurs.append(Professeur)

    def afficher_etudiants(self):
        print("La liste des Etudiants : ")
        for element in self.liste_Etudiants:
            print(f"{element.nom} {element.prenom} - {element.identifiant}")
            

    def afficher_professeurs(self):
        print("La liste des Professeurs : ")
        for element in self.liste_Professeurs:
            print(f"{element.nom} {element.prenom} - {element.age} ans - {element.matiere}")

ecole = Ecole("Lycée des Codeurs")
et1 = Etudiant("Barou", "Edmond", 20, "E001")
et2 = Etudiant("Koffi", "Jean", 21, "E002")

et1.ajouter_note(15)
et1.ajouter_note(18)
et2.ajouter_note(12)

prof1 = Professeur("Toto", "Marc", 35, "Maths")

ecole.ajouter_etudiant(et1)
ecole.ajouter_etudiant(et2)
ecole.ajouter_professeur(prof1)

ecole.afficher_etudiants()
ecole.afficher_professeurs()

