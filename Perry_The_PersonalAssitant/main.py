import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    assname =("Perry 1 point O")
    speak("I am your Personal Assistant")
    speak(assname)


def username():
    speak("What should I call you sir?")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("###################".center(columns))

    speak("How can I help you, Sir")


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        # r.pause_threshold = 5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        # query = r.recognize_google_cloud(audio, language= 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()


    server.login('now.official1@gmail.com', 'oonbdppqpysalzpp')
    server.sendmail('now.official1@gmail.com', to, content)
    server.close()



# main function

if __name__ == '__main__':
    clear = lambda: os.system('cls')

    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("Google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow. Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or "play song" in query:
            speak("Here you go to Spotify")
            webbrowser.open("spotify.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open chrome' in query:
            codePath = r"C:\Users\abhin\OneDrive\Desktop\Abhinav (Overall Use) - Chrome.lnk"
            os.startfile(codePath)

        elif 'email to friend' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "Receiver email address"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Abhinav")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to " in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My driends call me")
            speak(assname)
            print("my friends call me", assname)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Abhinav")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:
            app_id = "9W4GH4-LHL5RLH5EH"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "Who i am" in query:
            speak("If you talk then definitely you are human.")

        elif "why you came to world" in query:
            speak("Thanks to Abhinav, further it's a secret")

        elif "power point presentation" in query:
            speak("opening Power point presentation")
            power = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"
            os.startfile(power)

        elif "is love" in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am personal virtual assistant created by Abhinav")

        elif "reason for your creation" in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")

        elif "open valorant" in query:
            appli = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\VALORANT.lnk"
            os.startfile(appli)

        elif "news" in query:

            try:
                jsonObj = urlopen('''https://www.hindustantimes.com/''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''==================== HINDUSTAN TIMES =================''' + '\n')

                for item in data['articles']:

                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    print(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))

        elif 'lock window' in query:
            speak("Locking PAVI")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold on a sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p/f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle bin recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop perry from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("user asked to locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Perry camera", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown /h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown","/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('perry.txt', 'w')
            speak("Sir, should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("perry.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream = True)

            with open("Voice.py", "wb") as Pypdf:

                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size = 2391975), expected_size = (total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)


        elif "Perry" in query:

            wishMe()
            speak("Perry 1 point o in your service mister")
            speak(assname)

        elif 'weather' in query:


            api_key = "5a2d4c7bda51265476e0f3f45676dc50"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak("City name ")
            print("City name: ")
            city_name = takeCommand()
            complete_url = base_url + "appid = " + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["code"] != "404":
                y = x["main"]
                current_temprature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(current_temprature) + "\n atmospheric pressure (in hPa unit) =" + str(current_pressure)+
                      "\n humidity (in percentage) =" + str(current_humidity)+ "\n description = "+str(weather_description))

            else:
                speak("City not found")

        elif "send message" in query:

            account_sid = "AC70b03c2b0e21e21692913b58539758cf"
            auth_token = "ac9365909845e51cadfeec085feca773"
            client = Client(account_sid, auth_token)

            message = client.messages \
                            .create(
                                body=takeCommand(),
                                from_='Sender No',
                                to='Receiver No')
            print(message.sid)

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm "  +query)
            speak("How are you mister")
            speak(assname)

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif " how are you" in query:
            speak("I'm fine, glad you me that")

        elif "I love you" in query:
            speak("It's hard to understand")

        elif "what is" in query or "who is" in query:

            client = wolframalpha.Client("5a2d4c7bda51265476e0f3f45676dc50")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")




