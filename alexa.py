import speech_recognition as sr   #For speech recognition
import pyttsx3                    #For text to speech
import pywhatkit                  #For using alexa to do everything
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()    # To create a speech_recognition object which will listen to what we say.
engine = pyttsx3.init()  # Initialising the engine so that alexa can talk to us. Initialise it with some dummy or sapi5  
# engine.say('I am your alexa')
# engine.say('What can i do for you?')
# engine.runAndWait()
voices = engine.getProperty('voices')       # To change alexa's voice.
engine.setProperty('voice', voices[1].id)  

def talk(text):
    engine.say(text)
    engine.runAndWait()

# talk('Hi Aman')
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')  
            voice = listener.listen(source)        # we are using the above created object to listen to what we are saying
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                talk(command)
                command = command.replace('alexa','')
                print(command)
            else:
                talk(command)
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()