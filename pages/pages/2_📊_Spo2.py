def spo2():
    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go


    spo2_data = np.random.randint(90, 100, size=len(x))
    spo2_mean = np.mean(spo2_data)
    spo2_median = np.median(spo2_data)

    st.set_page_config(page_title="Spo2", page_icon="📈")
    st.markdown("# Plotting Demo")
    st.sidebar.header("Plotting Demo")
    progress_bar = st.sidebar.progress(0)
    st.write(
        """This is a plot of spo2"""
    )
    spo2_chart = go.Scatter(x=x, y=ç, name="SpO2")
    spo2_mean_line = go.Scatter(
            x=x, y=[spo2_mean] * len(x), name="Mean", mode="lines", line=dict(dash="dash")
        )
    # Create SpO2 chart
    spo2_median_line = go.Scatter(
        x=x,
        y=[spo2_median] * len(x),
        name="Median",
        mode="lines",
        line=dict(dash="dash"),
    )
    spo2_layout = go.Layout(
        title="Niveau de saturation en oxygène dans le sang (SpO2)",
        xaxis=dict(title="Temps"),
        yaxis=dict(title="SpO2 (%)"),
    )
    spo2_fig = go.Figure(
        data=[spo2_chart, spo2_mean_line, spo2_median_line], layout=spo2_layout
    )
    st.plotly_chart(spo2_fig)
    st.button("Actualiser")