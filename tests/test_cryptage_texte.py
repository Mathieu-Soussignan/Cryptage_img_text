from app.cryptage_texte import generer_cle, crypter_texte, dechiffrer_texte

def test_generer_cle():
    # Vérifier que la clé générée n'est pas None
    cle = generer_cle()
    assert cle is not None
    assert len(cle) > 0  # La clé doit avoir une longueur non nulle

def test_crypter_dechiffrer_texte():
    # Générer une clé
    cle = generer_cle()
    
    # Texte à chiffrer
    texte_original = "Ceci est un message secret."
    
    # Crypter le texte
    texte_crypte = crypter_texte(texte_original, cle)
    assert texte_crypte != texte_original  # Le texte chiffré doit être différent du texte original
    
    # Déchiffrer le texte
    texte_decrypte = dechiffrer_texte(texte_crypte, cle)
    assert texte_decrypte == texte_original  # Le texte déchiffré doit correspondre au texte original