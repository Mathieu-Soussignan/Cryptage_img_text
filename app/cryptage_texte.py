from cryptography.fernet import Fernet

def generer_cle():
    # Générer une clé de cryptage
    return Fernet.generate_key()

def crypter_texte(texte, cle_secrete):
    # Crypter un texte en utilisant une clé secrète
    fernet = Fernet(cle_secrete)
    return fernet.encrypt(texte.encode())

def dechiffrer_texte(texte_crypte, cle_secrete):
    # Déchiffrer un texte en utilisant une clé secrète
    fernet = Fernet(cle_secrete)
    return fernet.decrypt(texte_crypte).decode()