import speech_recognition as sr
from time import ctime
import webbrowser
import time 

r = sr.Recognizer()

def record_speech(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Unknown")
        except sr.RequestError:
            print("Request error")
        return voice_data
    
def respond(voice_data):
    if 'what is your name' in voice_data:
        print('autoaispeech')
    if 'what time is it' in voice_data:
        print(ctime())
    if 'find' in voice_data:
        search = record_speech("what do you want to search for?")
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        print('here is what I found ' + search)
    if 'find location' in voice_data:
        location = record_speech("what is the location of?")
        url = 'https://www.google.com/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('here is what I found about ' + location)
    if 'exit' in voice_data:
        exit()
        

time.sleep(1)
print("Listening...")
while 1:
    voice_data = record_speech()
    respond(voice_data)