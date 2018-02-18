from firebase import firebase
import os

FIREBASE_URL = "https://monitor-a80a5.firebaseio.com/"

# Main
if __name__ == '__main__':
    fb = firebase.FirebaseApplication(FIREBASE_URL, None) # Create a reference to the Firebase Application
    result = fb.get('', None)

    for k in result.keys():
        print(result[k])

