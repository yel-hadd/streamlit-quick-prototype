import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def dashboard():
    heart_rate_data = [60, 65, 70, 75, 80, 85, 90, 95, 100]
    rr_interval_data = [60, 65, 70, 75, 80, 85, 90, 95, 100]
    spo2_data = [60, 65, 70, 75, 80, 85, 90, 95, 100]
    acceleration_data = [60, 65, 70, 75, 80, 85, 90, 95, 100]
    gyro_data = [60, 65, 70, 75, 80, 85, 90, 95, 100]
    orientation_data = [60, 65, 70, 75, 80, 85, 90, 95, 100]
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if st.session_state.user is None:
        st.write("# 👋 Bienvenue sur la page d'accueil")
        st.write("Veuillez vous connecter ou vous inscrire pour continuer")
    else:
        st.write("# 📈 Vue d'ensemble")
        st.markdown("### Content de te revoir, " + st.session_state.user["email"] + "!")
        # Create subplot grid for charts
        fig = make_subplots(
            rows=3,
            cols=2,
            subplot_titles=[
                "SpO2",
                "Fréquence cardiaque",
                "Intervalles R-R",
                "Accélération",
                "Gyroscopie",
                "Orientation",
            ],
        )

        # Add charts to the subplot grid
        fig.add_trace(go.Scatter(x=x, y=spo2_data, name="SpO2"), row=1, col=1)
        fig.add_trace(
            go.Scatter(x=x, y=heart_rate_data, name="Fréquence cardiaque"), row=1, col=2
        )
        fig.add_trace(
            go.Scatter(x=x, y=rr_interval_data, name="Intervalles R-R"), row=2, col=1
        )
        fig.add_trace(
            go.Scatter(x=x, y=acceleration_data, name="Accélération"), row=2, col=2
        )
        fig.add_trace(go.Scatter(x=x, y=gyro_data, name="Gyroscopie"), row=3, col=1)
        fig.add_trace(
            go.Scatter(x=x, y=orientation_data, name="Orientation"), row=3, col=2
        )

        # Update subplot layout
        fig.update_layout(height=800, width=800, title_text="Valeurs des capteurs")

        # Show the plot
        st.plotly_chart(fig)

