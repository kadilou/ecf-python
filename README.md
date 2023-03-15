# ecf-python
Le programme attelierpython sert a verifier si une addresse mail est bien une adresse francaise,
Au debut nous avons commencé par importer la biblihoteque re pour les expressions reguliere,  
apres nous avons 
Ce programme utilise une expression régulière pour extraire toutes les adresses email dans le fichier texte, puis vérifie si chaque adresse se termine par ".fr" pour déterminer si elle est française ou non. Notez que ce n'est pas une méthode infaillible pour détecter les adresses email françaises, car il est possible qu'une adresse utilise un domaine autre que ".fr" mais reste néanmoins française.


Ce programme est un script Python qui lit un fichier texte contenant des adresses e-mail, utilise une expression régulière pour extraire les adresses e-mail de ce fichier, puis vérifie si chaque adresse e-mail est française ou non.

on commence par importer le module Python "re" pour les expressions régulières. Ensuite, il ouvre le fichier texte nommé "input-emails.txt" en mode lecture seule, lit son contenu et stocke le contenu dans la variable "fichier_content".

Il utilise ensuite une expression régulière pour extraire les adresses e-mail de "fichier_content". L'expression régulière est stockée dans la variable "motif". Cette expression régulière est conçue pour correspondre à des adresses e-mail valides de tout domaine. La fonction "findall" du module "re" est utilisée pour appliquer l'expression régulière à "fichier_content" et stocker toutes les adresses e-mail trouvées dans la liste "res".

Ensuite, le script parcourt chaque adresse e-mail dans "res" et vérifie si elle se termine par "fr" en utilisant la méthode "endswith". Si l'adresse e-mail se termine par fr, le script affiche "est une adresse e-mail française." Sinon, il affiche "n'est pas une adresse e-mail française.". Les résultats sont affichés à la console.

En résumé, ce script Python permet d'extraire les adresses e-mail d'un fichier texte, puis de vérifier si chaque adresse est française ou non en examinant son extension de domaine.

