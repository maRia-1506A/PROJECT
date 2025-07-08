'''
ctrl+shift+p: select interpreter >> +create virtual environment >> python env select
'''
# import
import speech_recognition as sr
import webbrowser
import pyttsx3
import MusicLibrary
import requests
from openai import OpenAI
from dotenv import load_dotenv
import os
from gtts import gTTS
import pygame

# Load environment variables from .env
load_dotenv()

# Get API keys from environment variables
open_api_key = os.getenv("OPENAI_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
print("Loaded OpenAI Key:", open_api_key)

# initialize recognizer and Speech Engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()  # start the engine


# function
def speak_old(text):
    engine.say(text)  # say something
    engine.runAndWait()  # wait until speech is finished


def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():  # wait for music to finish
        continue

    pygame.mixer.music.stop()
    pygame.mixer.quit()

    if os.path.exists("temp.mp3"):
        os.remove("temp.mp3")


def AIprocess(command):
    client = OpenAI(api_key=open_api_key)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "You are a vitual assistant named Jarvis skilled in geenral tasks like Alexa or Google Cloud. Give short responses"},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        '''
        play onedirection
        ['play','one']
        '''
        link = MusicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=bd&apiKey={news_api_key}")
        if r.status_code == 200:
            # json response
            data = r.json()
            # extract the articles
            articles = data.get("articles", [])

            for article in articles:
                title = article.get("title")
                if title:
                    speak(title)
    else:
        # let OpenAI handle the request
        output = AIprocess(c)
        speak(output)


# main program
if __name__ == "__main__":  # it will run only this file not another file
    speak("Initializing jarvis....")
    while True:
        # obtain command from the microphone
        r = sr.Recognizer()

        # recognize speech using google
        print("Recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)

            # wake word detection
            word = r.recognize_google(audio)
            if "jarvis" in word.lower():
                speak("Yes")

                # listen for command after wake word
                with sr.Microphone() as source:
                    print("Jarvis active.....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("Command: ", command)

                    processCommand(command)

        except Exception as e:
            print("error; {0}".format(e))
