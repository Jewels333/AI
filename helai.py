#https://www.behindthename.com/random/random.php?gender=f&number=1&sets=1&surname=&showextra=yes&all=yes
import pyttsx3 
import datetime
import speech_recognition as sr
engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Hey!")
    speak("It's")
    time()
    speak("And the date's")
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good evening")
    else:
        speak("Good Night.")
    speak("What's up") #legit npc 

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("proccessing")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("what?")
        return "None"
    return query