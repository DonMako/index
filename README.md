# Index

## Description du programme
Le programme par de la liste d'URLs au format json, et en extrait les titres, les tokenize et construit un index web non positionnel.

Avant de construire l’index web, le programme sort des statistiques sur les documents telles que:
* le nombre de documents ;
* le nombre de tokens ;
* la moyenne des tokens par documents.

Une fois terminé, le programme écrit dans un fichier *title.non_pos_index.json* l’index créé, et dans un fichier *metadata.json* les informations statistiques que vous aurez calculé.

## Lancer le programme

```
git clone https://github.com/DonMako/index.git
cd index
pip install -r requirements.txt
python3 main.py
```

## Auteur
Lucas Macaux