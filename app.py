import streamlit as st
from dashboard import dashboard
from heart_rate import heart_rate
from firebase_utils import database, auth, firebase


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

def reset_password():

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
    if st.session_state.user != None:
        side = st.sidebar.title("Navigation")
        # choice = st.sidebar.selectbox("Go to", pages)
        page_names_to_funcs = {
            "Accueil": dashboard,
            "Fréquence cardiaque": heart_rate,
        }

        choice = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
        page_names_to_funcs[choice]()
        st.sidebar.button("Logout", on_click=logout)
    else:
        side = st.sidebar.title("Authentification")
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