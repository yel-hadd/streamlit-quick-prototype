import streamlit as st
import pyrebase
from PIL import Image


login_icon = Image.open("assets/login.png")
register_icon = Image.open("assets/register.png")
logout_icon = Image.open("assets/logout.png")

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
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Create session state
if 'user' not in st.session_state:
    st.session_state.user = None

def home():
    if st.session_state.user == None:
        st.title("Home")
        st.write("# Welcome to the Home Page")
        st.write("Please log in or register to continue")
    else:
        st.title("Dashboard")
        st.write("# Welcome to the Home Page")
        st.write("You are logged in")

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
    st.experimental_rerun()

# Main function
def main():
    side = st.sidebar.title("Navigation")
    if st.session_state.user != None:
        pages = ["Dashboard", "Sensor 1", "Sensor 2", "Sensor 3", "Sensor 4"]
        st.sidebar.selectbox("Go to", pages)
        choice = 'Dashboard'
    else:
        pages = ["Dashboard"]
        choice = None
    auth_pages = ["Login", "Register", "logout"]
    auth_choice = st.sidebar.radio("Go to", auth_pages)

    if choice == "Dashboard" and st.session_state.user != None:
        home()
    elif auth_choice == "Login":
        login(pages)
    elif auth_choice == "Register":
        register()

if __name__ == "__main__":
    main()
