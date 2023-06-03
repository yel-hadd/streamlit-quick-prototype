import streamlit as st
import plotly.graph_objects as go
import time
from datetime import datetime
from firebase_utils import database
from plotly.subplots import make_subplots

def combined_charts():
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

    # Initialize the figure and create an empty subplot
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.05)

    # Create empty traces
    trace_ecg = go.Scatter(x=[], y=[], mode='lines', name='Signal ECG')
    trace_spo = go.Scatter(x=[], y=[], mode='lines', name='Niveau de SpO2')
    trace_mvm = go.Scatter(x=[], y=[], mode='lines', name='État de mouvement')

    # Add traces to the subplot
    fig.add_trace(trace_ecg, row=1, col=1)
    fig.add_trace(trace_spo, row=2, col=1)
    fig.add_trace(trace_mvm, row=3, col=1)

    # Set the layout for the subplot
    fig.update_layout(
        title='Graphiques combinés',
        height=1500,
        template='plotly_white',
        xaxis_title="Temps"
    )

    # Create Streamlit timer and plot
    timer = st.empty()
    plot = st.plotly_chart(fig, use_container_width=True)

    # Keep track of the last timestamps fetched
    ecg_last_timestamp = 0
    spo_last_timestamp = 0
    mvm_last_timestamp = 0

    def update_chart():
        nonlocal ecg_last_timestamp
        nonlocal spo_last_timestamp
        nonlocal mvm_last_timestamp

        # Retrieve ECG data from the Firebase Realtime Database starting from the last timestamp
        new_ecg_data = database.child("ecg").order_by_key().start_at(str(ecg_last_timestamp + 1)).get()
        new_spo_data = database.child("spo").order_by_key().start_at(str(spo_last_timestamp + 1)).get()
        new_mvm_data = database.child("mvm").order_by_key().start_at(str(mvm_last_timestamp + 1)).get()

        # Check if there is new ECG data
        if new_ecg_data.each():
            x_ecg = []
            y_ecg = []

            # Retrieve the timestamp and ECG amplitude values
            for data_point in new_ecg_data.each():
                timestamp = int(data_point.key())
                x_ecg.append(datetime.fromtimestamp(timestamp))
                y_ecg.append(data_point.val()["ecg"])
                ecg_last_timestamp = timestamp

            # Update ECG scatter trace with new data
            fig.data[0].x += tuple(x_ecg)
            fig.data[0].y += tuple(y_ecg)

        # Check if there is new SpO2 data
        if new_spo_data.each():
            x_spo = []
            y_spo = []

            # Retrieve the timestamp and SpO2 amplitude values
            for data_point in new_spo_data.each():
                timestamp = int(data_point.key())
                x_spo.append(datetime.fromtimestamp(timestamp))
                y_spo.append(data_point.val()["spo2"])
                spo_last_timestamp = timestamp

            # Update SpO2 scatter trace with new data
            fig.data[1].x += tuple(x_spo)
            fig.data[1].y += tuple(y_spo)

        # Check if there is new motion sensor data
        if new_mvm_data.each():
            x_mvm = []
            y_mvm = []

            # Retrieve the timestamp and motion state values
            for data_point in new_mvm_data.each():
                timestamp = int(data_point.key())
                x_mvm.append(datetime.fromtimestamp(timestamp))
                y_mvm.append(data_point.val()["mvm"])
                mvm_last_timestamp = timestamp

            # Update motion sensor scatter trace with new data
            fig.data[2].x += tuple(x_mvm)
            fig.data[2].y += tuple(y_mvm)

        # Update the plot
        plot.plotly_chart(fig)

        # Update the timer
        last_updated = max(ecg_last_timestamp, spo_last_timestamp, mvm_last_timestamp)
        last_updated_time = datetime.fromtimestamp(last_updated).strftime("%H:%M:%S")
        timer.text(f"Dernière mise à jour : {last_updated_time}")

    while True:
        try:
            update_chart()
        except KeyError:
            pass
        time.sleep(1)


if __name__ == "__main__":
    if st.session_state.page == "Vue générale":
        combined_charts()
