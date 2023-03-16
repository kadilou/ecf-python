import re

# Ouvrir le fichier contenant les adresses email
with open('input-emails.txt', 'r') as fichier :
     # Lire le contenu du fichier
    fichier_content = fichier.read()

# Utiliser une expression régulière pour extraire les adresses email
    motif = r'\s[A-Za-z0-9._%+!-]+@[A-Za-z0-9.-]+\.fr\s'
    res = re.findall(motif, fichier_content)
    for i in res :
        res = i.strip('\n')
        res= i.strip(' ')
        print(i)