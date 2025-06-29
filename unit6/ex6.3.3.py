import pyttsx3

text = "first time i'm using a package in next dot py course"

engine = pyttsx3.init()

# Convert text to speech
engine.say(text)

engine.runAndWait()
