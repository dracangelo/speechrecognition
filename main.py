import speech_recognition as sr

r = sr.Recognizer()

def record_speech():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print("Unknown")
        except sr.RequestError:
            print("Request error")
        return voice_data

print("Listening...")