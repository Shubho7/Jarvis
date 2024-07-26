import pyttsx3
import speech_recognition as sr
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os 
from dotenv import load_dotenv

load_dotenv()

# Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()


# Spotify API call
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("CLIENTID"),
                                               client_secret=os.getenv("CLIENTSECRET"),
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-modify-playback-state,user-read-playback-state"))
    

# Song
def play_song(song_name, artist_name):
    query = f'track:{song_name} artist:{artist_name}'
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        track_uri = track['uri']

        # Get the list of available devices
        devices = sp.devices()
        if not devices['devices']:
            speak("No active Spotify devices found.")
            return

        # Select the first available device
        device_id = devices['devices'][0]['id']

        # Start playback on the selected device
        sp.start_playback(device_id=device_id, uris=[track_uri])
        speak(f"Playing {song_name} by {artist_name} on Spotify.")
        print(f"Playing {song_name} by {artist_name} on Spotify.")
        webbrowser.open(track_uri)
    else:
        speak(f"Sorry, I couldn't find the song {song_name} by {artist_name}.")