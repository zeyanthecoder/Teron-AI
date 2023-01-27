from PyQt5 import QtCore , QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import webbrowser
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import pywhatkit
import wikipedia
import winsound
from googletrans import Translator
import cv2
import numpy as np
import os
from PIL import Image
import pyautogui
import psutil
from tkinter import Label
from tkinter import Entry
from tkinter import Button
import requests
from tkinter import Tk
from gtts import gTTS
from tkinter import StringVar
import PyPDF2
from win10toast import ToastNotifier
from pytube import YouTube
import datetime
from playsound import playsound
import keyboard
import pyjokes
from os import startfile
from pyautogui import click
from keyboard import write
import sys

Api_Key = "EYWI6OIyz2H9VcFMhS7R8bqvJ5j1NvhlFFrwJp1U"
Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices', voices[1].id)
Assistant.setProperty('rate', 200)

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
def speak(audio):
        print("      ")
        Assistant.say(audio)
        print(f":  {audio}")
        print("      ")
        Assistant.runAndWait()
        

def takecommand(self):
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            command.pause_threshold = 1
            audio = command.listen(source)

        try:
                print("Working On It")
                query = command.recognize_google(audio, language='en-in')
                print(f"User Said: {query}")
 
        except Exception as e:
            # print(e)    
            print("Say that again please...")  
            speak("Say that again please...")  
            return "None"
        return query
    
def taskexe(self):


        pyautogui.press('esc')
        speak("Welcome Back Zeyan Sir")
        speak("I Am Sonam")
        speak("Your Personal AI Assistant")
        speak("How May I Help You?")

        def Music():
                speak("Tell Me The name Of the Song Sir")
                musicName = takecommand(self)
                if 'payphone' in query:
                    os.startfile('C:\\Users\\zeyan\\Music\\teron\\payphone.mp3')
                if 'song' in query:
                    os.startfile('C:\\Users\\zeyan\\Music\\teron\\song.mp3')
                else:
                    pywhatkit.playonyt(musicName)
                    speak("Your Song Is Starting, Enjoy!")

        def time():
            t_now = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f" The Time Currently Is {t_now}")

        def date():
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            d_ate = int(datetime.datetime.now().day)

            speak(f"Today Is {year}, {month},{d_ate}")

        def Whatsapp():
            speak("Sir Tell Me The Name Of The Person")
            name = takecommand(self)

            if 'apalay' in name:
                speak("Message")
                msg = takecommand(self)
                speak("Tell Me The Time Sir")
                speak("Time In Hour!")
                hour = int(takecommand(self))
                speak("Time In Minutes!")
                min = int(takecommand(self))
                pywhatkit.sendwhatmsg("+917298975389", msg, hour, min,20)
                speak("Ok Sir. Sending Whatsapp Message!")
                pyautogui.press('enter')

            elif 'abilay' in query:
                speak("Message")
                msg = takecommand(self)
                speak("Tell Me The Time Sir")
                speak("Time In Hour!")
                hour = int(takecommand(self))
                speak("Time In Minutes!")
                min = int(takecommand(self))
                pywhatkit.sendwhatmsg("+919622167303", msg, hour, min,20)
                speak("Ok Sir. Sending Whatsapp Message!")
                pyautogui.press('enter')

            elif 'mama' in query:
                speak("Message")
                msg = takecommand(self)
                speak("Tell Me The Time Sir")
                speak("Time In Hour!")
                hour = int(takecommand(self))
                speak("Time In Minutes!")
                min = int(takecommand(self))
                pywhatkit.sendwhatmsg("+917298975389", msg, hour, min,20)
                speak("Ok Sir. Sending Whatsapp Message!")
                pyautogui.press('enter')

            elif 'kaka' in query:
                speak("Message")
                msg = takecommand(self)
                speak("Tell Me The Time Sir")
                speak("Time In Hour!")
                hour = int(takecommand(self))
                speak("Time In Minutes!")
                min = int(takecommand(self))
                pywhatkit.sendwhatmsg("+6005439498", msg, hour, min,20)
                speak("Ok Sir. Sending Whatsapp Message!")
                pyautogui.press('enter')

            elif 'message' in query:
                speak("Message")
                msg = takecommand(self)
                speak("Tell Me The Time Sir")
                speak("Time In Hour!")
                hour = int(takecommand(self))
                speak("Time In Minutes!")
                min = int(takecommand(self))
                pywhatkit.sendwhatmsg("+917298975389", msg, hour, min,20)
                speak("Ok Sir. Sending Whatsapp Message!")
                pyautogui.press('enter')

            elif 'bashir' in query:
                speak("Message")
                msg = takecommand(self)
                speak("Tell Me The Time Sir")
                speak("Time In Hour!")
                hour = int(takecommand(self))
                speak("Time In Minutes!")
                min = int(takecommand(self))
                pywhatkit.sendwhatmsg("+91 96229 58001", msg, hour, min,20)
                speak("Ok Sir. Sending Whatsapp Message!")
                pyautogui.press('enter')

        def openApp():
            speak("Ok Sir, Wait A Second!")

            if 'open code' in query:
                os.startfile("Code")
                speak("Opening Vs Code Sir")

            elif 'postman' in query:
                os.startfile("Postman")
                speak("opening Postman Sir")

            elif 'open Microsoft Word' in query:
                os.startfile("winword")
                speak("Opening Microsoft Word")

            elif 'open letter' in query:
                os.startfile("winword")
                speak("Opening Microsoft Word")

            elif 'open powerpoint' in query:
                os.startfile("powerpnt")
                speak("Opening Microsoft Powerpoint")

            elif 'open Chrome' in query:
                os.startfile("Chrome")
                speak("Opening Google Chrome")

            elif 'open Google Chrome' in query:
                os.startfile("Chrome")
                speak("Opening Google Chrome")
            
            elif 'open calculator'in query:
                    speak("opening calculator")
                    os.startfile("calc")

            elif 'open calendar'in query:
                    speak("opening calender")
                    os.startfile("calender")

            elif 'open youtube' in query:
                webbrowser.open('https://www.youtube.com')
        
        def closeApp():
            speak("Ok Sir")

            if 'chrome' in query:
                os.system("Taskkill /F /im chrome.exe")

            elif 'code' in query:
                os.system("Taskkill /F /im code.exe")

            elif 'close Microsoft Word' in query:
                os.system("Taskkill /F /im WINWORD.EXE")
                speak("Your Task Has Been Successfully Completed!")

        def Screenshot():
            speak("Ok Sir, What Should I name That File")
            path = takecommand(self)
            path1name = path + ".png"
            path1 = "C:\\Users\\zeyan\\OneDrive\\Desktop\\teron\\Screenshots\\"+ path1name
            kk = pyautogui.screenshot()
            kk.save(path1)
            os.startfile('C:\\Users\\zeyan\\OneDrive\\Desktop\\teron\\Screenshots')
            speak("Here Is Your Screenshot Sir!")

        def YoutubeAuto():

            webbrowser.open("https://www.youtube.com")

            speak("What Can I do For You Sir?")
            comm = takecommand(self)

            if 'pause' in comm:
                keyboard.press('space bar')
                speak("Video Paused")

            elif 'restart' in comm:
                speak("Restarting The Video")
                keyboard.press('0')

            elif 'mute' in comm:
                keyboard.press('m') 

            elif 'skip' in comm:
                keyboard.press('l')

            elif 'back' in comm:
                keyboard.press('j')

            elif 'full screen' in comm:
                speak("switching To Full Screen Mode")
                keyboard.press('f')

            elif 'film mode' in comm:
                keyboard.press('t')

            speak("Done Sir")

        def ChromeAuto():
            speak("Chrome Automation Started!")
            command = takecommand(self)

            if 'close the tab' in command:
                keyboard.press_and_release('ctrl + w')

            elif 'open new tab' in command:
                keyboard.press_and_release('ctrl + t')

            elif 'open new window' in command:
                keyboard.press_and_release('ctrl + n')

            elif 'history' in command:
                keyboard.press_and_release('ctrl +h')

        def dict():
            speak("Activated Dictionary!")
            if 'help me' in query:
                    speak(f"ofcourse sir ! how can i help you sir")
                    speak(f'question sir!')
                    s = takecommand(self)
                    print(s)
                    speak(
                        "There are 3 thing that i can do for you sir i can search for it on google or youtube or wikipedia")
                    speak(f"where i should to serach sir")
                    s1 = takecommand(self).lower()
                    if s1 == 'google':
                        speak(f"opening  google sir!")
                        webbrowser.open(
                            "www.google.com/search?q=" + s + "=9d02b0a92caa4bc895c28ea9269d27e6&FORM=ANAB01&PC=ASTS")

                    elif s1 == 'youtube' in query:
                        speak(f"opening youtubesir!")
                        webbrowser.open("www.youtube.com/results?search_query=" + s + "")

        def Tran():
            speak("Tell Me The Line!")
            line = TakeHindi()
            Translate = Translator()
            result = Translate.translate(line)
            Text = result.text
            speak(Text)

        def TakeHindi():
            command = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening......")
                command.pause_threshold = 1
                audio = command.listen(source)

                try:
                    print("Recognizing.....")
                    query = command.recognize_google(audio,language='hi')
                    print(f"You Said : {query}")

                except:
                    return "none"

                return query.lower() 

        def Temp():
            search = "temperature in leh"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            speak(f"The Temperature Is {temperature}")
            speak("Do I Have To Tell You Another Place Temperature ?")
            next = takecommand(self)

            if 'yes' in next:
                speak("Tell Me The Name Of the Place ")
                name = takecommand(self)
                search = f"temperature in {name}"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temperature = data.find("div",class_ = "BNeawe").text
                speak(f"The Temperature in {name} is {temperature} celcius")

            else:
                speak("no problem sir")
        
        def speedtest():
            import speedtest 
            speak("Checking Speed...")
            speed = speedtest.Speedtest()
            downloading = speed.download()
            correctDown = int(downloading/80000)
            uploading = speed.upload()
            correctUpload = int(uploading/80000)

            if 'uploading' in query:
                speak(f"The Uploading Speed Is {correctUpload} mbps")

            elif 'downloading' in query:
                speak(f"The Downloading Speed Is {correctDown} mbps")

            else:
                speak(f"The Downloading Speed Is {correctDown} and The Uploading Speed Is {correctUpload} mbps")

        def Reader():
            speak("Tell Me The Name Of The Book!")

            name = takecommand(self)

            if 'india' in name:

                os.startfile('C:\\Users\\zeyan\\OneDrive\\Desktop\\teron\\pdf\\read.pdf')
                book = open('C:\\Users\\zeyan\\OneDrive\\Desktop\\teron\\pdf\\read.pd' 'rb')
                pdfreader = PyPDF2.PdfFileReader(book)
                pages = pdfreader.getNumPages()
                speak(f"Number Of Pages In This Books Are {pages}")
                speak("From Which Page I Have To Start Reading ?")
                numPage = int(input("Enter The Page Number :"))
                page = pdfreader.getPage(numPage)
                text = page.extractText()
                speak("In Which Language , I Have To Read ?")
                lang = takecommand(self)

                if 'hindi' in lang:
                    transl = Translator()
                    textHin = transl.translate(text,'hi')
                    textm = textHin.text
                    speech = gTTS(text = textm )
                    try:
                        speech.save('book.mp3')
                        playsound('book.mp3')

                    except:
                        playsound('book.mp3')

                else:
                    speak(text)

                if 'hindi' in lang:
                    transl = Translator()
                    textHin = transl.translate(text,'hi')
                    textm = textHin.text
                    speech = gTTS(text = textm )
                    try:
                        speech.save('book.mp3')
                        playsound('book.mp3')

                    except:
                        playsound('book.mp3')

                else:
                    speak(text)

        def notepad():
            speak("Tell Me The Query")
            speak("I Am Ready To Write...")
            writes = takecommand(self)
            time = datetime.datetime.now()
            now = time.strftime("%H:%M")     
            filename = str(time).replace(":","-" )+ "-note.txt"
            with open (filename, "w") as file:
                file.write(writes)
            path_1 = "C:\\Users\\zeyan\\OneDrive\\Desktop\\Teron 2.0\\"+ str(filename)
            path_2 = "C:\\Users\\zeyan\\OneDrive\\Desktop\\Teron 2.0\\notepad\\" + str(filename)
            os.rename(path_1, path_2)
            os.startfile(path_2)

        def CloseNotepad():
            os.system("TASKKILL /F /im Notepad.exe")

        while True:
            query = takecommand(self)

            if 'hello' in query:
                speak("Hello Sir, I am Sonam How May I Help You")

            elif 'how are you' in query:
                speak("I am Fine Sir")
                speak("What About You?")

            elif 'change voice to female' in query:
                Assistant.setProperty('voices', voices[0].id)
                speak("Voice Changed Successfully")

            elif 'change voice to male' in query:
                Assistant.setProperty('voices', voices[1].id)
                speak("Voice Changed Successfully")

            elif 'who created you' in query:
                speak("Zeyan Ramzan Created Me on 2nd of November 2021 ")

            elif 'Sonam' in query:
                speak("Hello Sir I am Sonam. Your Personal AI Assistant. How Are You")

            elif 'How are you' in query:
                speak("I Am Fine Sir.")
                speak("What About You Sir ?")

            elif 'I am fine' in query:
                speak("Glad To Hear That !")

            elif 'what can you do' in query:
                Assistant.setProperty('rate', 220)
                speak("Try Saying")
                speak("play music !")
                speak("write a note")
                speak("I want to Play ludo")
                speak("Send Whatsapp Message")
                speak("Selmon Bhoi wikipedia")
                speak("website instagram")
                speak("google search who is the prime minister of india")
                speak("Show Me some Mars Images !")
                speak("About Solar System")
                Assistant.setProperty('rate', 200)

            elif 'who made you' in query:
                speak("Zeyan Ramzan Made Me On 2nd Of November 2021")

            elif 'youtube search' in query:
                ("Sir This is what I found on youtube")
                query = query.replace("Sonam", "")
                query = query.replace("youtube", "")
                web = 'https://www.youtube.com/results?search_query=' + query
                webbrowser.open(web)
                speak("Done Sir")

            elif 'website' in query:
                speak('Ok sir, Launching...')
                query = query.replace("Sonam", "")
                query = query.replace("website", " ")
                query = query.replace("  ", "")
                web0 = 'www.'
                web1 = query.replace("open", " ")
                web2 = web0 +web1 + '.com'
                webbrowser.open(web2)
                speak("Website Launched!")

            elif 'you need a break' in query:
                speak("Ok sir,Thanks for giving me your time !")
                exit()

            elif 'speak fast' in query:
                speak('"ok Sir')
                Assistant.setProperty('rate' ,200)

            elif 'speak slowly' in query:
                speak("Ok Sir")
                Assistant.setProperty('rate', 150)

            elif 'bye' in query:
                speak("Ok Sir, Thanks For Giving Me Your Time!")
                exit()

            elif 'launch' in query:
                speak("Sir Can You Tell Me The Name Of The Website?")
                name = takecommand(self)
                web = 'https://www.' + name + '.com'
                webbrowser.open(web)

            elif 'open facebook' in query:
                speak("Ok Sir")
                webbrowser.open("https://www.facebook.com")
                speak("Done Sir")

            elif 'music' in query:
                Music()

            elif 'wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace("Sonam", "")
                query = query.replace("wikipedia", "")
                wiki = wikipedia.summary(query, 2)
                speak(f"According To Wikipedia : {wiki}")

            elif 'whatsapp' in query:
                Whatsapp()

            elif 'screenshot' in query:
                Screenshot()

            elif 'open youtube' in query:
                openApp()
            
            elif 'open Microsoft Word' in query:
                openApp()

            elif 'open code' in query:
                openApp()
    
            elif 'open postman' in query:
                openApp()

            elif 'open calendar' in query:
                openApp

            elif 'open calculator'in query:
                openApp()

            elif 'open youtube' in query:
                openApp

            elif 'open chrome' in query:
                openApp()

            elif 'open Microsoft Word' in query:
                speak("Opening Microsoft Word")
                os.startfile('winword')

            elif 'open letter' in query:
                openApp()

            elif 'close Microsoft Word' in query:
                closeApp()
                speak("Closing Microsoft Word")

            elif 'close Chrome' in query:
                closeApp()
                speak("Closing Google Chrome")

            elif 'close code' in query:
                closeApp()
                speak("Closing Vs Code")

            elif 'restart' in query:
                speak("Restarting The Video")
                keyboard.press('0')

            elif 'mute' in query:
                keyboard.press('m')

            elif 'skip' in query:
                keyboard.press('l')

            elif 'back' in query:
                keyboard.press('j')

            elif 'full screen' in query:
                speak("switching To Full Screen Mode")
                keyboard.press('f')

            elif 'film mode' in query:
                keyboard.press('t')

            elif 'pause' in query:
                keyboard.press('space bar')
                speak("Video Paused Sir")

            elif 'youtube tool' in query:
                YoutubeAuto()

            elif 'close the tab' in query:
                keyboard.press_and_release('ctrl + w')

            elif 'open new tab' in query:
                keyboard.press_and_release('ctrl + t')

            elif 'press' in query:
                pressbtn = takecommand(self)
                keyboard.press_and_release(pressbtn)

            elif 'open new window' in query:
                keyboard.press_and_release('ctrl + n')

            elif 'history' in query:
                keyboard.press_and_release('ctrl +h')

            elif 'who' in query:
                import wikipedia as googleScrap
                query = query.replace("Sonam","")
                query = query.replace(" search","")
                query = query.replace("","")
                speak("This Is What I Found On The Web!")
                pywhatkit.search(query)

                try:
                    result = googleScrap.summary(query,2)
                    speak(result)

                except:
                    speak("No Speakable Data Available!")

            elif 'how to' in query:
                speak("Getting Data From The Internet !")
                op = query.replace("Sonam","")
                max_result = 1
                how_to_func = search_wikihow(op,max_result)
                assert len(how_to_func) == 1
                how_to_func[0].print()
                speak(how_to_func[0].summary)

            elif 'chrome automation' in query:
                ChromeAuto()

            elif 'joke' in query:
                get = pyjokes.get_joke()
                speak(get)

            elif 'repeat after me' in query:
                speak("Ok Sir")
                jj = takecommand(self)
                speak(f"You Said:  {jj}")

            elif 'my location' in query:
                speak("Ok Sir, Wait A Second!")
                webbrowser.open("https://www.google.com/maps/@33.9831244,77.9290684,10.73z")

            elif 'help me' in query:
                    speak(f"ofcourse sir ! how can i help you sir")
                    speak(f'question sir!')
                    s = takecommand(self)
                    print(s)
                    speak(
                        "There are 3 thing that i can do for you sir i can search for it on google or youtube or wikipedia")
                    speak(f"where i should to serach sir")
                    s1 = takecommand(self).lower()
                    if s1 == 'google':
                        speak(f"opening  google sir!")
                        webbrowser.open(
                            "www.google.com/search?q=" + s + "=9d02b0a92caa4bc895c28ea9269d27e6&FORM=ANAB01&PC=ASTS")

                    elif s1 == 'youtube' in query:
                        speak(f"opening youtube sir!")
                        webbrowser.open("www.youtube.com/results?search_query=" + s + "")    

            elif 'dictionary' in query:
                dict()

            elif 'alarm' in query:
                speak("Enter The Time")
                time = input('Enter The Time :') 

                while True:
                    Time_Ac = datetime.datetime.now()
                    now = Time_Ac.strftime("%H:%M:%S")     

                    if now == time:
                        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
                        time.sleep(10)
                        speak("Alarm Closed")

                    elif now>time:
                        break
            
            elif 'remember that' in query:
                remeberMsg = query.replace("remember that","")
                remeberMsg = remeberMsg.replace("Sonam","")
                speak("You Tell Me To Remind You That :"+remeberMsg)
                remeber = open('data.txt','w')
                remeber.write(remeberMsg)
                remeber.close()

            elif 'what do you remember' in query:
                remeber = open('data.txt','r')
                speak("You Tell Me That" + remeber.read())

            elif 'temperature' in query:
                Temp()

            elif 'downloading speed' in query:
                speedtest()

            elif 'uploading speed' in query:
                speedtest()

            elif 'internet speed' in query:
                speedtest()

            elif 'right' in query:
                speak("What to write?")
                writing = takecommand(self)
                pyautogui.write(writing, interval=0.01)
                pyautogui.press('space')

            elif 'enter' in query:
                pyautogui.press('enter')  

            elif 'rubbish' in query:
                pyautogui.alert('Sorry Sir.')

            elif 'how to' in query:
                speak("Getting Data From The Internet !")
                op = query.replace("Sonam","")
                max_result = 1
                how_to_func = search_wikihow(op,max_result)
                assert len(how_to_func) == 1
                how_to_func[0].print()
                speak(how_to_func[0].summary)

            elif 'who is' in query:
                speak("Searching !")
                op = query.replace("Sonam","")
                max_result = 1
                how_to_func = search_wikihow(op,max_result)
                assert len(how_to_func) == 1
                how_to_func[0].print()
                speak(how_to_func[0].summary)

            elif 'read book' in query:
                Reader()

            elif 'video downloader' in query:
                root = Tk()
                root.geometry('500x300')
                root.resizable(0,0)
                root.title("Youtube Video Downloader")
                speak("Enter Video Url Here !")
                Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
                link = StringVar()
                Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
                Entry(root,width = 70,textvariable = link).place(x=32,y=90)

                def VideoDownloader():
                    url = YouTube(str(link.get()))
                    video = url.streams.first()
                    video.download()
                    Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

                Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

                root.mainloop()
                speak("Video Downloaded")

            elif 'translator' in query:
                Tran()

            elif 'space news' in query:
                speak("Tell Me The Date For The Space News...")
                date = input('Enter  The Date :') 
                from nasa import NasaNews
                NasaNews(date)

            elif 'write a note' in query:
                speak("Ok?")
                writing = takecommand(self)
                pyautogui.write(writing)

            elif  'notepad' in query:
                notepad()

            elif 'close notepad' in query:
                CloseNotepad()

            elif 'mars images' in query:
                speak("Showing Images From Nasa's Space Rovers")
                from nasa import Mars
                Mars()

            elif 'solar system' in query:
                from nasa import SolarBodies
                speak("Tell Me The Name Of The Body")
                bod = takecommand(self)
                body = bod.replace(" ", "")
                body = bod.replace(" ", "")
                Body = str(bod)
                SolarBodies(Body= body)
            
            elif  'this' in query:
                speak("ok sir please say what you want to write sir")
                s =takecommand(self)
                pyautogui.write(s)
                # time.sleep(3)
                pyautogui.press('enter')

            elif 'what is the time' in query:
                time()

            elif 'date' in query:
                date()

            elif 'ludo' in query:
                speak("Launching Z-Ludo By Zeyan Ramzan")
                webbrowser.open('https://z-ludo-king.web.app')

            elif "who is my favourite cousin" in query:
                speak("Gulnaaz is your favourite cousin")

            elif 'scroll up' in query:
                pyautogui.scroll(1000) 

            elif 'scroll down' in query:
                pyautogui.scroll(-1000) 

            elif 'google search' in query:
                import wikipedia as googleScrap
                query = query.replace("Sonam","")
                query = query.replace("search","")
                query = query.replace("","")
                speak("This Is What I Found On The Web!")
                pywhatkit.search(query)

            elif 'how do you pronounce' in query:
                speak("Tell me the word")
                word = takecommand()
                speak("I pronounce that: " + word)