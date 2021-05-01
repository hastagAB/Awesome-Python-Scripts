import pyttsx3 as pt
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import smtplib  # enable less secure apps from google security settings for email feature to work

# make a dictionary with names as keys and emails as email addresses to store all the email addresses
emails = {"receiver1 name": "receiver1 full email id", "receiver2 name": "receiver2 full email id"} # store as many as you like

engine = pt.init('sapi5')  # MS Speech API, we can use the in built voice of windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

wb.register('chrome', None,
                    wb.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))
chromeBrowser = wb.get('chrome')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning boss! I am jarvis, your desktop assistant, what would you like me to do?")
    elif 12 <= hour < 17:
        speak("Good Afternoon boss! I am jarvis, your desktop assistant, what would you like me to do?")
    else:
        speak("Good Evening boss! I am jarvis, your desktop assistant, what would you like me to do?")


def getCommand():
    # takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 550
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"You said: {query}\n")

    except Exception as e:
        return "None"

    return query


def getCommand_no_text():
    # takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 550
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio)

    except Exception as e:
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # sender's login details to be input here
    server.login('your_full_email id',
                 'password_here')  # better store your password in a text file due to security concerns
    server.sendmail('your_full_email id', to, content)
    server.close()


if __name__ == '__main__':
    while True:
        hotword = getCommand_no_text().lower()
        if hotword == "hey jarvis":
            wishMe()
            while True:
                query = getCommand().lower()

                # Logic for executing tasks based on query
                if query == 'none':
                    speak("Say that again please")

                elif 'how are you' in query:
                    speak("I am fine, thank you")

                elif 'i love you' in query:
                    speak("Ummm, i am not sure about that!")

                elif 'what do you do' in query:
                    speak("I assist you, didn't you know?")

                elif 'tell me a joke' in query:
                    speak("don't trust the atoms, they make up everything")


                elif 'wikipedia' in query:          # example: shahrukh khan according to wikipedia
                    speak("Searching wikipedia...")
                    query = query.replace('wikipedia', '')
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    speak(results)


                elif 'open youtube' in query:
                    speak("Opening YouTube...")
                    chromeBrowser.open("youtube.com")


                elif 'open hackerrank' in query:
                    speak("Opening Hackerrank...")
                    chromeBrowser.open("hackerrank.com")


                elif 'open gmail' in query:
                    speak("Opening Gmail...")
                    chromeBrowser.open("gmail.com")


                elif 'open amazon' in query:
                    speak("Opening Amazon...")
                    chromeBrowser.open("amazon.in")


                elif 'open google' in query:
                    speak("Opening Google...")
                    chromeBrowser.open("google.com")


                elif 'open vs code' in query:
                    speak("Opening VS Code...")
                    path = "C:\\Users\\Gundeep\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(path)


                elif 'open pycharm' in query:
                    speak("Opening PyCharm...")
                    path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.3\\bin\\pycharm64.exe"
                    os.startfile(path)


                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(strTime)
                    speak(f"The time is {strTime}")


                elif 'play music' in query or 'play some music' in query:
                    music_dir = 'D:\\Music'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[random.randint(0, 52)]))

                # apply the if else clauses to recognize different people and identify them using the dictionary created in the beginning
                elif 'send an email' in query or 'send email' in query:
                    try:
                        speak("Whom do you want to send to?")
                        to = getCommand().lower()

                        while ("xyz" not in to) and ("abc" not in to):
                            speak("Sorry, the name is not in the list, please choose from the list")
                            to = getCommand().lower()

                        if 'xyz' in to:                 # xyz is the word(name or something, addressing the person to send to) appearing in the query input through microphone
                            to = emails["xyz's name as in the dictionary"]

                        elif 'abc' in to:               # similarly for some other recipient. enter as many as you like
                            to = emails["abc's name as in the dictionary"]

                        speak("What should I say?")
                        content = getCommand()

                        sendEmail(to, content)
                        speak("Email has been sent")

                    except Exception as e:
                        speak("Sorry, I am unable to send the email at the moment")


                elif 'goodbye jarvis' in query or 'good bye jarvis' in query or 'get lost' in query:
                    speak("Goodbye sir, see you later")
                    break

                else:
                    speak("Sorry, I am not programmed to execute this command")

            break
        elif hotword == "shut it down jarvis":
            break
        
        else:
            print("Say 'Hey jarvis' to invoke your voice assistant")
            print("Say 'Shut it down jarvis' to close it")
