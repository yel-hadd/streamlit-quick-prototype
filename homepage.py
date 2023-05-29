import streamlit as st
import pyrebase

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

def login():
    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.success(f"Logged in as {user['email']}")
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

# Main function
def main():
    st.sidebar.title("Authentication")
    choice = st.sidebar.radio("Select Option", ["Login", "Register"])

    if choice == "Login":
        login()
    elif choice == "Register":
        register()

if __name__ == "__main__":
    main()
