import random
import time
from firebase_utils import database


# Define a function to write a random bpm value and timestamp to the database
def write_bpm(timestamp, bpm):
    database.child("bpm").child(timestamp).set({
        "bpm": bpm,
        "timestamp": timestamp
    })


# Function to write data starting from 10 hours in the past
def write_initial_data():
    current_timestamp = int(time.time())

    for minutes in range(600, 0, -1):
        bpm = random.randint(60, 200)
        timestamp = current_timestamp - (minutes * 60)
        write_bpm(timestamp, bpm)
        time.sleep(1)


# Define a function to write a random bpm value and timestamp to the database every minute
def write_bpm_every_minute():
    while True:
        bpm = random.randint(60, 200)
        timestamp = int(time.time())
        write_bpm(timestamp, bpm)
        time.sleep(60)


# Erase existing "bpm" data
database.child("bpm").remove()

# Write data starting from 10 hours in the past
write_initial_data()

# Start writing data every minute
write_bpm_every_minute()
