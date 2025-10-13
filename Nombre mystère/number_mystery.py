"""Le jeu du nombre mystère.


Cela consiste à faire jouer l'utilisateur un certain nombre de coups pour qu'il trouve un nombre mystère aléatoire défini entre 0 et 100.

Le nombre d'essais est de 5. On propose à l'utilisateur de deviner le nombre:

-Tant que l'utilisateur envoie une entrée autre qu'un entier alors on lui avertit qu'il doit faire une entrée valide et le script lui renvoie la demande.

-Si l'utilisateur entre un nombre compris entre 0 et 100 et qu'il ne trouve pas le nombre mystère alors le script lui indique si le nombre mystère est plus grand ou plus petit que le nombre qu'il a indiqué puis il perd 1 essai.

-Dans le cas contraire il gagne la partie avec l'affichage du nombre d'essais non utilisés.

-S'il épuise tous ses essais alors il perd définitivement la partie et le script se ferme.

"""

from random import randint
user_choice = ""
nb_mystery = randint(1,101)
nb_essais = 5

print("*** Le jeu du nombre mystère ***")
while nb_essais>0:
    print(f"Vous avez {nb_essais} essai{'s' if nb_essais>1 else ''}")
    user_choice = input("Devinez le nombre : ")
    if not user_choice.isdigit():
        print("Entrez un nombre svp...")
        print("-"*50)
        continue
    elif user_choice.isdigit():
        user_choice = int(user_choice)
        if nb_mystery<user_choice:
            print(f"Le nombre mystère est plus petit que {user_choice} ")
            nb_essais -= 1
            print("-"*50)
        elif nb_mystery > user_choice:
            print(f"Le nombre mystère est plus grand que {user_choice} ")
            nb_essais -= 1
            print("-"*50)
        else:
            break    
if nb_essais == 0:
    print(f"Dommage le nombre mystère était {nb_mystery}")
else:
    print(f"Félicitations ! Vous avez trouvé le nombre mystère en {6-nb_essais}")            
        

