import streamlit as st
import plotly.graph_objects as go
import time
from datetime import datetime
from firebase_utils import database

def spo2_level():
    hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.markdown("<style>#main { display: none; }</style>", unsafe_allow_html=True)
    
    # Initialize the figure
    fig = go.Figure()

    # Create an empty trace
    trace = go.Scatter(x=[], y=[], mode='lines', name='Niveau de SpO2')

    # Add the trace to the figure
    fig.add_trace(trace)

    # Set the layout
    fig.update_layout(
        title='Niveau de SpO2',
        xaxis_title='Temps',
        yaxis_title='SpO2 (%)',
        xaxis=dict(type='date', tickformat='%H:%M:%S'),
        margin=dict(l=40, r=40, t=40, b=40),
        autosize=True,
        height=500,
        template='plotly_white'
    )

    # Create a Streamlit timer
    timer = st.empty()

    # Create a Streamlit plot
    plot = st.plotly_chart(fig, use_container_width=True)

    # Keep track of the last timestamp fetched
    last_timestamp = 0

    def update_chart():
        nonlocal last_timestamp

        # Retrieve SpO2 data from the Firebase Realtime Database starting from the last timestamp
        new_spo2_data = database.child("spo").order_by_key().start_at(str(last_timestamp + 1)).get()

        # Check if there is new data
        if new_spo2_data.each():
            x = []
            y = []

            # Retrieve the timestamp and SpO2 level values
            for data_point in new_spo2_data.each():
                timestamp = int(data_point.key())
                x.append(datetime.fromtimestamp(timestamp))
                y.append(data_point.val()["spo2"])
                last_timestamp = timestamp

            # Update the scatter trace with new data
            fig.data[0].x += tuple(x)
            fig.data[0].y += tuple(y)

            # Update the plot
            plot.plotly_chart(fig)

            # Update the timer
            last_updated = datetime.fromtimestamp(last_timestamp).strftime("%H:%M:%S")
            timer.text(f"Dernière mise à jour : {last_updated}")

    while True:
        try:
            update_chart()
        except KeyError:
            pass
        time.sleep(1)

if __name__ == "__main__":
    spo2_level()
