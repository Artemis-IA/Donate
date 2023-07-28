# 🐳Plateforme de Dons - Whale Care WebApp🐳

La Plateforme de Dons est une application web basée sur Flask qui permet aux utilisateurs de faire des dons pour soutenir une cause spécifique. Les utilisateurs peuvent remplir un formulaire avec leurs informations, effectuer un don et voir la somme totale des dons récoltés ainsi que la liste des donateurs.

## Fonctionnalités

- Les utilisateurs peuvent remplir un formulaire avec leurs informations (nom, prénom, adresse, code postal, ville, email et montant du don).
- Les données des donateurs sont enregistrées dans une base de données MySQL.
- L'application utilise l'API Nominatim pour géocoder la ville saisie par l'utilisateur et obtenir ses coordonnées (latitude et longitude).
- La page "view" affiche la liste de tous les donateurs et la somme totale des dons récoltés.
- La page "greeting" affiche un message de remerciement après avoir effectué un don et redirige vers la page "view" après un délai de 5 secondes.

## Configuration Requise

- Python 3.x
- Flask
- MySQL
- Requests (pour effectuer des requêtes HTTP à l'API Nominatim)

## Installation

1. Clonez le dépôt GitHub :

```
git clone https://github.com/votre_utilisateur/plateforme-de-dons.git
```

2. Accédez au répertoire du projet :

```
cd plateforme-de-dons
```

3. Installez les dépendances Python :

```
pip install -r requirements.txt
```

4. Configurez la base de données :

   - Créez une base de données MySQL.
   - Modifiez les informations de connexion à la base de données dans le fichier `models/connexion.py`.

5. Lancez l'application :

```
python app.py
```

L'application sera accessible à l'adresse http://127.0.0.1:5000/ dans votre navigateur.

## Architecture du Projet

Le projet est structuré de la manière suivante :

- `app.py` : Le fichier principal de l'application Flask.
- `models/` : Le répertoire contenant les classes de gestion des données (connexion à la base de données et opérations CRUD).
- `templates/` : Le répertoire contenant les templates HTML pour les différentes pages de l'application (formulaire, page de remerciement, page de vue des dons, etc.).
- `static/` : Le répertoire contenant les fichiers statiques (CSS, images, etc.).
- `requirements.txt` : Le fichier contenant la liste des dépendances Python requises pour le projet.

## Auteur

Artemis-ia
https://artemis-ia.github.io/

## Licence

Ce projet est sous licence MIT. Vous pouvez consulter le fichier [LICENSE](LICENSE) pour plus de détails.

## Remarque

Ce projet a été réalisé à des fins éducatives dans le cadre de l'apprentissage de Flask et de la création d'une application web simple de plateforme de dons. Il peut être amélioré en ajoutant des fonctionnalités supplémentaires telles que la gestion des erreurs, l'authentification des utilisateurs, etc.

N'hésitez pas à contribuer en ouvrant des issues ou en proposant des pull requests pour améliorer ce projet !

