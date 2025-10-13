a = b = ""
while not(a.isdigit() and b.isdigit()):
    a = input("Entrez un premier nombre: ")
    b = input("Entrez un deuxième nombre: ")
    if not(a.isdigit() and b.isdigit()):
        print("Veuillez entrer un nombre valide")
    else:
        print(f"L'addition de {a} avec {b} est égale à {int(a)+int(b)}")
