import streamlit as st
import pyrebase
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots

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

# Firebase configuration
firebase_config = {
  'apiKey': "AIzaSyBsXCCqwqgPe9xpq02yTgBg6Q2NQ84j5M8",
  'authDomain': "stats-ed9ac.firebaseapp.com",
  'projectId': "stats-ed9ac",
  'storageBucket': "stats-ed9ac.appspot.com",
  'messagingSenderId': "801682877749",
  'appId': "1:801682877749:web:7356a7790744adbc0cf07c",
  'measurementId': "G-8RE2DQ397C",
  'databaseURL': None
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
            #MainMenu {visibility: hidden;}
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Create session state
if 'user' not in st.session_state:
    st.session_state.user = None

def home():
    if st.session_state.user is None:
        st.title("Home")
        st.write("# Welcome to the Home Page")
        st.write("Please log in or register to continue")
    else:
        st.title("Dashboard")
        st.markdown("### Welcome back, " + st.session_state.user['email'] + "!")
        
        # Create subplot grid for charts
        fig = make_subplots(rows=3, cols=2, subplot_titles=[
            "SpO2", "Fréquence cardiaque",
            "Intervalles R-R", "Accélération",
            "Gyroscopie", "Orientation"
        ])

        # Add charts to the subplot grid
        fig.add_trace(go.Scatter(x=x, y=spo2_data, name='SpO2'), row=1, col=1)
        fig.add_trace(go.Scatter(x=x, y=heart_rate_data, name='Fréquence cardiaque'), row=1, col=2)
        fig.add_trace(go.Scatter(x=x, y=rr_interval_data, name='Intervalles R-R'), row=2, col=1)
        fig.add_trace(go.Scatter(x=x, y=acceleration_data, name='Accélération'), row=2, col=2)
        fig.add_trace(go.Scatter(x=x, y=gyro_data, name='Gyroscopie'), row=3, col=1)
        fig.add_trace(go.Scatter(x=x, y=orientation_data, name='Orientation'), row=3, col=2)

        # Update subplot layout
        fig.update_layout(height=800, width=800, title_text="Valeurs des capteurs")

        # Show the plot
        st.plotly_chart(fig)


def login(pages):
    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.session_state.user = user
            st.success("Login successful")
            st.experimental_rerun()
        except Exception as e:
            st.error("Invalid email or password")

def register():
    st.title("Register")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if password != confirm_password:
            st.error("Passwords do not match")
        else:
            try:
                user = auth.create_user_with_email_and_password(email, password)
                st.success("Registration successful. Please log in.")
            except Exception as e:
                st.error("Registration failed")

def logout():
    st.session_state.user = None

# Main function
def main():
    side = st.sidebar.title("Navigation")
    if st.session_state.user != None:
        pages = ["Dashboard", "Sensor 1", "Sensor 2", "Sensor 3", "Sensor 4"]
        st.sidebar.selectbox("Go to", pages)
        choice = 'Dashboard'
        st.sidebar.button("Logout", on_click=logout)
    else:
        pages = ["Dashboard"]
        choice = None
        auth_pages = ["Login", "Register"]
        auth_choice = st.sidebar.radio("Go to", auth_pages)

    if choice == "Dashboard" and st.session_state.user != None:
        home()
    elif auth_choice == "Login":
        login(pages)
    elif auth_choice == "Register":
        register()

if __name__ == "__main__":
    main()
