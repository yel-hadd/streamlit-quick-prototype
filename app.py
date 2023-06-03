import streamlit as st
from dashboard import dashboard
from heart_rate import heart_rate
from firebase_utils import database, auth, firebase
from spo import spo2_level
from ecg import ecg_chart
from motion_sensor import motion_sensor
from vue_generale import combined_charts


# Create session state
if "user" not in st.session_state:
    st.session_state.user = None
if "page" not in st.session_state:
    st.session_state.page = None


def login():
    st.title("Connexion")

    email = st.text_input("Email")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Connexion"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.session_state.user = user
            st.success("Connexion réussie")
            st.experimental_rerun()
        except Exception as e:
            st.error("Email ou mot de passe invalide")


def register():
    st.title("Inscription")

    email = st.text_input("Email")
    password = st.text_input("Mot de passe", type="password")
    confirm_password = st.text_input("Confirmer le mot de passe", type="password")

    if st.button("Register"):
        if password != confirm_password:
            st.error("Les mots de passe ne correspondent pas")
        else:
            try:
                user = auth.create_user_with_email_and_password(email, password)
                st.success("Inscription réussie. Veuillez vous connecter.")
            except Exception as e:
                st.error("Échec de l'inscription")


def logout():
    st.session_state.user = None


def reset_password():

    st.markdown("# Réinitialiser le mot de passe")
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
    if st.session_state.user != None:
        st.sidebar.title("Navigation")
        page_names_to_funcs = {
            "Accueil": dashboard,
            "Capteur SpO2": spo2_level,
            "Capteur ECG": ecg_chart,
            "Capteur de mouvement": motion_sensor,
            "Graphiques combinés": combined_charts,
        }

        choice = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
        st.sidebar.button("Déconnexion", on_click=logout)
        st.session_state.page = choice
        page_names_to_funcs[choice]()
    else:
        side = st.sidebar.title("Authentification")
        choice = None
        auth_pages = ["Connexion", "Inscription", "Réinitialisation du mot de passe"]
        auth_choice = st.sidebar.radio("", auth_pages)
        if auth_choice == "Connexion":
            login()
        elif auth_choice == "Inscription":
            register()
        elif auth_choice == "Réinitialisation du mot de passe":
            reset_password()


if __name__ == "__main__":
    main()
