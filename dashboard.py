import streamlit as st

def dashboard():
    st.write("# 📈 Naturekine")
    st.markdown("### Content de te revoir, " + st.session_state.user["email"] + "!")
    # Create subplot grid for charts
    st.write("Naturekine est une plateforme révolutionnaire qui facilite l'évolution physiologique des athlètes grâce à la visualisation des données. En utilisant les capteurs SpO2, ECG et de mouvement, Naturekine génère des diagrammes informatifs, permettant aux athlètes de comprendre, d'optimiser et de maximiser leurs performances sportives de manière personnalisée et précise.")