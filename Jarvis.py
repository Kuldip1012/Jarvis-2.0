import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0])
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(): #wish krse time na hisaabe speak function ni help thi
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hey Kuldip How Can I Help You ?")
 

def takeCommand():
    '''It Takes Microphone Input From The User and Returns string Output '''

    r = sr.Recognizer()  # Aa Class Help Kre Audio recognize Krvama
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)  # Aa Badha Speech recogntion Module Mathi Aave 6e

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en-in")
        print(f"User Said : {query}\n ")

    except Exception as e:
        # print(e)
        print("Say That Again Please ..")
        return "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    # if 1:
    query = takeCommand().lower()
    # Logic For Executing Tasks Based On Query
    if 'wikipedia' in query:
        speak('searching wikipedia...')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences = 1)
        speak("According To wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    
    elif 'open google' in query:
        webbrowser.open("google.com")
    
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'my website' in query:
        webbrowser.open("https://onlinegovjob.in/")
    
    elif 'new post' in query:
        webbrowser.open("https://onlinegovjob.in/wp-admin/post-new.php")

    elif 'play music' in query:
        music_dir = 'E:\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'time details' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, The Time is {strTime}")

    elif 'vs code' in query:
        CodePath = "C:\\Users\\dheme\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(CodePath)

    elif 'email to harry' in query:  # send email lakh skie ane nam thi detect kr skie pela ek dictionary banai nakhvani keys ma nam ane values email id hogi 
        try:
            speak("what should i say ?")
            content = takeCommand()
            to = "yourEmail@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("sorry, I'm Not Able To Send Email")


