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
import json
from hugchat.hugchat import ChatBot
from oauthlib.uri_validate import query
from translate import Translator
import speech_recognition
import urllib.parse
from pydub import AudioSegment
from pydub.playback import play
import time
from datetime import datetime
from playsound import playsound
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from colored import attr
reset = attr('reset')


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
#playAssistantSound()

def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine/cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print("Bot: "+response)
    # speak(response)
    return response


def open_youtube_search(query):
    base_url = "https://www.youtube.com/results?search_query="
    search_url = base_url + urllib.parse.quote(query)
    webbrowser.open(search_url)
# search = input("What you want to search?")
#open_youtube_search(search)


def audiototext():
    recognizer = speech_recognition.Recognizer()
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.5)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                print(f'Bot: {text}')
                if text.lower()=="exit":
                    break
                #get_response(text)
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            continue
#audiototext()


def opener():
    from AppOpener import open
    app = input("Bot: Enter App Name to open:- ")
    try:
        [open(app, match_closest=True)]
    except FileNotFoundError:
        print("No App with Name", app)
#opener()


def closer():
    from AppOpener import close  #To Close Any App
    app = input("Bot: Enter App Name to close:- ")
    try:
        [close(app, match_closest=True)]
    except FileNotFoundError:
        print("Bot:No App with Name", app)
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


def spotifyW():
    client_id = 'd7fd6fca60d54a86b156a58ed3be0ec0'
    client_secret = 'b3a5bac8aa644bb0bf63dea51c07b305'
    redirect_uri = 'http://localhost:8888/callback'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=redirect_uri,
                                                   scope='user-read-private user-read-email'))
    Song=input("Bot: Enter Song Name:- ").lower()
    def play_song(song_name):
        results = sp.search(q=song_name, type='track', limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            track_url = track['external_urls']['spotify']
            speak('Playing' + Song)
            webbrowser.open(track_url)
            print(f"Opening '{track['name']}' by {track['artists'][0]['name']}' in your web browser.")
        else:
            print(f"Bot: No results found for '{song_name}'")
    play_song(Song)
# spotifyW()

def weather():
    api_key = '87bb4a8443fd0ec621a73e5b390fcbb2'
    city = input("Bot: Enter City :- ")
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


def mediawiki():
    wiki = input("Bot: What you want to search on Wikipedia? : ")
    wikipedia.set_lang('en')
    try:
        search_results = wikipedia.search(wiki)
        print(search_results)
        page = wikipedia.page(wiki)
        print(wikipedia.summary(wiki, sentences=2))
        url = page.url
        webbrowser.open_new(url)
    except wikipedia.exceptions.PageError:
        print("Could not find that page")
    # print(page.content)
    # print(page.title)
# MediaWiki()


def news():
    api_key = '26a0b568d79c4c91bef6041be8e0c694'
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'ok' and data['totalResults'] > 0:
            articles = data['articles'][:5]
            for article in articles:
                print(f"Title: {article['title']}")
                print(f"Description: {article['description']}\n")
        else:
            print("Bot: No articles found or invalid response structure")
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
    print("Bot: Let's Play A Python Quiz!!")
    questions = {
        "Bot: Is List Mutable?": "True" or "Yes" or "yes",
        "Bot: Who created Python ?": "Guido Van Rossum",
        "Bot: What is 2*5**1*2?": 20,
        "Bot: Which brackets are used for Tuple?": "()"
    }
    score = 0
    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.strip().lower() == answer.lower():
            score += 1
            print("Bot: Correct!")
        else:
            print(f"Bot: Wrong! The correct answer is {answer}.")
    print(f"Bot: Your score is {score}/{len(questions)}.")
#pyquiz()


def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke = response.json()
        return f"Bot: {joke['setup']} - {joke['punchline']}"
    else:
        return "Bot: Couldn't fetch a joke at the moment."
#print(get_joke())


def translate_text(text, dest_lang):
    translator = Translator(to_lang=dest_lang)
    translation = translator.translate(text)
    return "Bot: " +translation
#print(translate_text(message, 'hi'))


def quote():
    quote = pyquotegen.get_quote("inspirational")
    print("Bot: "+quote)
# quote()


from colored import fg, attr

from colored import fg, attr

from colored import fg, attr

def Contents():
    # Example of color-coded outputs
    print(f"{fg('green')}Welcome to MultiTasking Chat Bot!!! I Can Tell and Do Anything....{attr('reset')}")
    print(f"{fg('green')}1. Wikipedia{attr('reset')}")
    print(f"{fg('green')}2. News{attr('reset')}")
    print(f"{fg('green')}3. Quiz{attr('reset')}")
    print(f"{fg('green')}4. Joke{attr('reset')}")
    print(f"{fg('green')}5. Text to audio{attr('reset')}")
    print(f"{fg('green')}6. Quote{attr('reset')}")
    print(f"{fg('green')}7. Google Search{attr('reset')}")
    print(f"{fg('green')}8. Open App{attr('reset')}")
    print(f"{fg('green')}9. Close App{attr('reset')}")
    print(f"{fg('green')}10. Audio to Text{attr('reset')}")
    print(f"{fg('green')}11. Music{attr('reset')}")
    print(f"{fg('green')}12. Translate{attr('reset')}")
    print(f"{fg('green')}13. YouTube Search{attr('reset')}")
    print(f"{fg('green')}14. Weather{attr('reset')}")
    print(f"{fg('green')}15. Type Anything Else{attr('reset')}")
def Time():
    print(
        f"Current Time: {datetime.now().strftime('%H:%M:%S')}, Date: {datetime.now().strftime('%Y-%m-%d')}, Day: {datetime.now().strftime('%A')}")


Time()
Contents()
def get_response():
    playAssistantSound()
    blue = fg('blue')
    Input = input(f"{blue}You: {reset}")
    text=Input.strip()
    if text.lower() in ["wikipedia","1"]:
        mediawiki()
    elif text.lower() in ["news","2"]:
        news()
    elif text.lower() in ["quiz","3"]:
        pyquiz()
    elif text.lower() in  ["4","joke", "tell me a joke" , "tell a joke","make me laugh",4]:
        print(get_joke())
    elif text.lower() in ["5","text to audio"]:
        Para=input("Bot: Write your text to convert in audio: ")
        speak(Para)
    elif text.lower() in ["6","quote"]:
        quote()
    elif text.lower() in ["7","google", "google search"]:
        query = input("Bot: Enter Search Query : ")
        webbrowser.open_new(google_search(query).url)
        google_search(query)
    elif text.lower() in ["8","open", "app", "open app"]:
        opener()
    elif text.lower() in ["9","close" , "close app"]:
        closer()
    elif text.lower() in ["10","audio to text"]:
        audiototext()
    elif text.lower() in ["11","play song" ,"could you play some song" ,"play music" ,"can you play" , "song please","spotipy"]:
        spotifyW()
    elif text.lower() in ["12","translate" or "convert"]:
        message = input("Enter Text you want to translate: :")
        print(translate_text(message, 'hi'))
    elif text.lower() in ["13","youtube" or "search youtube" or "youtube search"]:
        search = input("Bot: What you want to search? :")
        open_youtube_search(search)
    elif text.lower() in ["14","temperature", "weather", "climate"]:
        weather()
    elif text.lower() in ['content']:
        Contents()
    elif text.lower() in ["0","quit"]:
        quit()
    else:
        chatBot(text)


while True:
    get_response()


