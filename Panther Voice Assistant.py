import pyttsx3 
import datetime
import wikipedia
import webbrowser
import os
import time
import pywhatkit
import pyautogui
import speech_recognition as sr 
engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id) this for demo of voice 
engine.setProperty('voice',voices[0].id) # you can change the male or female voice by 0 & 1


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    speak 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12: 
        speak('good morning Sir')
    elif hour>=12 and hour<=18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")   
    speak("I am  Panther ,  your personal assistant. Now tell me how may i help you")              

def takeCommand():
    '''it take microphone input fromt he user and return string as output '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 2
        audio = r.listen(source)
        
    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in') 
        print(f"user said: {query}\n")
    except Exception as e:
#         print("E")
        
        print("say that again ......")
        return "none"
    return query
if __name__ == "__main__":
    print("panther activated")
#     wishMe()
    
    while True:

#     if 1:
        query = takeCommand().lower()
#     logic for solving problems based on wikipedia and google

        if 'wikipedia' in query:
            speak(" searching on wikipedia.......")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)# sent=2 for atleast taken two sentences 2 sent we cane also cahnge to more
            speak("according  to wikipedia")
            print(results)
            speak(results)
                
        elif 'wake up panther' in query:
            speak(" welcome back sir ! what can i do for you today")
           
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
#         elif "wake up " in query:
#             wishMe()
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'type' in query:
            query = query.replace("type","")
#             pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.press("enter")
        
        elif 'play music' in query:
            music_dir = 'D:\\MOVIE'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir , the time is {strTime}")
            print(strTime)
        
        elif 'stop'in query:
            speak("thank you sir  you can call me anytime ")
            os.stop()
            
        elif 'who are you' in query:
            ("my name is panther , i am a voice assistant based on artificial intenlligence ")
            
        elif 'hey panther' in query:
            wishMe()
            
        elif 'how are you' in query:
            
            speak(" i m perfect sir , i hope you're fine , so tell me what brings you here ? ")
        
        elif 'i am here'  in query:
            speak("well this is great idea  sir ,  i hope my abilities make you you feel special. ")
        
        elif 'can you speak Hindi' in query:
            speak(" sir , i know that hindi is most spoken language . currently me and my boss working on it so i can speak hindi as soon as possible")
        
        elif 'greet me' in query:
            wishMe()
        
        elif 'greet everybody' in query:
            speak(" hello everybody  ,   its nice to meeting you all  , i hope you all doing well ,  you can ask anything to me")
        
        elif 'why i choose' in query:
            speak("sir , you choose me as your Major Project ,because choosing me as your personal assitant ,can offer you ,a quick versatile informatiom retrival  ,and you can assist any task easily with me ,and i have ability, to engage in natural languages conversation. ")
        
        elif 'tell us about your future plan' in query:
            speak("My purpose is to help you ,  with any question , or task  , you have to best of my abilities ")
        
        elif 'do you hear' in query:
            speak("yess i hear all the conversation , but reply only when you tell me reply")
            
        elif 'open' in query :
            
            query = query.replace("open","")
            query = query.replace("panther","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            speak(query)
#             pyautogui.sleep(2)
            pyautogui.press("enter")
        
        elif 'close' in query :
            query = query.replace("open","")
            query = query.replace("panther","")
            pyautogui.press("super")
            speak("i m closing ")
            pyautogui.hotkey("alt","f4")
            #remain for check
        
        elif 'take screenshot' in query :
            speak("i m taking screenshot")
            pyautogui.press("prtsc")
            
        elif 'lock screen' in query :
            speak(" screen locked in 2 seconds")
            pyautogui.press("super")
            pyautogui.hotkey("win","L")
        
        elif 'go to search' in query :
            
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("tab")
    
        
        elif 'on youtube' in query:
            speak("this is what i found sir")
            query = query.replace("on youtube","")
            query = query.replace("panther","")
            web = " htps://www.youtube.com/results?search_query= " + query
            webbrowser.open(web)
            pywhatkit.playonyt(query)
            
        elif 'close tab' in query :
            pyautogui.press("super")
            speak("i m closing ")
            pyautogui.hotkey("ctrl","w")
            pyautogui.press("enter")
            
            
        elif 'pause' in query:
            pyautogui.press("space")
        
        elif 'play'  in query:
            pyautogui.press("space") 
            
        elif 'enter' in query:
            pyautogui.press("enter")
            
        elif 'use my whatsapp' in query:
            web = "https://web.whatsapp.com/" 
            webbrowser.open(web)
            
        elif 'search contact' in query:
            query = query.replace("search contact","") 
            pyautogui.typewrite(query)
            speak("this is what i found")
            pyautogui.press('tab')
            pyautogui.press('enter')
            
        elif 'type message' in query:
            query = query.replace("type message","")
            pyautogui.typwrite(query)