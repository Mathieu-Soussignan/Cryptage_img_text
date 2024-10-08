import streamlit as st
from cryptography.fernet import Fernet
from PIL import Image
import io
from app.cryptage_image import crypter_image, decrypter_image

# Titre de l'application
st.title("Cryptage d'Image avec Fernet")

# Générer une clé unique pour le cryptage
if 'cle' not in st.session_state:
    st.session_state['cle'] = Fernet.generate_key()

cle = st.session_state['cle']

# Choix de l'action (Crypter ou Déchiffrer)
choix = st.radio("Choisissez l'action", ("Crypter", "Déchiffrer"))

# Crypter une image
if choix == "Crypter":
    st.subheader("Crypter une Image")

    uploaded_file = st.file_uploader("Choisissez une image", type=["jpg", "png"])
    if uploaded_file is not None:
        # Crypter l'image
        image_cryptee = crypter_image(uploaded_file, cle)
        taille_cryptee = len(image_cryptee)
        st.write(f"Taille du fichier crypté : {taille_cryptee} octets")

        # Télécharger les données cryptées
        st.download_button(
            label="Télécharger l'image cryptée",
            data=image_cryptee,
            file_name="image_cryptee.bin",
            mime="application/octet-stream"
        )

# Décrypter une image
if choix == "Déchiffrer":
    st.subheader("Déchiffrer une Image")

    uploaded_encrypted_file = st.file_uploader("Téléchargez l'image cryptée", type=["bin"])
    if uploaded_encrypted_file is not None:
        # Lire les données cryptées
        data_cryptee = uploaded_encrypted_file.read()

        # Décrypter l'image
        image_decryptee = decrypter_image(data_cryptee, cle)

        # Afficher l'image décryptée
        st.image(image_decryptee, caption="Image déchiffrée", use_column_width=True)

        # Option de télécharger l'image décryptée
        img_data = io.BytesIO()
        image_decryptee.save(img_data, format='PNG')
        img_data = img_data.getvalue()

        st.download_button(
            label="Télécharger l'image déchiffrée",
            data=img_data,
            file_name="image_decryptee.png",
            mime="image/png"
        )