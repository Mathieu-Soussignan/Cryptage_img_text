import numpy as np
import matplotlib.image as mpimg

def charger_image(image_path):
    # Charger une image depuis le chemin fourni
    return mpimg.imread(image_path)

def convertir_en_gris(image):
    # Convertir une image en niveaux de gris
    return np.mean(image, axis=2) if len(image.shape) == 3 else image

def crypter_image(image):
    return np.sum(image, axis=2) if len(image.shape) == 3 else image