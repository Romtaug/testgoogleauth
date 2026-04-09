import streamlit as st
import streamlit_authenticator as stauth

names = ["Rom"]
usernames = ["romtaug"]
passwords = ["motdepassefort"]

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(
    dict(credentials=dict(usernames={
        usernames[0]: dict(name=names[0], password=hashed_passwords[0])
    })),
    "app_cookie",
    "une_signature_tres_longue_et_aleatoire",
    cookie_expiry_days=30,
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status is False:
    st.error("Identifiant ou mot de passe incorrect")
elif authentication_status is None:
    st.warning("Entrez vos identifiants")
elif authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.title(f"Bonjour {name} 👋")
    st.write("✅ Accès autorisé")
