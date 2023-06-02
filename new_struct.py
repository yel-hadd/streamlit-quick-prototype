import streamlit as st
import pyrebase
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots
from datetime import datetime
from time import sleep
from firebase_utils import database, auth, firebase

# Generate fake data
x = np.arange(0, 10, 0.1)
heart_rate_data = np.random.randint(60, 100, size=len(x))
heart_rate_mean = np.mean(heart_rate_data)
heart_rate_median = np.median(heart_rate_data)


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






