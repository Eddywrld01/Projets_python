def barre():
    print("-"*50)
    return
#importer le module random qui servira à l'ordinateur de faire un choix au hasard 
import random
#importer le module sys pour pouvoir quitter le programme
import sys
#Une liste pour stocker les différents choix
LISTE_CHOIX = ["P","C","F"]
#Initialiser les points de l'utilisateur, l'ordinateur et le nombre de manches

choix_ordinateur = ""
choix_utilisateur = ""
nom = input("Entrez votre nom svp : ")
print(f"Bienvenue {nom} !")
input()
while True:
    
    pt_utilisateur = 0
    pt_ordinateur = 0
    nb_manches = 1
    print("LE JEU DU PIERRE, FEUILLE, CISEAUX")
    print("La partie se déroulera en 3 manches")
    input()
    while nb_manches <= 3:
        print(f"Manche {nb_manches}")
        choix_utilisateur = input("Faites un choix entre 'P', 'F' et 'C' : ").upper()
        choix_ordinateur = random.choice(LISTE_CHOIX)
        while not(choix_utilisateur in LISTE_CHOIX):
            print("Erreur de saisie, veuillez faire une commande valide !")
            input()
            break
        if choix_utilisateur in LISTE_CHOIX:
            if ((choix_utilisateur == "F") and  (choix_ordinateur == "P")) or ((choix_utilisateur == "P") and (choix_ordinateur == "C"))or ((choix_utilisateur == "C") and (choix_ordinateur == "F")):
                print("Vous avez gagné cette manche ! ")
                pt_utilisateur+=1
                print(f"{nom} : {pt_utilisateur} \nOrdinateur : {pt_ordinateur}")
                barre()
            elif ((choix_ordinateur == "F") and  (choix_utilisateur == "P")) or ((choix_ordinateur == "P") and (choix_utilisateur == "C")) or ((choix_ordinateur == "C") and (choix_utilisateur == "F")):    
                print("L'ordinateur à gagné cette manche !")
                pt_ordinateur+=1
                print(f"{nom} : {pt_utilisateur} \nOrdinateur : {pt_ordinateur}")
                barre()
            else:
                print("Egalité ! ") 
                print(f"{nom} : {pt_utilisateur} \nOrdinateur : {pt_ordinateur}")
                barre()
            nb_manches+=1       

    if pt_utilisateur < pt_ordinateur:
        print("L'ordinateur à gagné cette partie !")
    elif pt_utilisateur > pt_ordinateur:
        print("Vous avez gagné cette partie ! ")
    else:
        print("Pas de gagnant ! ")

    restart = input("Voulez vous recommencer la partie? o/n : ").lower()
    if restart == 'o':
        print("-"*100)  
        continue
    elif restart == 'n':
        print("Au revoir !")
        sys.exit()
    else:
        print("Veuillez entrer o ou n") 


        
        


    
    



