import numpy as np
import sys
import os

# Ajoutez le chemin du dossier parent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.cryptage_image import charger_image, convertir_en_gris, crypter_image

def test_charger_image():
    # Tester si l'image est correctement chargée
    image = charger_image('../images/example.jpg')
    print("Image chargée:", image.shape)  # Ajout d'un print pour afficher la forme de l'image
    assert image is not None
    assert len(image.shape) == 3  # Vérifier que l'image est bien en 3D (RGB)

def test_conversion_en_gris():
    # Charger une image couleur
    image = charger_image('../images/example.jpg')
    print("Image couleur chargée:", image.shape)  # Ajout d'un print pour afficher la forme de l'image couleur
    
    # Convertir en niveaux de gris
    image_gris = convertir_en_gris(image)
    print("Image convertie en niveaux de gris:", image_gris.shape)  # Ajout d'un print pour afficher la forme de l'image en niveaux de gris
    
    # Vérifier que l'image a bien été convertie en niveaux de gris
    assert len(image_gris.shape) == 2  # L'image en niveaux de gris doit être en 2D

def test_crypter_image():
    # Charger une image couleur
    image = charger_image('../images/example.jpg')
    print("Image couleur chargée pour le cryptage:", image.shape)  # Ajout d'un print pour afficher la forme de l'image couleur
    
    # Crypter l'image
    image_cryptee = crypter_image(image)
    print("Image cryptée:", image_cryptee.shape)  # Ajout d'un print pour afficher la forme de l'image cryptée
    
    # Vérifier que l'image cryptée a bien été transformée
    assert image_cryptee is not None
    assert len(image_cryptee.shape) == 2  # Le résultat doit être une image en 2D
    assert np.any(image_cryptee)  # Vérifier que le tableau n'est pas vide