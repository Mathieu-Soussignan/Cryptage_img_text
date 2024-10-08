# Projet de Cryptage d'Images et de Textes

## Table des matières
- [Description](#description)
- [Fonctionnalités](#fonctionnalités)
- [Structure du projet](#structure-du-projet)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Tests](#tests)
- [Dépendances](#dépendances)
- [Contribution](#contribution)
- [Licence](#licence)

## Description

Ce projet permet de crypter et de déchiffrer des images et des textes en utilisant des techniques de cryptage symétrique avec la bibliothèque `cryptography` (via Fernet). Une interface graphique interactive a été développée avec Streamlit, permettant une utilisation facile via une interface web.

## Fonctionnalités

- Cryptage et décryptage d'images avec une clé Fernet
- Cryptage et déchiffrement de textes avec une clé secrète générée
- Téléchargement des résultats cryptés (texte ou image)
- Interface utilisateur conviviale via Streamlit

## Structure du projet

```
Cryptage_img_text/
├── app/
│   ├── __init__.py
│   ├── cryptage_image.py
│   └── cryptage_texte.py
├── images/
│   └── example.jpg
├── tests/
│   ├── test_cryptage_image.py
│   └── test_cryptage_texte.py
├── app_streamlit.py
├── README.md
├── requirements.txt
└── .github/
    └── workflows/
        └── python-app.yml
```

## Installation

### Prérequis
- Python 3.x
- pip

### Étapes
1. Cloner le projet :
   ```bash
   git clone <url_du_dépôt>
   cd ImageTextCryptProject
   ```
2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Lancer l'application (optionnel) :
   ```bash
   streamlit run app_streamlit.py
   ```

## Utilisation

### Interface Streamlit
- **Cryptage d'images** : Chargez une image, générez une clé Fernet, cryptez l'image.
- **Décryptage d'images** : Utilisez la même clé pour décrypter l'image.
- **Cryptage/Déchiffrement de texte** : Entrez du texte, générez une clé, cryptez/décryptez.
- **Téléchargement** : Téléchargez les résultats cryptés ou décryptés.

### Lancement
```bash
streamlit run app_streamlit.py
```

## Tests

Exécutez les tests unitaires avec :
```bash
pytest
```

Les tests sont automatiquement exécutés via GitHub Actions à chaque push ou pull request.

## Dépendances

- Streamlit
- cryptography
- Pillow (PIL)
- numpy
- matplotlib
- pytest

Voir `requirements.txt` pour la liste complète.

## Contribution

Les contributions sont bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request pour des améliorations ou des corrections.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.