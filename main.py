import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import datetime
import pyautogui
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

# Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()


# Take input from the user through mic
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        if query.lower() == "jarvis":
            speak("I'm ON...How can I assist you Sir?")
        return query.lower()

    except Exception as e:
        print("Say that again please...")  
        return "None"
    

# Set alarm 
def set_alarm(time):
    with open("command.txt", "w") as file:
        file.write(time)
    os.startfile("alarm.py")

    
# Main function     
if __name__ == "__main__":
    speak("Initializing...")
    while True:
        query = takeCommand()

        # Open websites, set alarm, calculate, click photo, screenshot, temperature and play music
        if "open google" in query:
            webbrowser.open("https://google.com")
            speak("Opening Google")
        elif "open youtube" in query:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")
        elif "set an alarm" in query:
            print("Input time in the 24 hour format - HH:MM:SS")
            speak("Please tell the time")
            a = input("Please tell the time - ")
            
            # Validate input time format
            try:
                datetime.datetime.strptime(a, '%H:%M:%S')
                set_alarm(a)
                speak(f"Alarm set for {a}")
            except ValueError:
                speak("Invalid time format. Please try again.")
        elif "calculate" in query: 
            from calculator import WolfRamAlpha
            from calculator import Calc
            query = query.replace("calculate", "")
            query = query.replace("jarvis", "")
            Calc(query)
        elif "click a photo" in query: 
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(2)
            speak("SMILE!")
            pyautogui.press("enter")
        elif "screenshot" in query: 
            im = pyautogui.screenshot()
            im.save("ss.jpg")
            speak("DONE")
        elif "temperature in" in query:
            from temp import get_weather
            city_name = query.split("in")[-1].strip()
            speak(f"Getting weather details for {city_name}")
            temperature, description = get_weather(city_name)
            if temperature is not None:
                print(f"Temperature in {city_name}: {temperature} degree celcius")
                speak(f"The temperature in {city_name} is {temperature} degree celsius with {description}.")

            else:
                speak(f"Sorry, I couldn't find the weather details for {city_name}") 
        elif "play" in query and "by" in query:
            from music import play_song
            song_artist = query.replace("play", "").strip()
            song_name, artist_name = song_artist.split("by")
            song_name = song_name.strip()
            artist_name = artist_name.strip()
            if song_name and artist_name:
                play_song(song_name, artist_name)
            else:
                speak("Please specify both the name of the song and the artist.")
        elif "thank you" in query or "thanks" in query:
            speak("You're welcome sir")