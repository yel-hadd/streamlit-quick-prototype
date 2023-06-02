import streamlit as st

def dashboard():
    st.write("# 📈 Vue d'ensemble")
    st.markdown("### Content de te revoir, " + st.session_state.user["email"] + "!")
    # Create subplot grid for charts
    st.markdown("## Python")
    st.write("Python est un langage de programmation populaire, connu pour sa simplicité et sa polyvalence. Il est largement utilisé pour le développement web, l'analyse de données, l'apprentissage automatique, et bien plus.")