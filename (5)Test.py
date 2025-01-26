try:
    number = int(input("Entrez un nombre : "))
    result = 10 / number
except ValueError:
    print("Veuillez entrer un nombre valide.")
except ZeroDivisionError:
    print("Division par zéro impossible.")
else:
    print(f"Le résultat est : {result}")  # S'exécute uniquement si aucune exception n'est levée
finally:
    print("Merci d'avoir utilisé ce programme.")
