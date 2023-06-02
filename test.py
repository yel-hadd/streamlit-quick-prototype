import streamlit as st
import plotly.graph_objects as go
import random
import time

# Initialize the figure
fig = go.Figure()

# Create an empty trace
trace = go.Scatter(x=[], y=[], mode='lines')

# Add the trace to the figure
fig.add_trace(trace)

# Set the layout
fig.update_layout(title='Realtime Line Chart', xaxis_title='Time', yaxis_title='Value')

# Create a Streamlit timer
timer = st.empty()

# Create a Streamlit plot
plot = st.plotly_chart(fig)

while True:
    # Generate random data
    x = time.strftime("%H:%M:%S")
    y = random.randint(0, 10)

    # Update the data
    fig.data[0].x = list(fig.data[0].x) + [x]
    fig.data[0].y = list(fig.data[0].y) + [y]

    # Update the plot
    plot.plotly_chart(fig)

    # Update the timer
    timer.text(f"Last updated: {x}")

    # Wait for 5 seconds
    time.sleep(1)
