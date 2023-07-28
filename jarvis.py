import pyttsx3 # pip install pyttsx3 -> allows conversion of txt to speech
import datetime
import speech_recognition as sr # pip install SpeechRecognition -> recognizes user's voice through the mic.
import wikipedia # pip install wikipedia ->
import smtplib  # built in module
import webbrowser as wb
import os
import pyautogui # pip install pyautogui -> enables screenshot to be taken
import psutil  # pip install psutil
import pyjokes  # pip install pyjokes


engine = pyttsx3.init() # initializes the Text-to-Speech (TTS) engine using the pyttsx3 library.


def speak(audio):
    # function speak that passes a variable audio
    engine.say(audio)
    engine.runAndWait()

def time():
    # function that give current time
    Time = datetime.datetime.now().strftime("%I:%M:%S") # format: hr, min. sec
    speak("the current time is")     # whenever time() is called, AI will say the string passed 
    speak(Time)

def date():
    # function that gives current date
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")     # whenever date() is called, AI will say the string passed
    speak(date) # call the speak function and pass the date variable
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Alex!") # function call with passed string
    time() # function call
    date() # function call
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning Alex!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Alex")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Alex")
    else:
        speak("Good night Alex")

    speak("Jarvis at your service. Please tell me how I can help you?")

def takeCommand():
    # define function that takes command from user
    r = sr.Recognizer() # initialize the recogrnizer in the r variable
    with  sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # wait 1 sec and listen for audio
        audio = r.listen(source)   # listen to the mic -> pass source var in the listen function

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(query)

    except Exception as e:  # error handling
        print(e)
        speak("Say that again please...")

        return "None"
    return query   # if try works...return query

def sendEmail(to, content): 
    # define sendEmail() takes 2 parameters: recipient and email content
    server = smtplib.SMTP('smtp.gmail.com', 587)  #gmail port
    server.ehlo()
    server.starttls   # Puts the connection to the SMTP server into TLS mode.
    server.login('example@gmail.com', 'password')
    server.sendmail('example@gmail.com', to, content)
    server.close()

def screenshot():
    # define screenshot function
    img = pyautogui.screenshot()  # built in function to take screenshot
    img.save("C:/Users/user/Desktop/Afree-tec/projects/Jarvis-AI/img.png")   # save image in current folder

def cpu():
    # function that gets cpu usage
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+ usage)   # concatenate string with usage var
    battery = psutil.sensors_battery()   # return a list of items related to battery status
    speak("Battery is at")
    speak(battery.percent)  # return % of battery

def jokes():
    speak(pyjokes.get_joke())  #fetch jokes from jokes lib and return to speak function


if __name__ == "__main__":  # module that defines the wishme() -> main function
    wishme() # function call  -> execute function when module is run as a script
    while True:
        query = takeCommand().lower()  # convert text from takeCommand to lowercase

        if 'time' in query:  # if query contains time string, call time()  -> when user says the word time in query
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2) # return summary -> get second sentence of the result
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'recipient@gmail.com'
                sendEmail(to, content)

                speak("content")
            except Exception as e:
                print(e)
                speak("Unable to send the email")

        elif 'search in chrome' in query:
            speak("What should I search?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'  # add location
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')   # concatenate user request with .com

        elif 'logout' in query:
            os.system("shutdown -l")  # logs out user from system

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")   # shutdown the computer

        elif 'restart' in query:
            os.system("shutdown /r /t 1")  # restart computer

        elif 'play songs' in query:
            songs_dir = 'C:\Music' 
            songs = os.listdir(songs_dir)    # return list of songs present in directory
            os.startfile(os.path.join(songs_dir, songs[0]))    # start music files -> join path of song directory -> play first song
            
        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()   # take command from user
            speak("you said to remember that"+data)  # concatenate string with data
            remember = open('data.txt', 'w')  # open file in write format
            remember.write(data)  # write data AI gets from user and save into txt file
            remember.close()

        elif 'do you know anything' in query:
            remember =open('data.txt', 'r')  # open data.txt in read format
            speak("You told me to remember that" +remember.read())  # AI speaks data present in the file

        elif 'screenshot' in query:
            screenshot() # function call
            speak("Screenshot has been taken")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            speak("Okay Alex, shutting down the system")
            quit()
