import plotly.graph_objects as go
import numpy as np

# Generate fake data
x = np.arange(0, 10, 0.1)
spo2_data = np.random.randint(90, 100, size=len(x))
heart_rate_data = np.random.randint(60, 100, size=len(x))
rr_interval_data = np.random.uniform(0.6, 1.2, size=len(x))
acceleration_data = np.random.uniform(0, 5, size=len(x))
gyro_data = np.random.uniform(-180, 180, size=len(x))
orientation_data = np.random.uniform(-90, 90, size=len(x))

# Calculate mean and median for each metric
spo2_mean = np.mean(spo2_data)
spo2_median = np.median(spo2_data)

heart_rate_mean = np.mean(heart_rate_data)
heart_rate_median = np.median(heart_rate_data)

rr_interval_mean = np.mean(rr_interval_data)
rr_interval_median = np.median(rr_interval_data)

acceleration_mean = np.mean(acceleration_data)
acceleration_median = np.median(acceleration_data)

gyro_mean = np.mean(gyro_data)
gyro_median = np.median(gyro_data)

orientation_mean = np.mean(orientation_data)
orientation_median = np.median(orientation_data)

# Create SpO2 chart
spo2_chart = go.Scatter(x=x, y=spo2_data, name='SpO2')
spo2_mean_line = go.Scatter(x=x, y=[spo2_mean] * len(x), name='Mean', mode='lines', line=dict(dash='dash'))
spo2_median_line = go.Scatter(x=x, y=[spo2_median] * len(x), name='Median', mode='lines', line=dict(dash='dash'))
spo2_layout = go.Layout(
    title='Niveau de saturation en oxygène dans le sang (SpO2)',
    xaxis=dict(title='Temps'),
    yaxis=dict(title='SpO2 (%)'),
)
spo2_fig = go.Figure(data=[spo2_chart, spo2_mean_line, spo2_median_line], layout=spo2_layout)

# Create heart rate chart
heart_rate_chart = go.Scatter(x=x, y=heart_rate_data, name='Fréquence cardiaque')
heart_rate_mean_line = go.Scatter(x=x, y=[heart_rate_mean] * len(x), name='Mean', mode='lines', line=dict(dash='dash'))
heart_rate_median_line = go.Scatter(x=x, y=[heart_rate_median] * len(x), name='Median', mode='lines', line=dict(dash='dash'))
heart_rate_layout = go.Layout(
    title='Fréquence cardiaque',
    xaxis=dict(title='Temps'),
    yaxis=dict(title='Fréquence cardiaque (bpm)'),
)
heart_rate_fig = go.Figure(data=[heart_rate_chart, heart_rate_mean_line, heart_rate_median_line], layout=heart_rate_layout)

# Create RR interval chart
rr_interval_chart = go.Scatter(x=x, y=rr_interval_data, name='Intervalles R-R')
rr_interval_mean_line = go.Scatter(x=x, y=[rr_interval_mean] * len(x), name='Mean', mode='lines', line=dict(dash='dash'))
rr_interval_median_line = go.Scatter(x=x, y=[rr_interval_median] * len(x), name='Median', mode='lines', line=dict(dash='dash'))
rr_interval_layout = go.Layout(
    title='Intervalles R-R',
    xaxis=dict(title='Temps'),
    yaxis=dict(title='Intervalles R-R (s)'),
)
rr_interval_fig = go.Figure(data=[rr_interval_chart, rr_interval_mean_line, rr_interval_median_line], layout=rr_interval_layout)

# Create acceleration chart
acceleration_chart = go.Scatter(x=x, y=acceleration_data, name='Accélération')
acceleration_mean_line = go.Scatter(x=x, y=[acceleration_mean] * len(x), name='Mean', mode='lines', line=dict(dash='dash'))
acceleration_median_line = go.Scatter(x=x, y=[acceleration_median] * len(x), name='Median', mode='lines', line=dict(dash='dash'))
acceleration_layout = go.Layout(
    title='Accélération',
    xaxis=dict(title='Temps'),
    yaxis=dict(title='Accélération (m/s²)'),
)
acceleration_fig = go.Figure(data=[acceleration_chart, acceleration_mean_line, acceleration_median_line], layout=acceleration_layout)

# Create gyro chart
gyro_chart = go.Scatter(x=x, y=gyro_data, name='Gyroscopie')
gyro_mean_line = go.Scatter(x=x, y=[gyro_mean] * len(x), name='Mean', mode='lines', line=dict(dash='dash'))
gyro_median_line = go.Scatter(x=x, y=[gyro_median] * len(x), name='Median', mode='lines', line=dict(dash='dash'))
gyro_layout = go.Layout(
    title='Gyroscopie',
    xaxis=dict(title='Temps'),
    yaxis=dict(title='Gyroscopie (°/s)'),
)
gyro_fig = go.Figure(data=[gyro_chart, gyro_mean_line, gyro_median_line], layout=gyro_layout)

# Create orientation chart
orientation_chart = go.Scatter(x=x, y=orientation_data, name='Orientation')
orientation_mean_line = go.Scatter(x=x, y=[orientation_mean] * len(x), name='Mean', mode='lines', line=dict(dash='dash'))
orientation_median_line = go.Scatter(x=x, y=[orientation_median] * len(x), name='Median', mode='lines', line=dict(dash='dash'))
orientation_layout = go.Layout(
    title='Orientation spatiale',
    xaxis=dict(title='Temps'),
    yaxis=dict(title='Orientation (°)'),
)
orientation_fig = go.Figure(data=[orientation_chart, orientation_mean_line, orientation_median_line], layout=orientation_layout)

# Display the charts
spo2_fig.show()
heart_rate_fig.show()
rr_interval_fig.show()
acceleration_fig.show()
gyro_fig.show()
orientation_fig.show()
