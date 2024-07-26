import pyttsx3
import speech_recognition as sr
import requests
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

# Temperature API call
def get_weather(city_name):
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = os.getenv("APIKEY2")
    print(api_key)
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        description = weather["description"]
        return temperature, description
    else:
        return None, None