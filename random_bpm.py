import random
import time
import pyrebase

# Initialize Firebase
config = {
  "apiKey": "AIzaSyAdKv6pcJh-dlpRA44p_6ji6xwdOqB9rwg",
  "authDomain": "naturekine.firebaseapp.com",
  "databaseURL": "https://naturekine-default-rtdb.firebaseio.com",
  "projectId": "naturekine",
  "storageBucket": "naturekine.appspot.com",
  "messagingSenderId": "666122354517",
  "appId": "1:666122354517:web:b007a9b3bc6b2a166139dc",
  "measurementId": "G-Q7KKP82VYP"
}

firebase = pyrebase.initialize_app(config)

# Get the reference to the Realtime Database
database = firebase.database()


# Define a function to write a random bpm value and timestamp to the database
def write_bpm():
    # Generate a random bpm value
    bpm = random.randint(60, 200)

    # Get the current timestamp
    timestamp = int(time.time())

    # Write the bpm value and timestamp to the database
    database.child("bpm").child(timestamp).set({
        "bpm": bpm,
        "timestamp": timestamp
    })

# Start a loop that writes a random bpm value and timestamp to the database every 1 minute
while True:
    write_bpm()
    time.sleep(1)


