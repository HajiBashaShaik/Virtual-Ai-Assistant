import pyttsx3 as ts

def text_to_speech(text):
    engine= ts.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate', 'rate - 70')
    engine.say(str(text))
    engine.runAndWait()  

