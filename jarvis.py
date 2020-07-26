import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import smtplib
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0])

engine.setProperty('voice', voices[1].id)

def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Very Good Morning!")

    elif hour>=12 and hour<16:
        speak("Very Good afternoon")

    else:
        speak("Very Good evening")

    speak("Hello Sir, I am Jarvis at your service ,how can i help you..")  

def screenshot():
    img = pyautogui.screenshot()
    img.save = ("Enter file path.png")  
  
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please..")
        return "None" 
    return query  

def sendEmail(to, content):
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password') 
    server.sendmail('youremail@gmail.com', to, content)
    server.close() 

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia'in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'search' in query:
            speak("what should i search ?")
            search = takeCommand().lower()
            chromepath = "File path/chrome.exe %s"
            wb.get(chromepath).open_new_tab(search + '.com')     

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'email to client' in query:
            try:
                speak("Tell the message")
                content = takeCommand()
                to = "clientEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry not able to send email")  
        
        elif "take screenshot"  in query:
            screenshot()
            speak("Done")

        elif 'offline' in query:
            quit()    
            

            

    


