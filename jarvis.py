# Programmed Virtual Assistant

import pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia
import webbrowser 
import os
import smtplib
import requests
import pyautogui
import PyPDF2
import pywhatkit as kit
import pyjokes
import random 
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[len(voices)-1].id)
engine.setProperty('rate', 180)

def speak(audio):
    print('System: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning sir!')
    
    elif hour>=12 and hour<18:
        speak('Good Afternoon sir!')

    else:
        speak('Good Evening sir!')

    speak('I am your creation, Leo')
    speak('Please tell me, how may I help you ?')

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio,language='en-in')
        print(f'User: {query}\n')

    except sr.UnknownValueError:
        return "none"

    query = query.lower()
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    print("FROM (Sender Email) :",end=" ")
    sender = input()
    print('Password :',end=" ")
    pwd = input()
    # server.login('lightyagami3108@gmail.com', pwd)
    server.login(sender, pwd)
    server.sendmail(sender, to, content)
    server.close()

def pdf_reader():
    speak('sir, please type the name of the pdf, you want me to read')
    print('Enter pdf name:', end=" ")
    var = input()
    book = open(f'{var}.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f'sir, there are {pages} pages in this book, tell me which page you want me to read')
    print('Please enter the page number:', end=" ")
    p_no = int(input())
    page = pdfReader.getPage(p_no-1)
    text = page.extractText()
    speak(text)

def TaskExecution():

    wishme()
    while True:
        query = takecommand()

# logics for executing tasks based on query
        if 'what\'s up' in query or 'how are you' in query:
            msg = ['I am fine sir', 'Good sir', 'Just doing my thing!', 'I am nice sir', 'I am fine and full of energy sir']
            speak(random.choice(msg))
            que =['What about you ?', 'How are you ?']
            speak(random.choice(que)) 

        elif 'i am good' in query or 'i am fine' in query:
            speak('That\'s good to hear from you, sir')
            speak('May I help you with something')

        elif 'hello' in query or 'hi' in query:
            speak('Hello sir, may I help you with something ?')

        elif 'no' in query:
            speak('Okay then, I am taking your leave') 

        elif 'thanks' in query or 'thank you' in query:
            speak('It\'s my pleasure sir')

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}") 
            speak('Anything else sir ?')

        elif 'date' in query:
            strdate = datetime.datetime.now().strftime("%A, %d %B %Y")
            speak(f"Sir, the date is {strdate}.")
            speak('Anything else sir ?') 

        elif "wikipedia" in query:
            speak("Searching wikipedia..")    
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 1)
            speak("According to wikipedia")
            speak(results)
            speak('Done sir, anything else ?')

        elif 'open youtube' in query:
            speak('What do you want to search in youtube?')
            get = takecommand()
            # webbrowser.open('youtube.com')
            url = 'https://www.youtube.com/results?search_query='
            webbrowser.get().open_new(url+get)
            speak('Done sir, anything else ?')

        elif 'open google' in query:
            speak('Sir, what do you want to search ?')
            get = takecommand()
            # webbrowser.open('google.com')
            url = 'https://www.google.com/search?q='
            webbrowser.get().open_new(url+get)    
            speak('Done sir, anything else ?')

        # elif 'open google' in query:
        #     speak('sir, what do you want to search')
        #     cm = takecommand().lower()
        #     webbrowser.open(f'{cm}')

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
            speak('Done sir, anything else ?')

        elif 'open music' in query:
            music_dir = 'C:\\Music\\Favourite Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak('Done sir, anything else ?')

# to open any application
        elif 'open visual studio code' in query:
            codepath = "C:\\Users\\nawani\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak('Done sir, anything else ?')

        elif 'open pycharm' in query:
            codepath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2\\bin\\pycharm64.exe"
            os.startfile(codepath)
            speak('Done sir, anything else ?')

        elif 'open notepad' in query:
            codepath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad'
            os.startfile(codepath)
            speak('Done sir, anything else ?')

        elif 'open command prompt' in query:
            codepath = 'C:\\Users\\nawani\\AppData\\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt'
            os.startfile(codepath)
            speak('Done sir, anything else ?')

# to close any application
        elif 'close visual studio code' in query:
            speak('Okay sir, closing visual studio code')
            os.system('taskkill /f /im Code.exe')
            speak('Done sir, anything else ?')

        elif 'close pycharm' in query:
            speak('Okay sir, closing pycharm')
            os.system('taskkill /f /im pycharm64.exe')
            speak('Done sir, anything else ?')

        elif 'close notepad' in query:
            speak('Okay sir, closing notepad')
            os.system('taskkill /f /im notepad.exe')
            speak('Done sir, anything else ?')

# to find a joke
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        # elif 'ip address' in query:
        #     ip = get('https://api.ipify.org').text
        #     speak(f'Your IP address is: {ip}')

        elif 'my location' in query or 'our location' in query:
            speak('Wait sir, let me check')
            try:
                ipadd = requests.get('https://api.ipify.org').text
                url = 'http://get.geojs.io/v1/ip/geo/' + ipadd + '.json'
                geo_req = requests.get(url)
                geo_data = geo_req.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f'Sir I am not sure but i think we are in {city} city of {country} country, anything else!')
            except Exception as e:
                speak('Sorry sir, due to certain network issue I am unable to find out our location')
                pass

        elif 'take a screenshot' in query or 'take screenshot' in query:
            speak('sir, please tell me the name of this screenshot')
            name = takecommand().lower()
            speak('hold on sir, we are running your command in few seconds')
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f'{name}.png')
            speak('Done sir, screenshot has been sucessfully saved in the main folder, anything else ?')

        elif 'email to me' in query:
            try:
                speak('Sir, tell me the content..')
                content = takecommand()
                speak('Tell me the sender as well as reciever email..')
                print('TO (Recipient Email) :',end=" ")
                to = input()
                sendEmail(to, content)
                speak('Email has been sucessfully sent, anything else ?')
            except Exception as e:
                print(e)
                speak('You have entered incorrect email or password!')  

        elif 'send whatsapp message' in query:
            try:
                speak('Type the reciever\'s number, sir')
                no = int(input("Number: +91"))
                speak("Tell me the message, sir")
                msg = takecommand().lower()
                speak('Tell me the time, at which you want to send this message')
                Hr = int(input('Hour: '))
                Min = int(input('Minute: '))
                kit.sendwhatmsg(f'+91{no}', msg, Hr, Min)
                speak('Message has been sucessfully sent, anything else ?')
            except Exception as e:
                speak('Sorry sir, I am unable to send your message')
                speak('Please try again after some time')

        elif 'open pdf reader' in query or 'read pdf' in query:
            pdf_reader()

        elif 'shut down the system' in query:
            os.system('shutdown /s /t S')

        elif 'restart the system' in query:
            os.system('shutdown /r /t S')

        elif 'sleep my pc' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'abort' in query or 'quit' in query:
            speak('Okay..')
            speak('Bye sir! Have a good day.')
            sys.exit()

        elif 'go to sleep' in query or ' you can sleep' in query:
            speak('Okay sir, I am going to sleep, you can call me anytime')
            break

        else:
            speak('Sorry sir, I didn\'t get that! Can you please say that again ?')
            
   
if __name__ == "__main__":
    while True:
        wake_up = takecommand()
        if 'leo' in wake_up or 'wake up' in wake_up:
            TaskExecution()
        elif 'bye leo' in wake_up:
            msg = ['Bye-bye sir! Have a nice day', 'Thanks for having me sir, have a good day', 'My pleasure to help you sir, see you later']
            speak(random.choice(msg))
            sys.exit()      

 