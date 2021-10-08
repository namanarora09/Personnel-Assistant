import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
from weather import sendweather
from musixplayer2 import musicplayer2
import subprocess
import random
from MyMail import *
from automate_whatsapp import *
from reminder import *
from SimpNote import *
#from Face_detection import *
#from face import *


print('warming up my vocal cords!')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
                         

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        audio=r.listen(source)


        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


wishMe()


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you?")
        statement = takeCommand().lower()
        
        if statement==0:
            continue

        if "goodbye" in statement or "ok bye" in statement or "nothing else" in statement:
            speak('yay! I am done for the day')
            print('Goodbye, talk to you soon!')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "how are you" in statement:
            speak("I am fine, thank you for asking. how have you been?")
            mood=takeCommand()
            if "I am fine" in statement:
                speak("that's good how may I assist you today")
            elif 'I am not fine' in statement:
                speak("Oh no!,What can I do to help you?")

        elif 'flip a coin' in statement:
            speak("flipping the coin")
            flip=random.randint(0,1)
            if flip==1:
                speak("it's tails")
            else:    
                speak("it's heads")
            
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
            
        elif "I want to watch a movie" in statement:
            webbrowser.open_new_tab("netflix.com")
            speak("play something you like")
            speak("wake me up when you are done")
            time.sleep(100)

        elif "what's the weather like today" in statement or "Should I carry an umbrella" in statement:
            speak("what's the city name")
            statement=takeCommand().lower()
            sendweather(statement)
            speak("here take a look")
            webbrowser.open_new_tab('https://www.windy.com/-Rain-thunder-rain?rain,26.915,75.819,11')
            time.sleep(10)

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am your persoanl assistant. I am programmed to do variety of tasks, support for more tasks coming soon')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Group 5")
            print("I was built by Group 5")
            
        elif 'news' in statement or "What are the today's headlines" in statement:
            speak("let me read the newspaper so that I can give you quick updates")
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            time.sleep(45)

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
            
        elif "remind me" in statement or "set a reminder" in statement:
            speak("what is it that you want me to remind you about")
            remindme=takeCommand()
            speak("I will remind you when the time comes")
            
        elif "add" in statement or "sum" in statement or "multiplication" in statement:
            speak("Let me bring up the calculator")
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            time.sleep(20)
           
        elif 'I want to watch a TV show' in statement:
            speak("PLease tell me the name of the show")
            tvshow=takeCommand()
            speak("hang on let me play it")
            webbrowser.open_new_tab("www.netflix.com")
           
        elif "download from spotify" in statement:
            speak("Please say the name of the song")
            songname=takeCommand()
            os.system('cmd /c "spotdl "'+songname)
            speak("song is downloaded")           
            
        elif "play some music" in statement:
        #     speak("hang on let me try")
   #         localsong=takeCommand()
             musicplayer2()

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
        
        elif "send a mail" in statement:
            speak("what do you want to write?")
            speak("unable to contact servers please try again after some time")
            time.sleep(2)
            
        elif "add items to shopping list" in statement:
            speak("hang on")
            speak("okay tell me do you want to create new list or update old one")
            shop=takeCommand()
            if "update old one" in shop:
                speak("wait let me bring up your old list")
                speak("unable to reach your shopping list. Error 404")
                print("fatal error occurred. Restart me.")
                
            elif "create new one" in shop:
                speak("okay tell me what you want to buy this time")
                speak("unable to make a new list. Error 503")
                print("fatal error")
                
                
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
            
        elif "convert this video file please" in statement:
            speak("tell me the name of the file")
            videofile=input("type the name with extension")
            final=input("type the format in which you want the video")
            os.system('cmd /c "ffmpeg -i"'+videofile+" "+final)
        
        elif "search on wolframalpha" in statement or "ask" in statement:
            speak("hang on let me connect to wolframalpha")
            speak('I can answer to computational and geographical questions')
            question = takeCommand()
            app_id = "29R7PV-X9K3U8X5ET"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        
        elif "webcam" in statement or "camera" in statement or "take photo" in statement or "capture photo" in statement:
            speak("Opening webcam")
            face()
            
        elif "whatsapp" in statement or "send a message" in statement:
            speak("okay as you wish")
            automateWhatsapp()
            
        
time.sleep(3)












