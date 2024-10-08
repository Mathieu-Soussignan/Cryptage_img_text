# Projet de Cryptage d'Images et de Textes

## Description

Ce projet permet de crypter et de déchiffrer des images ainsi que des textes en utilisant des techniques simples pour les images et la bibliothèque `cryptography` pour les textes. Une interface graphique interactive a été développée en utilisant **Streamlit**, ce qui permet une interaction facile via un navigateur.

## Fonctionnalités

- **Cryptage d'images** : Charger une image, la convertir en niveaux de gris et la crypter.
- **Décryptage d'images** : Récupérer l'image cryptée et la déchiffrer.
- **Cryptage et déchiffrement de textes** : Crypter un texte avec une clé secrète générée, puis déchiffrer ce texte avec la même clé.
- **Téléchargement des résultats** : Télécharger les résultats cryptés (texte ou image) dans des fichiers séparés.

## Arborescence du projet

```
Cryptage_img_text/
│
├── app/
│   ├── __init__.py                # Fichier pour marquer le répertoire comme un package
│   ├── cryptage_image.py           # Fonctions pour le cryptage d'image
│   └── cryptage_texte.py           # Fonctions pour le cryptage et déchiffrement de texte
│
├── images/                         # Contient les images utilisées pour le cryptage
│   └── example.jpg                 # Exemple d'image à utiliser pour les tests
│
├── tests/                          # Contient les fichiers de tests unitaires
│   ├── test_cryptage_image.py      # Tests pour le cryptage d'image
│   └── test_cryptage_texte.py      # Tests pour le cryptage et déchiffrement de texte
│
├── app_streamlit.py                # Interface graphique développée avec Streamlit
├── README.md                       # Ce fichier README
├── requirements.txt                # Liste des dépendances
└── .github/
    └── workflows/
        └── python-app.yml          # Workflow GitHub Actions pour automatiser les tests
```

## Installation

### Prérequis

- Python 3.x
- pip (gestionnaire de paquets pour Python)

### Étapes d'installation

1. Clonez le projet depuis GitHub :
   ```bash
   git clone <url_du_dépôt>
   cd ImageTextCryptProject
   ```

2. Installez les dépendances du projet :
   ```bash
   pip install -r requirements.txt
   ```

3. (Facultatif) Si vous voulez tester l'application localement avec l'interface Streamlit, exécutez la commande suivante :
   ```bash
   streamlit run app_streamlit.py
   ```

## Utilisation

### Interface graphique avec Streamlit

L'interface vous permet de :

- Crypter et déchiffrer des textes :
  - Entrez un texte à crypter.
  - Une clé secrète est générée automatiquement.
  - Utilisez la même clé pour déchiffrer le texte plus tard.

- Crypter une image :
  - Chargez une image dans l'interface.
  - L'image est convertie en niveaux de gris, puis cryptée.

### Lancement de l'application

Pour lancer l'application avec Streamlit, exécutez :

```bash
streamlit run app_streamlit.py
```

## Tests unitaires

Les tests sont inclus dans le projet pour valider les fonctionnalités de cryptage et déchiffrement des images et des textes.

Pour exécuter les tests, utilisez :

```bash
pytest
```

## Tests automatisés avec GitHub Actions

Le projet est configuré avec GitHub Actions pour exécuter automatiquement les tests à chaque push ou pull request. Le workflow se trouve dans `.github/workflows/python-app.yml`.

## Dépendances

Le projet utilise les bibliothèques suivantes :

- streamlit
- cryptography
- numpy
- matplotlib
- pytest

Toutes les dépendances sont listées dans le fichier `requirements.txt`.

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez proposer des améliorations ou corriger des bugs, n'hésitez pas à ouvrir une issue ou une pull request.

## Licence

Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.