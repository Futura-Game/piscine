import os
from datetime import datetime

# Default values
param = {'bdd': [(1, 3, 10, '2024-05-11'), (2, 1, 13, '2024-05-12'), (3, 2, 6, '2024-05-11'), (3, 1, 8, '2024-05-13')],
         'nages': [(1, "Brasse"), (2, "Dos"), (3, "Crawl")],
         'nageurs': [(1, "Pierre"), (2, "Paul"), (3, "Léa")]
         }


def reset(param):
    """Réinitialise la base de données."""
    param.clear()
    param['bdd'] = []
    param['nages'] = []
    param['nageurs'] = []


def afficher_menu():
    print("\nChoisissez une option :")
    print("1 -> Ajout d'une performance")
    print("2 -> Ajout d'un individu")
    print("3 -> Ajout d'une nouvelle nage")
    print("4 -> Liste toutes les performances")
    print("5 -> Liste les performances d'un nageur")
    print("6 -> Liste tous les nageurs pratiquant une nage")
    print("7 -> Liste des performances d'un jour spécifique")
    print("8 -> Sauvegarde les données utilisateurs")
    print("9 -> Charge les données utilisateurs")
    print("0 -> Quitte le logiciel")


def get_str_from_num_in_list(num, liste):
    """Retourne la valeur associée à un ID dans une liste."""
    for elt in liste:
        if elt[0] == num:
            return elt[1]
    return "unknown"


def cmd_ajout(param):
    """Ajoute une performance."""
    for elt in param['nageurs']:
        print(f"{elt[0]:5} : {elt[1]}")
    a = int(input("Nageur n° ? "))
    for elt in param['nages']:
        print(f"{elt[0]:5} : {elt[1]}")
    b = int(input("Nage n° ? "))
    c = int(input("Combien de longueurs ? "))
    date = input("Date de l'événement (YYYY-MM-DD) ? ")
    # Validation du format de la date
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Date invalide. Utilisez le format YYYY-MM-DD.")
        return
    param['bdd'].append((a, b, c, date))
    print("Performance ajoutée avec succès.")


def cmd_individu(param):
    """Ajoute un nouvel individu."""
    prénom = input("Prénom du nouveau nageur ? ")
    id = len(param['nageurs']) + 1
    param['nageurs'].append((id, prénom))
    print(param['nageurs'])


def cmd_nouvelle_nage(param):
    """Ajoute une nouvelle nage."""
    nage = input("Quelle nage enregistrer ? ")
    id = len(param['nages']) + 1
    param['nages'].append((id, nage))
    print(param['nages'])


def cmd_liste(param):
    """Liste toutes les performances."""
    print("Prénom      |  nage   |  longueur | date")
    print("-----------------------------------------")
    for elt in param['bdd']:
        nageur = get_str_from_num_in_list(elt[0], param['nageurs'])
        nage = get_str_from_num_in_list(elt[1], param['nages'])
        print(f" {nageur:11}| {nage:8}|  {elt[2]:8}| {elt[3]}")


def cmd_nageur(param):
    """Liste les performances d'un nageur."""
    for elt in param['nageurs']:
        print(f"{elt[0]:5} : {elt[1]}")
    tmp = int(input("Quel numéro de nageur ? "))
    print(f"Performances de {get_str_from_num_in_list(tmp, param['nageurs'])}")
    print("  nage   | longueur | date")
    print("---------------------------")
    for elt in param['bdd']:
        if elt[0] == tmp:
            nage = get_str_from_num_in_list(elt[1], param['nages'])
            print(f" {nage:8}| {elt[2]:8}| {elt[3]}")


def cmd_par_date(param):
    """Liste les performances d'une date spécifique."""
    date = input("Entrez la date (YYYY-MM-DD) : ")
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Date invalide. Utilisez le format YYYY-MM-DD.")
        return
    print(f"Performances pour la date {date}")
    print("Nageur      |  nage   | longueur")
    print("-------------------------------")
    for elt in param['bdd']:
        if elt[3] == date:
            nageur = get_str_from_num_in_list(elt[0], param['nageurs'])
            nage = get_str_from_num_in_list(elt[1], param['nages'])
            print(f" {nageur:11}| {nage:8}| {elt[2]}")


def cmd_save(param, filename='save.csv'):
    """Sauvegarde des données."""
    with open(filename, 'w') as fichier:
        fichier.write('@ nageurs\n')
        for elt in param['nageurs']:
            fichier.write(f"{elt[0]},{elt[1]}\n")
        fichier.write('@ nages\n')
        for elt in param['nages']:
            fichier.write(f"{elt[0]},{elt[1]}\n")
        fichier.write('@ bdd\n')
        for elt in param['bdd']:
            fichier.write(f"{elt[0]},{elt[1]},{elt[2]},{elt[3]}\n")
    print("Données sauvegardées.")


def cmd_load(param, filename='save.csv'):
    """Charge des données sauvegardées."""
    reset(param)
    key = ''
    with open(filename, 'r') as fichier:
        for line in fichier:
            line = line.strip()
            if line.startswith('#'):
                continue
            if line.startswith('@'):
                key = line[2:]
                continue
            if not key:
                continue
            tmp = line.split(',')
            if key == 'bdd':
                tmp[0], tmp[1], tmp[2] = int(tmp[0]), int(tmp[1]), int(tmp[2])
            elif key in ('nages', 'nageurs'):
                tmp[0] = int(tmp[0])
            param[key].append(tuple(tmp))
    print("Données chargées avec succès.")


def gestion_commande(param):
    """Boucle principale de gestion des commandes."""
    while True:
        afficher_menu()
        choix = input("Entrez le numéro correspondant à votre choix : ")
        if choix == "1":
            cmd_ajout(param)
        elif choix == "2":
            cmd_individu(param)
        elif choix == "3":
            cmd_nouvelle_nage(param)
        elif choix == "4":
            cmd_liste(param)
        elif choix == "5":
            cmd_nageur(param)
        elif choix == "6":
            cmd_par_date(param)
        elif choix == "8":
            cmd_save(param)
        elif choix == "9":
            cmd_load(param)
        elif choix == "0":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")


# Programme principal
if __name__ == "__main__":
    if os.path.exists('save.backup'):
        cmd_load(param, 'save.backup')
    gestion_commande(param)