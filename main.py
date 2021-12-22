import googlesearch
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from googlesearch import search

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<4:
            speak("It Seems Really Urgent Because You Contacted Me On Midnight, Go On And Tell How Can I help You?")
    if hour>=4 and hour<12:
        speak("Good Morning! I hope You Have a Good Day Today")
        print("Good Morning! I hope You Have a Good Day Today")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
        print("Good Afternoon!")   
    elif hour>=18 and hour<0:
        speak("Good Evening!")  
        print("Good Evening!")
    speak("Hello This Is Jarvis And You are My IRON MAN, Can You Please Tell Me How I can Help You?")   
    print("Hello This Is Jarvis And You are My IRON MAN, Can You Please Tell Me How I can Help You?")           

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("I didn't get it, Say that again please... or maybe I am not Built For that") 
        speak("I didn't get it, Say that again please... or maybe I am not Built For that") 
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sarthak.sidhant@gmail.com', 'Sarthak@44') #there's really no use of testing my password becoz it must be changed by then why waste your time?
    server.sendmail('sarthak.sidhant@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            print("looks like you want to watch some videos, Go on...")
            print("Opening Youtube...")
            print("Ah I forgot, So There is A Really Cool Guy Named Sarthak Sidhant On YouTube, Can You Please Subscribe to him He makes cool stuff like this (he made me) so please subscribe him on youtube, thanks!")
            speak("looks like you want to watch some videos, Go on...")
            speak("Opening Youtube...")
            speak("Ah I forgot, So There is A Really Cool Guy Named Sarthak Sidhant On YouTube, Can You Please Subscribe to him He makes cool stuff like this (he made me) so please subscribe him on youtube, thanks!")
        elif 'open google' in query:
            webbrowser.open("google.com")
            print("Oh! you want to have some time with the god Of information? Great! ")
            print("Opening Google...")
            speak("Oh! you want to have some time with the god Of information? Great! ")
            speak("Opening Google...")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
            print("What You Have An Error in Programming Again?")
            print("opening StackOverFlow....")
        elif 'music' in query:
            music_dir = 'C:\\Users\\User\\Desktop\\project\\test'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime} and your watch is in your pocket, Wear it! you always keep asking for time and stupid stuff not realising you are wasting your time, Remember Time Is Important and its valuable dont waste it ")
            speak(f"Sir, the time is {strTime} and your watch is in your pocket, Wear it! you always keep asking for time and stupid stuff not realising you are wasting your time, Remember Time Is Important and its valuable dont waste it ")
        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("opening Visual Studio Code")
            print("opening Visual Studio Code")
        elif 'email to school' in query:
            try:
                speak("Sure! What should I say then?")
                print("Sure! What should I say then?")
                content = input("What Email Should I Say")
                to = "sarthaksidhantisopolice@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sarthak, Cant Send The Email Right Now, Can You Try Again Later")    
        elif 'execute operation 42' in query:
            speak("Saving Resources...")
            print("Saving Resources...")
            speak("Initiating Shutdown...")
            print("Initiating Shutdown...")
            speak("Multiple Excursions Detected... ")
            print("Multiple Excursions Detected... ")
            speak("Cleaning Excursions...")
            print("Cleaning Excursions...")
            speak("Initiating Shutdown Confirm....")
            print("Initiating Shutdown Confirm....")
            speak("Initiating Vibranium Arc Reactor Shutdown")
            print("Initiating Vibranium Arc Reactor Shutdown")
            speak("Arc Reactor Shutdown Succesful")
            print("Arc Reactor Shutdown Succesful")
            speak("Jarvis is Turning Down")
            print("Jarvis is Turning Down")
            speak("Jarvis has left the chat")
            print("Jarvis has left the chat")
            break
        elif 'you are bad'in query:
            print("i am really sorry if my system is bad, here you can write a feedback to the developer")
            print("sarthaksidhantofficial@gmail.com")
            print ("you can also report bugs here") 
            speak("i am really sorry if my system is bad, here you can write a feedback to the developer")
            speak("sarthaksidhantofficial@gmail.com")
            speak("you can also report bugs here")
        elif 'you are good'in query:
            print("you made my day, thanks")
            print("you can write a email to the developer thanking him, i was made by him!")
            print("sarthaksidhantofficial@gmail.com")
            speak("you made my day, thanks")
            speak("you can write a email to the developer thanking him, i was made by him!")
        elif 'what can you do'in query:    
            speak("I can Do Alot Of Things")
            print("I can Do Alot Of Things")
            speak("i can send emails (use : email address, content), open youtube (use: open youtube), search wikipedia (use: wikipedia, search content), open google (use : open google), open stack overflow (use: open Stackoverflow), Tell Time (use: time), Open Code (use: open code), Bunk Classes :P (version 2 - coming soon), Science Fiction Talks - Beta (use: execute operation 42), Feedback Pages : good (use: you are good), bad (use: you are bad), Discord Logs Tell The Use Of The Bot When Connected to the Internet (version 2 - coming soon) And Alot Of Cool Things To Come Sooner :D")          
            print("i can send emails (use : email address, content), open youtube (use: open youtube), search wikipedia (use: wikipedia, search content), open google (use : open google), open stack overflow (use: open Stackoverflow), Tell Time (use: time), Open Code (use: open code), Bunk Classes :P (version 2 - coming soon), Science Fiction Talks - Beta (use: execute operation 42), Feedback Pages : good (use: you are good), bad (use: you are bad), Discord Logs Tell The Use Of The Bot When Connected to the Internet (version 2 - coming soon) And Alot Of Cool Things To Come Sooner :D")
        elif 'credits'in query:
            print("developed by SarthakSidhant (discord : Sarthak Sidhant#4374)")
            print("helped from the main project by code with harry")
            print("runs on any laptop/computer just needs some libraries installed")            
        elif 'search' in query:
            for i in search(query, tld="com", num=5, stop=5, pause=2):
                speak("Here Are The Search Results:")
                print(i)        
        elif 'repeat' in query:
            query = query.replace("repeat", "")
            speak(query)
            print(query)
        elif "jarvis" in query:
            speak("Yes Sir! Always Present At This Computer, You Need TO Give Me Commands")
            print("Yes Sir! Always Present At This Computer, You Need TO Give Me Commands")
        elif "email" in query:
            try:
                speak("Sure! What shall Be The Content?")
                print("Sure! What shall Be The Content?")
                content = takeCommand()
                speak("Please Tell The Email Address I Should Send The Email To:   ")
                to = input("Please Tell The Email Address I Should Send The Email To:  ")    
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sarthak, Cant Send The Email Right Now, Can You Try Again Later")
                print("Sorry Sarthak, Cant Send The Email Right Now, Can You Try Again Later")
            #A TRUE EDITH FUNCTION
        elif "set target" in query:
            speak("Sure! What shall Be The Target?")
            print("Sure! What shall Be The Target?")
            target = takeCommand()
            speak("Are You Sure That You Want To Set The Target To " + target + "?")
            print("Are You Sure That You Want To Set The Target To " + target + "?")
            print("input yes or no")
            conf=input("Y/N: ")
            if conf=="yes" or conf=="y" or conf=="Yes" or conf=="Y" or conf=="YES" :
                speak("Copy That!")
                print("Copy That!")
                speak("Target Set To: " + target)
                print("Target Set To: " + target)
                speak("Initating Start Of Attack")
                print("Initating Start Of Attack")
                speak("Intercept Point Determined")
                print("Intercept Point Determined")
                speak("Releasing Kill Vehicle")
                print("Releasing Kill Vehicle")
                speak("Drumroll Please")
                print("Drumroll Please, BA DUM TSS")
                speak("Kill Vehicle Released")
                print("Kill Vehicle Released")
                speak("Kill Vehicle Inbound")
                print("Kill Vehicle Inbound")
                speak("Kill Vehicle Approaching The Target")
                print("Kill Vehicle Approaching The Target")
                speak("Target 3 hundred meter From The Intercept Point")
                print("Target 300m From The Intercept Point")
                speak("Target 2 hundred meter From The Intercept Point")
                print("Target 200m From The Intercept Point")
                speak("Target 1 hundred meter From The Intercept Point")
                print("Target 100m From The Intercept Point")
                speak("Target fifty meter From The Intercept Point")
                print("Target 50m From The Intercept Point")
                speak("Target thirty meter From The Intercept Point")
                print("Target 30m From The Intercept Point")
                speak("Target twenty meter From The Intercept Point")
                print("Target 20m From The Intercept Point")
                speak("Target 10 meter From The Intercept Point")
                print("Target 10m From The Intercept Point")
                speak("Target 5 meter From The Intercept Point")
                print("Target 5m From The Intercept Point")
                speak("Target Destroyed")
                print("Target Destroyed")
                speak("Paying Last Rites To The Target aka: " + target)
                print("Paying Last Rites To The Target aka: " + target)

            else:
                speak("Target Decline")
                print("Target Decline")
    