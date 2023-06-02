import random
import time
from firebase_utils import database


# Define a function to write a random bpm value and timestamp to the database
def write_bpm(timestamp, bpm):
    database.child("bpm").child(timestamp).set({
        "bpm": bpm,
        "timestamp": timestamp
    })
    print("BPM: " + str(bpm))

def write_spo(timestamp, bpm):
    database.child("spo").child(timestamp).set({
        "spo2": bpm,
        "timestamp": timestamp
    })
    print("SPO: " + str(bpm))


def write_ecg(timestamp, bpm):
    database.child("ecg").child(timestamp).set({
        "ecg": bpm,
        "timestamp": timestamp
    })
    print("ECG: " + str(bpm))


def write_mvm(timestamp, bpm):
    database.child("mvm").child(timestamp).set({
        "mvm": bpm,
        "timestamp": timestamp
    })
    print("MVM: " + str(bpm))

# Function to write data starting from 10 hours in the past
def write_initial_data():
    current_timestamp = int(time.time())

    for minutes in range(600, 0, -1):
        var = random.randint(60, 200)
        timestamp = current_timestamp - (minutes * 60)
        write_bpm(timestamp, var)
        var = random.randint(60, 200)
        write_spo(timestamp, var)
        var = random.randint(60, 200)
        write_ecg(timestamp, var)
        var = random.randint(0, 1)
        write_mvm(timestamp, var)
        time.sleep(1)


# Define a function to write a random bpm value and timestamp to the database every minute
def write_every_minute():
    while True:
        var = random.randint(60, 200)
        timestamp = int(time.time())
        write_bpm(timestamp, var)
        var = random.randint(60, 200)
        write_spo(timestamp, var)
        var = random.randint(60, 200)
        write_ecg(timestamp, var)
        var = random.randint(0, 1)
        write_mvm(timestamp, var)
        time.sleep(60)


# Erase existing "bpm" data
database.child("spo").remove()
database.child("bpm").remove()
database.child("ecg").remove()
database.child("mvm").remove()

# Write data starting from 10 hours in the past
write_initial_data()

# Start writing data every minute
write_every_minute()
