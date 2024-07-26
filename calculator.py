import wolframalpha
import pyttsx3
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


# Calculate
def WolfRamAlpha(query):
    api_key = os.getenv("API_KEY")
    request = wolframalpha.Client(api_key)
    requested = request.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("Invalid")


def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("add", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("divide", "/")

    Final = str(Term)

    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("Not answerable")