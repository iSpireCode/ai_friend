from datetime import datetime
import pyttsx3
import speech_recognition

friend = pyttsx3.init()
friend.setProperty("rate", 150) # slow down speech rate

voices = friend.getProperty('voices')
friend.setProperty('voice', voices[10].id) 
activationWord = "computer"


friend.say("Good morning Brian")
friend.runAndWait()

def speak(audio):
    friend.say(audio)
    friend.runAndWait()

def time():  
    Time = datetime.now().strftime("%A%H-%M") # %A(Day) %B(Month) %d(day) %Y(year) %H(hour) -%M(minute) -%S(second)
    speak(Time)
time()



# friend.say("Hello Brian")
# friend.runAndWait()
# friend.stop()

