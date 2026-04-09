import streamlit as st

if not st.user.is_logged_in:
    st.button("Log in with Google", on_click=st.login, args=["google"])
    st.stop()

st.write("Connecté")
st.write(st.user)

EMAILS_AUTORISES = ["romtaug@gmail.com"]

if st.user.email not in EMAILS_AUTORISES:
    st.error(f"Accès non autorisé : {st.user.email}")
    st.stop()

st.title(f"Bonjour {st.user.name} 👋")
st.write("✅ Accès autorisé")
