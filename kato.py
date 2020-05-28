#!C:\Python36\python.exe
# importing speech recognition package from google api 

import speech_recognition as sr  
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # save/open files 
import wolframalpha # to calculate strings into formula 
from selenium import webdriver # to control browser operations 
import pyglet

animation = pyglet.image.load_animation('./Src/kato.gif')
animSprite = pyglet.sprite.Sprite(animation)


w = animSprite.width
h = animSprite.height

window = pyglet.window.Window(width=w, height=h)

r,g,b,alpha = 0.5,0.5,0.8,0.5


pyglet.gl.glClearColor(r,g,b,alpha)

@window.event
def on_draw():
    window.clear()
    animSprite.draw()
pyglet.app.run()


## funda
bukaan = os.startfile

# py -3.6 kato.py
# multiple interpreter
# py -3.6 get-pip.py pyglet


def hai(): # outer function      
    playsound.playsound('./Src/ok.mp3')

def dota(): # outer function      
    playsound.playsound('./Src/lina.mp3')  

def hiki():       
    playsound.playsound('./Src/hiki.mp3')    

def lewd():       
    playsound.playsound('./Src/lewd.mp3')    
num = 1
def assistant_speaks(output): 
    global num 
  
    # num to rename every audio file  
    # with different name to remove ambiguity 
    num += 1
    print("PerSon : ", output) 
  
    toSpeak = gTTS(text = output, lang ='en', slow = False) 
    # saving the audio file given by google text to speech 
    file = str(num)+".mp3"  
    toSpeak.save(file) 
      
    # playsound package is used to play the same file. 
    playsound.playsound(file, True)  
    os.remove(file) 
  
  
  
def get_audio(): 
  
    rObject = sr.Recognizer() 
    audio = '' 
  
    with sr.Microphone() as source: 
        print("Speak...") 
          
        # recording the audio using speech recognition 
        audio = rObject.listen(source, phrase_time_limit = 2)  
    print("Stop.") # limit 5 secs 
  
    try: 
  
        text = rObject.recognize_google(audio, language ='en-US') 
        print("You : ", text) 
        return text 
  
    except: 
  
        assistant_speaks("Could not understand your audio, PLease try again !") 
        return 0

def process_text(input): 
    try: 
        if 'search' in input or 'play' in input: 
            # a basic web crawler using selenium 
            search_web(input) 
            return
  
        elif "who are you" in input or "define yourself" in input: 
            hiki()
            from playsound import playsound
            
            assistant_speaks(playsound('./Src/spree.mp3')) 
            return
  
        elif "who made you" in input or "created you" in input: 
            speak = "I have been created by Sheetansh Kumar."
            assistant_speaks(speak) 
            return
  
        elif "geeksforgeeks" in input:# just 
            speak = """Geeks for Geeks is the Best Online Coding Platform for learning."""
            assistant_speaks(speak) 
            return
  
        elif "calculate" in input.lower(): 
              
            # write your wolframalpha app_id here 
            app_id = "WOLFRAMALPHA_APP_ID" 
            client = wolframalpha.Client(app_id) 
  
            indx = input.lower().split().index('calculate') 
            query = input.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            assistant_speaks("The answer is " + answer) 
            return
  
        elif 'open' in input: 
              
            # another function to open  
            # different application availaible 
            open_application(input.lower())  
            return
  
        else: 
  
            assistant_speaks("I can search the web for you, Do you want to continue?") 
            ans = get_audio() 
            if 'yes' in str(ans) or 'yeah' in str(ans): 
                search_web(input) 
            else: 
                return
    except : 
  
        assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?") 
        ans = get_audio() 
        if 'yes' in str(ans) or 'yeah' in str(ans): 
            search_web(input)   

def search_web(input): 
  
    driver = webdriver.Firefox() 
    driver.implicitly_wait(1) 
    driver.maximize_window() 
    
  
    if 'youtube' in input.lower(): 
  
        assistant_speaks("Opening in youtube") 
        indx = input.lower().split().index('youtube') 
        query = input.split()[indx + 1:] 
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query)) 
        return
    

    elif 'nekopoi' in input.lower(): 
        lewd()
        assistant_speaks("Opening nekopoi") 
        driver.get("https://poi.sinxdr.workers.dev/") 
        return
  
    else: 
  
        if 'google' in input: 
  
            indx = input.lower().split().index('google') 
            query = input.split()[indx + 1:] 
            driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
  
        elif 'search' in input: 
  
            indx = input.lower().split().index('google') 
            query = input.split()[indx + 1:] 
            driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
  
        else: 
  
            driver.get("https://www.google.com/search?q =" + '+'.join(input.split())) 
  
        return
  
  
# function used to open application 
# present inside the system. 
def open_application(input): 
  
    if "chrome" in input: 
        assistant_speaks("Google Chrome") 
        bukaan('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') 
        return
  
    elif "firefox" in input or "mozilla" in input: 
        assistant_speaks("Opening Mozilla Firefox") 
        bukaan('C:\Program Files\Mozilla Firefox\\firefox.exe') 
        return

    elif "discord" in input: 
        hai()
        assistant_speaks("Opening Discord") 
        bukaan('C:\\Users\\bib\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\Discord.lnk') 
        return

    elif "dota" in input: 
        dota()
        assistant_speaks("Opening Dota") 
        bukaan('C:\\Users\\bib\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Steam\\Dota 2.url') 
        return    


  
    else: 
  
        assistant_speaks("Application not available") 
        return  
# Driver Code 
if __name__ == "__main__": 
    
    import playsound       
    playsound.playsound('./Src/intro.mp3')
    assistant_speaks("yoo")
    name ='Master'
     
    assistant_speaks("" + name + '.') 
      
    while(1): 
  
        assistant_speaks("What's next?") 
        text = get_audio().lower() 
  
        if text == 0: 
            continue
  
        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
            assistant_speaks("Ok bye, "+ name+'.') 
            break
  
        # calling process text to process the query 
        process_text(text) 