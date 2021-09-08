import os
import os.path
from os import path
import pyttsx3
from pytube import YouTube
import webbrowser
import wikipedia
from bs4 import BeautifulSoup
import requests
from lxml.html.soupparser import fromstring
import lxml
import random
import pyjokes
import time
import datetime

computer = pyttsx3.init()
greeting = "Hello sir, I am always here to assist you, how can I be of help?"
computer.say(greeting)
computer.runAndWait()

def computer():
    computer = pyttsx3.init()

    iput = input("> ")

    if iput == "mkdir" or iput == "directory":
        while True:
            dir_question = "How are we going to call your directory sir?"
            computer.say(dir_question)
            computer.runAndWait()
            direct = input("> Directory name: ")
            parent_dir = "C:\\Users\\O\\Desktop"
            path = os.path.join(parent_dir, direct)
            os.makedirs(path)
            dir_success = "Direcory created successfully"
            computer.say(dir_success)
            computer.runAndWait()
            print("> Direcory created successfully")
            break

    if iput == "file":
        while True:
            fname = "How are we going to call your file sir?"
            computer.say(fname)
            computer.runAndWait()
            file = input("> File name: ")
            path = "C:\\Users\\O\\Desktop"
            with open(os.path.join(path, file), 'w') as fp:
                pass
            fil_success = "File created successfully"
            computer.say(fil_success)
            computer.runAndWait()
            print("> File created successfully")
            break

    if iput == "youtube download":
        while True:
            vid_path = "C:\\Users\\O\\Desktop"
            vidl  = "Please provide me with a link to the video you want downloaded sir"
            computer.say(vidl)
            computer.runAndWait()
            link  = input("> YouTube link: ")
            ylink = YouTube(link)
            print("> Downloading Video...")
            ylink.streams.filter(res="360p").first().download(vid_path)
            id_success = "Video download successful sir"
            computer.say(vid_success)
            computer.runAndWait()
            print("> Download successful")
            break

    if iput == "time":
        while True:
            time0 = datetime.datetime.now().strftime('%H%M')
            time1 = datetime.datetime.now().strftime('%H:%M')
            computer.say('It is'+ time0 + "now")
            computer.runAndWait()
            print("> " + time1)
            break

    if iput == "create password":
        while True:
            chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@().,1234567890'
            quest = "How long would you like your password to be sir?"
            computer.say(quest)
            computer.runAndWait()
            q = 1
            q = int(q)
            l = input("> Password length: ")
            l = int(l)
            for j in range(q):
                password = ''
                for i in range(l):
                    password += random.choice(chars)
            file = input("> Password file name: ")
            path = "C:\\Users\\O\\Desktop"
            with open(os.path.join(path, file), 'w') as f:
                f.write(password)
                f.close()
            pwd_success = "Password created successfully, it is now stored in your desktop directory"
            print(pwd_success)
            break
            
    if iput == "joke":
        while True:
            jk = pyjokes.get_joke()
            computer.say(jk)
            computer.runAndWait()
            break

    if iput == "google":
        while True:
            guery = "What are we searching for sir?"
            computer.say(guery)
            computer.runAndWait()
            query = input("> ")
            url = f"https://google.com/search?q={query}"
            computer.say("Opening the web now")
            computer.runAndWait()
            webbrowser.get().open(url)
            break

    if iput == "youtube":
        while True:
            yuery = "What are we looking for?"
            computer.say(yuery)
            computer.runAndWait()
            kuery = input("> ")
            yurl = f"https://www.youtube.com/results?search_query={kuery}"
            computer.say("Opening the web")
            computer.runAndWait()
            webbrowser.get().open(yurl)
            break

    if ".com" in iput:
        while True:
            site = "https://www." + iput
            computer.say("Opening" + iput)
            computer.runAndWait()
            webbrowser.get().open(site)
            break

    if iput == "locate":
        while True:
            loc = "What are we trying to locate sir?"
            computer.say(loc)
            computer.runAndWait()
            locat = input("> ")
            lurl = 'https://google.com/maps/place/' + locat + '/&amp;'
            webbrowser.get().open(lurl)
            endmap = "This is" + locat + "sir"
            computer.say(endmap)
            computer.runAndWait()
            break

    if "youtube" not in iput and ".com" not in iput and iput!="mkdir" and iput!="directory" and iput!="locate" and iput!="google" and iput!="time" and iput!="joke" and iput!="file" and iput!='exit all':
            wiki_search = wikipedia.search(iput, results = 5)
            print(wiki_search)
            computer.say(wiki_search)
            computer.runAndWait()
            print("> Write in single quotes")
            while True:
                wiki_iput = input("> ")
                wiki_result = wikipedia.summary(wiki_iput, sentences = 3)
                print(wiki_result)
                computer.say(wiki_result)
                computer.runAndWait()
                break
            
    if iput == "exit all":
        while True:
            exit()

while True:
    computer()




    
