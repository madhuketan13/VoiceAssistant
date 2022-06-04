from http.server import CGIHTTPRequestHandler
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import requests
import json
import pytz

def speechtotext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        recognizer.adjust_for_ambient_noise(source) 
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            # return data
        except sr.UnknownValueError:
            print("Sorry I did not Understand")
# speechtotext()

def speechtxt(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    speedrate = engine.getProperty('rate')
    engine.setProperty('rate',160)
    engine.say(x)
    engine.runAndWait()
# speechtxt("I am Jarvis")


if __name__ == '__main__':
    my_date = datetime.datetime.now(pytz.timezone('US/Pacific'))
    print(my_date)
    
    # print(j['joke'])
    sttdata = speechtotext()
    if 'your name' in sttdata:
        name = "I am Jarvis"
        speechtxt(name)
    if 'joke' in sttdata:
        r = requests.get("https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Dark,Pun,Spooky,Christmas?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single")
        j=r.json()
        speechtxt(j['joke'])
    if 'date' in sttdata:
        dt = datetime.datetime.now() 
        speechtxt(dt) 

        
        
            








