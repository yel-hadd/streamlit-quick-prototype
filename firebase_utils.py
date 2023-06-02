import pyrebase

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
