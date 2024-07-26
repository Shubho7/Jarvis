import pyttsx3
import datetime 
import os

# Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Read the time from the file
with open("command.txt", "rt") as extractedtime:
    time = extractedtime.read().strip()

# Clear the file after reading
with open("command.txt", "w") as deletetime:
    deletetime.truncate()

def ring(alarm_time):
    print(f"Alarm set for: {alarm_time}")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            speak("Alarm ringing")
            os.startfile("music.mp3")
            break


# Call the ring function with the time read from the file
ring(time) 

