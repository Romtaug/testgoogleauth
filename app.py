import streamlit as st
import streamlit_authenticator as stauth

name = "Rom"
username = "romtaug"
password = "motdepassefort"

hashed_password = stauth.Hasher.hash(password)

credentials = {
    "usernames": {
        username: {
            "name": name,
            "password": hashed_password,
        }
    }
}

authenticator = stauth.Authenticate(
    credentials=credentials,
    cookie_name="app_cookie",
    cookie_key="une_cle_secrete_tres_longue_et_aleatoire",
    cookie_expiry_days=30,
)

authenticator.login(location="main", key="Login")

authentication_status = st.session_state.get("authentication_status")
name = st.session_state.get("name")

if authentication_status is False:
    st.error("Identifiant ou mot de passe incorrect")
elif authentication_status is None:
    st.warning("Veuillez vous connecter")
else:
    authenticator.logout(location="sidebar", key="Logout")
    st.title(f"Bonjour {name} 👋")
    st.write("✅ Accès autorisé")
