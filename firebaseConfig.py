import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

config = {
    'apiKey': "AIzaSyAW8hNJncjK9AZtKrCeGjKRiiUbyA0XoXc",
    'authDomain': "travelblog-b7941.firebaseapp.com",
    'projectId': "travelblog-b7941",
    'storageBucket': "travelblog-b7941.appspot.com",
    'messagingSenderId': "839540723786",
    'appId': "1:839540723786:web:1bef7981791d6bdbd396b3",
    'measurementId': "G-G30PEKM6W4",
    'databaseURL': ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def getAuth():
    return auth


cred = credentials.Certificate("secret.json")
firebase_auth = firebase_admin.initialize_app(
    cred, {'storageBucket': "travelblog-b7941.appspot.com"})

db = firestore.client()

def getDb():
    return db

bucket = storage.bucket()


def getBucket():
    return bucket