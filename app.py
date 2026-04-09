import streamlit as st

st.login("google")

if not st.user.is_logged_in:
    st.stop()

EMAILS_AUTORISES = [
    "romtaug@gmail.com",
]

if st.user.email not in EMAILS_AUTORISES:
    st.error(f"Accès non autorisé : {st.user.email}")
    st.stop()

st.title(f"Bonjour {st.user.name} 👋")
st.write("✅ Accès autorisé")
