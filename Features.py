import eel
import pyaudio
import pyautogui
import pyttsx3
import self
import speech_recognition as sr
from hugchat import hugchat

import requests
import pyquotegen
import webbrowser
import wikipedia
from oauthlib.uri_validate import query
from translate import Translator
import speech_recognition
import urllib.parse
from pydub import AudioSegment
from pydub.playback import play
import time
from datetime import datetime


from colored import fg, attr
reset = attr('reset')  # Resets the Text Color to Default.

@eel.expose
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        # eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        # eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"You : {query}")
        # eel.DisplayMessage(query)
        time.sleep(2)

    except Exception as e:
        return ""

    return query.lower()
#takecommand()


def playAssistantSound():
    music= r"C:\Users\Sanchit\PycharmProjects\ChatBot\assets\audio\start_sound.mp3"
    sound = AudioSegment.from_file(music)
    play(sound)
playAssistantSound()

print(f"Current Time: {datetime.now().strftime('%H:%M:%S')}, Date: {datetime.now().strftime('%Y-%m-%d')}, Day: {datetime.now().strftime('%A')}")




def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path=r"engine\cookies.json")  # Raw string for cleaner path handling
    conversation_id = chatbot.new_conversation()
    chatbot.change_conversation(conversation_id)
    response = chatbot.chat(user_input)
    print(response)
    # speak(response)
    return response


def open_youtube_search(query):
    base_url = "https://www.youtube.com/results?search_query="
    search_url = base_url + urllib.parse.quote(query)
    webbrowser.open(search_url)
# search = input("What you want to search?")
# open_youtube_search(search)


def audiototext():
    recognizer = speech_recognition.Recognizer()
    while True:

        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.5)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                print(f'Father: {text}')
                if text.lower()=="exit":
                    break
                # get_response(text)

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            continue
# audiototext()


def opener():
    from AppOpener import open
    app = input("Enter App Name to open:")
    try:
        [open(app, match_closest=True)]
    except FileNotFoundError:
        print("No App with Name", app)
#opener()


def closer():
    from AppOpener import close  #To Close Any App
    app = input("Enter App Name to close:")
    try:
        [close(app, match_closest=True)]
    except FileNotFoundError:
        print("No App with Name", app)
#closer()


def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty("volume", 0.5)
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    engine.say(text)
    engine.runAndWait()
#speak()

def spotify(self):
    self.query = takecommand().lower()
    # song
    if 'song please' in self.query or 'play some song' in self.query or 'could you play some song' in self.query:
        speak('Sir what song should i play...')
        song = takecommand()


    # spotify
    elif 'play' in self.query or 'can you play' in self.query or 'please play' in self.query:
        speak("OK! here you go!!")
        self.query = self.query.replace("play", "")
        self.query = self.query.replace("could you play", "")
        self.query = self.query.replace("please play", "")
        webbrowser.open(f'https://open.spotify.com/search/{self.query}')
        time.sleep(19)
        pyautogui.click(x=1055, y=617)
        print('Enjoy!' + reset)
        speak("Enjoy Sir!!")
# spotify(self)


def spotify():
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth
    import webbrowser

    # Replace with your actual Client ID, Client Secret, and Redirect URI
    client_id = 'd7fd6fca60d54a86b156a58ed3be0ec0'
    client_secret = 'b3a5bac8aa644bb0bf63dea51c07b305'
    redirect_uri = 'http://localhost:8888/callback'

    # Set up Spotify authentication
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=redirect_uri,
                                                   scope='user-read-private user-read-email'))

    def play_song(song_name):
        if 'song please' in self.query or 'play some song' in self.query or 'could you play some song' in self.query:
            speak('Sir what song should i play...')
            song = takecommand()
        results = sp.search(q=song_name, type='track', limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            track_url = track['external_urls']['spotify']
            speak('Playing' + track)
            webbrowser.open(track_url)

            print(f"Opening '{track['name']}' by {track['artists'][0]['name']}' in your web browser.")
        else:
            print(f"No results found for '{song_name}'")
spotify()




# To Get Weather Forecast
def weather():
#API key from OpenWeatherMap
    api_key = '87bb4a8443fd0ec621a73e5b390fcbb2'
    city = input("Enter City :")
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weathers = data['weather'][0]
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weathers['description']}")
    else:
        print("Error: Could not retrieve weather data")
#weather()


#To Search on Wikipedia
def MediaWiki():
    import wikipedia
    wiki = input("What you want to search on Wikipedia? : ") or takecommand()
    print("What you want to search on Wikipedia? :")
    wikipedia.set_lang('en')
    search_results = wikipedia.search(wiki)
    print(search_results)
    page = wikipedia.page(wiki)
    print(wikipedia.summary(wiki, sentences=2))
    #if Want to Print in Webpage Details in Pycharm only
    # print(page.content)
    # print(page.title)
    url = page.url
    webbrowser.open_new(url)
# MediaWiki()


def news():
    # API key from Generated using NewsAPI
    api_key = '26a0b568d79c4c91bef6041be8e0c694'
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    # Make the request to the API
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'ok' and data['totalResults'] > 0:
            articles = data['articles'][:10]  # Get the top 5 articles
            for article in articles:
                print(f"Title: {article['title']}")
                print(f"Description: {article['description']}\n")
        else:
            print("No articles found or invalid response structure")
#news()


def google_search(query):
    url = "https://www.google.com/search"
    params = {"q": query}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/58.0.3029.110 Safari/53‌​7.36".encode(
            'utf-8')}
    response = requests.get(url, params=params, headers=headers)
    return response


def pyquiz():
    print("Let's Play A Python Quiz!!")
    questions = {
        "Is List Mutable?": "True" or "Yes",
        "Who created Python ?": "Guido Van Rossum",
        "What is 2*5**1*2?": "20",
        "Which brackets are used for Tuple?": "()"
    }

    score = 0
    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.strip().lower() == answer.lower():
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {answer}.")
    print(f"Your score is {score}/{len(questions)}.")
#pyquiz()


def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke = response.json()
        return f"{joke['setup']} - {joke['punchline']}"
    else:
        return "Couldn't fetch a joke at the moment."
# print(get_joke())


def translate_text(text, dest_lang):
    translator = Translator(to_lang=dest_lang)
    translation = translator.translate(text)
    return translation
# print(translate_text(message, 'hi'))


def quote():
    quote = pyquotegen.get_quote("inspirational")
#print(quote)
import requests
from playsound import playsound


print("Hey there! I'm Noobie, your virtual companion.")

@eel.expose
def get_response():
    # self.query = takecommand().lower()

    text = input("Message Noobie :")
    if text.lower() == "wikipedia":
        MediaWiki()
    elif text.lower() == "news":
        news()
    elif text.lower() == "quiz":
        pyquiz()
    elif text.lower() == "text to audio":
        speak(text)
    elif text.lower in ["google search" or "google"]:
        query = input("Enter Search Query : ")
        webbrowser.open_new(google_search(query).url)
        google_search(query)
    elif text.lower() in ["open", "app", "open app"]:
        opener()
    elif text.lower() in ["close" or "close app"]:
        closer()
    elif text.lower() == "audio to text":
        audiototext()
    elif text.lower() in ["translate" or "convert"]:
        message = input("Enter Text you want to translate: :")
        print(translate_text(message, 'es'))
    elif text.lower() in ["youtube" or "search youtube" or "youtube search"]:
        search = input("What you want to search? :")
        open_youtube_search(search)
    elif text.lower in ["please play","play","can you play","song please","play some song","could you play some song"]:
        spotify(self)
    elif text in ["temperature", "weather", "climate"]:
        weather()
    else:
        chatBot(text)
while True:
    get_response()

# Choice=int(input("Enter 1 to Continue\nEnter 2 to Exit\nEnter your Choice : "))



