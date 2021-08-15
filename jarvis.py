import sys

import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


# Text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print('Recognizing')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour > 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis sir please tell me can may i help you")


# to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shudhanshushekhar99736@gail.com', 'shekhar99736')
    server.sendmail('shudhanshushekhar99736@gail.com', to, content)
    server.close()


if __name__ == "__main__":

    wish()
    while True:

    # if 1:

        query = takecommand().lower()

        # logic building for tasks
        if "open python" in query:
            npath = "C:\\Users\\shudh\\Downloads\\python-3.7.3.exe"
            os.startfile(npath)
        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while 1:

                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\Users\\shudh\\music"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith(('.mp3')):
                    os.startfile(os.path.join(music_dir, song))

            # os.startfile(os.path.join(music_dir,rd))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
        # print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            speak("sir,what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")




        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open gaana" in query:

            webbrowser.open("www.gaana.com")

        elif "send message" in query:
            kit.sendwhatmsg("+919956681703", "this is testing jarvis", 2, 25)

        elif "play song on youtube" in query:
            speak("which song you want to play")
            cd = takecommand().lower()
            kit.playonyt(f"{cd}")

        elif "email to aditya " in query:


            try:
                speak("what should i say?")


                content = takecommand()
                to = "aadimish2012@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to aditya mishra")

            except Exception as e:
                print(e)
                speak("sorry sir,i am not able to sent this  mail to aditya ")

        elif "no thanks" in query:
            speak("thanks for using me sir,have a good day")
            sys.exit()


        speak("sir,do you have other work ")

