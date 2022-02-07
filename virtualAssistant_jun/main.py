import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Hi, I am Your virtual assistant Jun!, please ask me any question, I am listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jun' in command:
                command = command.replace('jun', '')
                print(command)
    except:
        pass
    return command


def run_jun():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I can not hear you')
    elif 'are you single' in command:
        talk('Oh? What happen? I can not hear what you said.')
    elif 'joke' in command:
        print('Here you are')
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    else:
        talk('Please say the command again.')
        return run_jun()


while True:
    run_jun()
