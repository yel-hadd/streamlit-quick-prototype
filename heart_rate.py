import streamlit as st
import plotly.graph_objects as go
import time
from datetime import datetime
from firebase_utils import database

def heart_rate():
    st.markdown("# Fréquence cardiaque")
    st.write("This is a plot of heart rate")

    # Create a new figure for the heart rate chart
    fig = go.Figure()

    # Retrieve initial data from the database
    bpm_data = database.child("bpm").order_by_key().get()
    x = []
    y = []
    for data_point in bpm_data.each():
        timestamp = int(data_point.key())
        x.append(datetime.fromtimestamp(timestamp))
        y.append(data_point.val()["bpm"])

    # Create an initial scatter trace for heart rate data
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Fréquence cardiaque"))

    # Set the x-axis type to 'date'
    fig.update_xaxes(type="date")

    # Show the initial chart
    chart_shown = False

    # Keep track of the last timestamp fetched
    last_timestamp = max([int(data_point.key()) for data_point in bpm_data.each()])

    # Function to update the chart with new data
    def update_chart():
        nonlocal last_timestamp, chart_shown

        # Retrieve new data from the database starting from the last timestamp
        new_bpm_data = database.child("bpm").order_by_key().start_at(str(last_timestamp + 1)).get()

        if new_bpm_data.each():
            new_x = []
            new_y = []
            for data_point in new_bpm_data.each():
                timestamp = int(data_point.key())
                new_x.append(datetime.fromtimestamp(timestamp))
                new_y.append(data_point.val()["bpm"])
                last_timestamp = timestamp  # Update the last timestamp fetched

            # Update the scatter trace with new data
            fig.add_trace(go.Scatter(x=new_x, y=new_y, mode="lines", name="Fréquence cardiaque"))

            if not chart_shown:
                # Show the updated chart only for the first time
                st.plotly_chart(fig)
                chart_shown = True

    # Call the update function initially
    update_chart()


if __name__ == "__main__":
    heart_rate()
