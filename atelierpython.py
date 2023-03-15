import re

# Ouvrir le fichier contenant les adresses email
with open('input-emails.txt', 'r') as fichier :
     # Lire le contenu du fichier
    fichier_content = fichier.read()

# Utiliser une expression régulière pour extraire les adresses email
    motif = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    res = re.findall(motif, fichier_content)
    print(res)

# Parcourir les adresses email et vérifier si elles sont françaises
    for email in res:
        if email.endswith('fr') or email.endswith('fr\n'):
            print( email ,"est une adresse email française.")
        else:
            print(email," n'est pas une adresse email française.")