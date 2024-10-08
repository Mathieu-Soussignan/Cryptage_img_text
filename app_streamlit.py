import streamlit as st
import numpy as np
from app.cryptage_image import charger_image, convertir_en_gris, crypter_image
from app.cryptage_texte import generer_cle, crypter_texte, dechiffrer_texte
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Cryptage d'Image et de Texte")

# Choix du type de cryptage
choix = st.radio("Que souhaitez-vous crypter ?", ("Image", "Texte"))

# Crypter une image
if choix == "Image":
    st.subheader("Cryptage d'une Image")
    
    # Charger l'image
    uploaded_file = st.file_uploader("Choisissez une image", type=["jpg", "png"])
    
    if uploaded_file is not None:
        # Lire l'image
        image = plt.imread(uploaded_file)
        
        # Afficher l'image originale
        st.image(image, caption="Image originale", use_column_width=True)
        
        # Convertir en niveaux de gris
        image_gris = convertir_en_gris(image)
        
        # Normalisation des valeurs de l'image entre 0 et 1
        image_gris = image_gris / 255.0
        
        st.image(image_gris, caption="Image en niveaux de gris", use_column_width=True)

        # Crypter l'image
        image_cryptee = crypter_image(image)
        
        # Normalisation de l'image cryptée si nécessaire
        if np.max(image_cryptee) > 1.0:
            image_cryptee = image_cryptee / np.max(image_cryptee)
        
        st.image(image_cryptee, caption="Image cryptée", use_column_width=True)

# Crypter un texte
if choix == "Texte":
    st.subheader("Cryptage d'un Texte")
    
    # Entrer le texte à crypter ou déchiffrer
    texte = st.text_area("Entrez le texte à crypter ou déchiffrer", value="")
    
    # Choix d'action: Crypter ou Déchiffrer
    action = st.radio("Choisissez l'action", ("Crypter", "Déchiffrer"))
    
    if action == "Crypter":
        # Générer une clé secrète pour le cryptage
        if "cle_secrete" not in st.session_state:
            st.session_state["cle_secrete"] = generer_cle()  # La clé est stockée en session
        
        cle_secrete = st.session_state["cle_secrete"]  # Récupérer la clé depuis la session
        st.write("Clé secrète générée : ", cle_secrete.decode('utf-8'))  # Afficher la clé sous forme de chaîne
        
        if texte:
            # Crypter le texte
            texte_crypte = crypter_texte(texte, cle_secrete)
            texte_crypte_str = texte_crypte.decode('utf-8')  # Convertir les bytes en chaîne pour l'affichage
            st.write("Texte crypté : ", texte_crypte_str)
            
            # Option de téléchargement du texte crypté (sous forme de chaîne)
            st.download_button(label="Télécharger le texte crypté", data=texte_crypte_str, file_name="texte_crypte.txt", mime="text/plain")

    if action == "Déchiffrer":
        # Saisie manuelle de la clé secrète pour le déchiffrement
        cle_saisie = st.text_input("Entrez la clé secrète utilisée pour le cryptage")
        
        if texte and cle_saisie:
            try:
                # Reconversion de la clé saisie en bytes
                cle_secrete = cle_saisie.encode('utf-8')
                
                # Reconversion du texte chiffré en bytes
                texte_crypte_bytes = texte.encode('utf-8')  # Texte reçu comme chaîne, reconverti en bytes
                
                # Déchiffrer le texte
                texte_decrypte = dechiffrer_texte(texte_crypte_bytes, cle_secrete)
                st.write("Texte déchiffré : ", texte_decrypte)
            except Exception as e:
                st.error(f"Erreur lors du déchiffrement : {e}. Assurez-vous que le texte et la clé sont corrects.")

