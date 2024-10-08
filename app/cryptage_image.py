from cryptography.fernet import Fernet
from PIL import Image
import io

def crypter_image(nom_image, cle):
    """
    Crypte une image en utilisant Fernet.

    Args:
        nom_image: Le nom du fichier image.
        cle: La clé de cryptage (générée par Fernet).

    Returns:
        Les données de l'image cryptée (bytes).
    """
    f = Fernet(cle)
    with Image.open(nom_image) as image:
        image_data = io.BytesIO()
        image.save(image_data, format=image.format)
        image_bytes = image_data.getvalue()
        encrypted_data = f.encrypt(image_bytes)
    return encrypted_data


def decrypter_image(data_cryptee, cle):
    """
    Décrypte une image cryptée avec Fernet.

    Args:
        data_cryptee: Les données de l'image cryptée (bytes).
        cle: La clé de cryptage utilisée pour crypter l'image.

    Returns:
        Une image décryptée (objet PIL.Image).
    """
    f = Fernet(cle)
    decrypted_data = f.decrypt(data_cryptee)
    image = Image.open(io.BytesIO(decrypted_data))
    return image