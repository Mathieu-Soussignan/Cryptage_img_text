import numpy as np
import sys
import os
from cryptography.fernet import Fernet
from app.cryptage_image import crypter_image, decrypter_image
from PIL import Image
import io

# Ajoutez le chemin du dossier parent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_crypter_image():
    """
    Teste le cryptage d'une image avec Fernet.
    """
    # Générer une clé Fernet
    cle = Fernet.generate_key()
    
    # Chemin vers l'image de test
    nom_image = 'images/example.jpg'
    
    # Crypter l'image
    image_cryptee = crypter_image(nom_image, cle)
    
    # Vérifier que les données cryptées ne sont pas vides
    assert image_cryptee is not None
    assert len(image_cryptee) > 0

def test_decrypter_image():
    """
    Teste le décryptage d'une image avec Fernet.
    """
    # Générer une clé Fernet
    cle = Fernet.generate_key()

    # Chemin vers l'image de test
    nom_image = 'images/example.jpg'

    # Crypter puis décrypter l'image
    image_cryptee = crypter_image(nom_image, cle)
    image_decryptee = decrypter_image(image_cryptee, cle)

    # Vérifier que l'image décryptée est un objet Image
    assert isinstance(image_decryptee, Image.Image)

    # Vérifier que l'image décryptée peut être sauvegardée et a une taille non nulle
    image_data = io.BytesIO()
    image_decryptee.save(image_data, format="PNG")
    assert image_data.tell() > 0