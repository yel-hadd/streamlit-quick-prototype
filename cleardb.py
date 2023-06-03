from firebase_utils import database

database.child("spo").remove()
database.child("bpm").remove()
database.child("ecg").remove()
database.child("mvm").remove()

