import streamlit as st
import pyrebase
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots
from datetime import datetime
from time import sleep

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
  "apiKey": "AIzaSyAdKv6pcJh-dlpRA44p_6ji6xwdOqB9rwg",
  "authDomain": "naturekine.firebaseapp.com",
  "databaseURL": "https://naturekine-default-rtdb.firebaseio.com",
  "projectId": "naturekine",
  "storageBucket": "naturekine.appspot.com",
  "messagingSenderId": "666122354517",
  "appId": "1:666122354517:web:b007a9b3bc6b2a166139dc",
  "measurementId": "G-Q7KKP82VYP"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
database = firebase.database()
auth = firebase.auth()

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
# MainMenu {visibility: hidden;}
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Create session state
if "user" not in st.session_state:
    st.session_state.user = None


def dashboard():
    import streamlit as st
    import pyrebase
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    if st.session_state.user is None:
        st.title("Home")
        st.write("# 👋 Bienvenue sur la page d'accueil")
        st.write("Veuillez vous connecter ou vous inscrire pour continuer")
    else:
        st.title("Dashboard")
        st.markdown("### Content de te revoir, " + st.session_state.user["email"] + "!")
        st.write("## 📈 Vue d'ensemble")
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


def login():
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
            print(e)
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


def spo2():
    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go

    spo2_data = np.random.randint(90, 100, size=len(x))
    spo2_mean = np.mean(spo2_data)
    spo2_median = np.median(spo2_data)

    st.markdown("# Spo2")
    st.write("""This is a plot of spo2""")
    spo2_chart = go.Scatter(x=x, y=spo2_data, name="SpO2")
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


def heart_rate():
    import streamlit as st
    import plotly.graph_objects as go
    import time

    st.markdown("# Fréquence cardiaque")
    st.write("This is a plot of heart rate")

    # Create a new figure for the heart rate chart
    fig = go.Figure()

    # Keep track of the last timestamp fetched
    last_timestamp = 0

    # Retrieve data from the database and update the chart
    def update_chart():
        nonlocal last_timestamp

        # Retrieve new data from the database starting from the last timestamp
        bpm_data = database.child("bpm").order_by_key().start_at(f"{last_timestamp}").get()

        if bpm_data.each():
            x = []
            y = []
            for data_point in bpm_data.each():
                timestamp = int(data_point.key())
                x.append(datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S"))
                y.append(data_point.val()["bpm"])
                last_timestamp = timestamp  # Update the last timestamp fetched

            fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Fréquence cardiaque"))
            st.plotly_chart(fig)
        else:
            st.write("No new data available")

    # Call the update function initially
    update_chart()

    # Periodically update the chart with new data
    while True:
        time.sleep(1)  # Wait for 30 seconds
        st.experimental_rerun()

def rr_intervals():
    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go

    x = np.arange(0, 10, 0.1)
    rr_intervals_data = np.random.randint(60, 100, size=len(x))
    rr_intervals_mean = np.mean(rr_intervals_data)
    rr_intervals_median = np.median(rr_intervals_data)
    st.markdown("# Intervalles R-R")
    st.write("This is a plot of rr_intervals")
    # Create rr_intervals chart
    rr_intervals_chart = go.Scatter(x=x, y=rr_intervals_data, name="Intervalles R-R")
    rr_intervals_mean_line = go.Scatter(
        x=x,
        y=[rr_intervals_mean] * len(x),
        name="Mean",
        mode="lines",
        line=dict(dash="dash"),
    )
    rr_intervals_median_line = go.Scatter(
        x=x,
        y=[rr_intervals_median] * len(x),
        name="Median",
        mode="lines",
        line=dict(dash="dash"),
    )
    rr_intervals_layout = go.Layout(
        title="Intervalles R-R",
        xaxis=dict(title="Temps"),
        yaxis=dict(title="Intervalles R-R (ms)"),
    )
    rr_intervals_fig = go.Figure(
        data=[rr_intervals_chart, rr_intervals_mean_line, rr_intervals_median_line],
        layout=rr_intervals_layout,
    )
    st.plotly_chart(rr_intervals_fig)
    st.button("Actualiser")


def acceleration():
    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go

    x = np.arange(0, 10, 0.1)
    acceleration_data = np.random.randint(60, 100, size=len(x))
    acceleration_mean = np.mean(acceleration_data)
    acceleration_median = np.median(acceleration_data)
    st.markdown("# Accélération")
    st.write("This is a plot of acceleration")
    # Create acceleration chart
    acceleration_chart = go.Scatter(x=x, y=acceleration_data, name="Accélération")
    acceleration_mean_line = go.Scatter(
        x=x,
        y=[acceleration_mean] * len(x),
        name="Mean",
        mode="lines",
        line=dict(dash="dash"),
    )
    acceleration_median_line = go.Scatter(
        x=x,
        y=[acceleration_median] * len(x),
        name="Median",
        mode="lines",
        line=dict(dash="dash"),
    )
    acceleration_layout = go.Layout(
        title="Accélération",
        xaxis=dict(title="Temps"),
        yaxis=dict(title="Accélération (m/s²)"),
    )
    acceleration_fig = go.Figure(
        data=[acceleration_chart, acceleration_mean_line, acceleration_median_line],
        layout=acceleration_layout,
    )
    st.plotly_chart(acceleration_fig)
    st.button("Actualiser")


def gyroscope():
    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go

    x = np.arange(0, 10, 0.1)
    gyroscope_data = np.random.randint(60, 100, size=len(x))
    gyroscope_mean = np.mean(gyroscope_data)
    gyroscope_median = np.median(gyroscope_data)
    st.markdown("# Gyroscope")
    st.write("This is a plot of gyroscope")
    # Create gyroscope chart
    gyroscope_chart = go.Scatter(x=x, y=gyroscope_data, name="Gyroscope")
    gyroscope_mean_line = go.Scatter(
        x=x,
        y=[gyroscope_mean] * len(x),
        name="Mean",
        mode="lines",
        line=dict(dash="dash"),
    )
    gyroscope_median_line = go.Scatter(
        x=x,
        y=[gyroscope_median] * len(x),
        name="Median",
        mode="lines",
        line=dict(dash="dash"),
    )
    gyroscope_layout = go.Layout(
        title="Gyroscope",
        xaxis=dict(title="Temps"),
        yaxis=dict(title="Gyroscope (°/s)"),
    )
    gyroscope_fig = go.Figure(
        data=[gyroscope_chart, gyroscope_mean_line, gyroscope_median_line],
        layout=gyroscope_layout,
    )
    st.plotly_chart(gyroscope_fig)
    st.button("Actualiser")


def orientation():
    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go

    x = np.arange(0, 10, 0.1)
    orientation_data = np.random.randint(60, 100, size=len(x))
    orientation_mean = np.mean(orientation_data)
    orientation_median = np.median(orientation_data)
    st.markdown("# Orientation")
    st.write("This is a plot of orientation")
    # Create orientation chart
    orientation_chart = go.Scatter(x=x, y=orientation_data, name="Orientation")
    orientation_mean_line = go.Scatter(
        x=x,
        y=[orientation_mean] * len(x),
        name="Mean",
        mode="lines",
        line=dict(dash="dash"),
    )
    orientation_median_line = go.Scatter(
        x=x,
        y=[orientation_median] * len(x),
        name="Median",
        mode="lines",
        line=dict(dash="dash"),
    )
    orientation_layout = go.Layout(
        title="Orientation",
        xaxis=dict(title="Temps"),
        yaxis=dict(title="Orientation (°)"),
    )
    orientation_fig = go.Figure(
        data=[orientation_chart, orientation_mean_line, orientation_median_line],
        layout=orientation_layout,
    )
    st.plotly_chart(orientation_fig)
    st.button("Actualiser")


def reset_password():
    import streamlit as st

    st.markdown("# Reset Password")
    st.write("This is a form to reset password")
    form = st.form("Saisissez votre Email ici", True)
    email = form.text_input("Email")
    submitted = form.form_submit_button("Réinitialiser le mot de passe")
    if submitted:
        if email == "":
            st.error("Veuillez saisir votre email")
            return
        try:
            auth.send_password_reset_email(email)
        except Exception as e:
            pass
        st.success(
            "Si {} existe dans notre base de données, un lien de réinitialisation du mot de passe sera envoyé".format(
                email
            )
        )


# Main function
def main():
    # st.set_page_config(page_title="Simple App", page_icon="📈")
    side = st.sidebar.title("Navigation")
    if st.session_state.user != None:
        # choice = st.sidebar.selectbox("Go to", pages)
        page_names_to_funcs = {
            "Accueil": dashboard,
            "Spo2": spo2,
            "Fréquence cardiaque": heart_rate,
            "Intervalles R-R": rr_intervals,
            "Accélération": acceleration,
            "Gyroscopie": gyroscope,
            "Orientation": orientation,
        }

        choice = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
        page_names_to_funcs[choice]()
        st.sidebar.button("Logout", on_click=logout)
    else:
        choice = None
        auth_pages = ["Connexion", "Inscription", "Réinitialisation du mot de passe"]
        auth_choice = st.sidebar.radio("Authentification", auth_pages)
        if auth_choice == "Connexion":
            login()
        elif auth_choice == "Inscription":
            register()
        elif auth_choice == "Réinitialisation du mot de passe":
            reset_password()


if __name__ == "__main__":
    main()
