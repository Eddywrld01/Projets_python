# Le jeu du nombre mystère.





Cela consiste à faire jouer l'utilisateur un certain nombre de coups pour qu'il trouve un nombre mystère aléatoire défini entre 0 et 100.



Le nombre d'essais est de 5. On propose à l'utilisateur de deviner le nombre:



-Tant que l'utilisateur envoie une entrée autre qu'un entier alors on lui avertit qu'il doit faire une entrée valide et le script lui renvoie la demande.



-Si l'utilisateur entre un nombre compris entre 0 et 100 et qu'il ne trouve pas le nombre mystère alors le script lui indique si le nombre mystère est plus grand ou plus petit que le nombre qu'il a indiqué puis il perd 1 essai.



-Dans le cas contraire il gagne la partie avec l'affichage du nombre d'essais non utilisés.



-S'il épuise tous ses essais alors il perd définitivement la partie et le script se ferme.













## Réflexion



Étape			Question à se poser



1\. Entrées		Qu’est-ce que l’utilisateur peut saisir ?

2\. Données		Qu’est-ce que je dois stocker ?

3\. Actions		Quelles opérations sur ces données ?

4\. Erreurs possibles	Qu’est-ce qui peut mal se passer ?

5\. Sorties		Qu’est-ce que j’affiche à l’utilisateur ?

6\. Fin de vie		Comment/quand mon script s’arrête ?



## Réponse



1. Un **nombre** pour deviner le nombre mystère
2. Le choix de l'utilisateur, le nombre mystère et le nombre d'essais
3. Une comparaison
4. L'utilisateur entre tout caractère différent d'un nombre ( q , . , "" , '' , # ,  , etc...)
5. Des messages clairs et visuels
6. Si l'utilisateur gagne ou s'il épuise tous ses essais



## Fonctionnalités



1. Pouvoir comparer le choix de l'utilisateur au nombre mystère
2. Lui faire reprendre la demande s'il entre un caractère différent d'un nombre
3. Pouvoir lui retirer 1 essai à chaque erreur
4. Lui donner un indice sur l'emplacement du nombre mystère à chaque erreur
