import numpy as np
import sys
import os

# Ajoutez le chemin du dossier parent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.cryptage_image import charger_image, convertir_en_gris, crypter_image

def test_charger_image():
    # Tester si l'image est correctement chargée
    image = charger_image('images/example.jpg')
    assert image is not None
    assert len(image.shape) == 3  # Vérifier que l'image est bien en 3D (RGB)

def test_conversion_en_gris():
    # Charger une image couleur
    image = charger_image('images/example.jpg')
    
    # Convertir en niveaux de gris
    image_gris = convertir_en_gris(image)    
    # Vérifier que l'image a bien été convertie en niveaux de gris
    assert len(image_gris.shape) == 2  # L'image en niveaux de gris doit être en 2D

def test_crypter_image():
    # Charger une image couleur
    image = charger_image('images/example.jpg')
    
    # Crypter l'image
    image_cryptee = crypter_image(image)
    
    # Vérifier que l'image cryptée a bien été transformée
    assert image_cryptee is not None
    assert len(image_cryptee.shape) == 2  # Le résultat doit être une image en 2D
    assert np.any(image_cryptee)  # Vérifier que le tableau n'est pas vide