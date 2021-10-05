import pyjokes # i swear to god if you don't pip install imma be pretty mad
import pyttsx3

engine = pyttsx3.init() # you porbably didn't install pip stuff
voices = engine.getProperty('voices') # until you get more common sense dont read this code.
engine.setProperty('voice', voices[1].id) # okay you probably ARE smart now. just uses properties to get a joke from the api.
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+-20)

def speak(audio): # AUDIO? so fancy owo
    engine.say(audio)
    engine.runAndWait()

def joke():
    speak(pyjokes.get_joke()) # gets the joke, haha

if __name__ == "__main__":
    joke() # tells a joke. an example is my life
