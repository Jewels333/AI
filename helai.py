#https://www.behindthename.com/random/random.php?gender=f&number=1&sets=1&surname=&showextra=yes&all=yes
import pyttsx3
import datetime
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
    speak("What's up") #legit npc 

wishme()