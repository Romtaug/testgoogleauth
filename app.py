import streamlit as st

st.login("google")

if not st.user.is_logged_in:
    st.title("⚡ ThermoData")
    st.button("Se connecter avec Google", on_click=st.login, args=("google",))
    st.stop()

st.title(f"Bonjour {st.user.name} 👋")
st.write(f"Email : {st.user.email}")
st.write("✅ Connexion Google OK")
