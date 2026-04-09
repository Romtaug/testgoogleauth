import streamlit as st

if not st.user.is_logged_in:
    st.button("Log in with Google", on_click=st.login, args=["google"])
    st.stop()

st.write("Connecté")
st.write(st.user)
