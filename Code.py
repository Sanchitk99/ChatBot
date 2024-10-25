import time
import pyimagine
import pyaudio

current_time = time.strftime("%H:%M:%S", time.localtime())
print(current_time)


#For Opening Apps
def AppOpen():
    from AppOpener import open
    choice = int(input())
    App = input("Enter App Name to open:")
    try:
        [open(App, match_closest=True)]
    except:
        print("No App with Name", App, "Available")
def AppClose():
    from AppOpener import close  #To Close Any App
    App = input("Enter App Name to close:")
    try:
        [close(App, match_closest=True)]
    except:
        print("No App with Name", App, "Available")


#AppOpen()

# Function to convert text to speech
def speak():
    import pyttsx3
    engine = pyttsx3.init()
    text = input("Enter Your Text to Convert to Audio:")
    engine.setProperty("volume", 0.5)
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()


#speak()

# To Get Weather Forecast
def weather():
    import requests
    from pyowm.owm import OWM

    # Your API key from OpenWeatherMap
    api_key = '87bb4a8443fd0ec621a73e5b390fcbb2'
    city = input("Enter City :")

    # Create the API request URL
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Make the request to the API
    response = requests.get(base_url)

    # Check if the request was successful
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
def wikipedia():
    import webbrowser
    import wikipedia
    wiki = input("What you want to search on Wikipedia? : ")
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


#wikipedia()


def news():
    import requests
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


import requests
import webbrowser


# Function to perform a Google search
def google_search(query):
    url = "https://www.google.com/search"
    params = {"q": query}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/53‌​7.36".encode(
            'utf-8')}
    response = requests.get(url, params=params, headers=headers)
    return response





def pyquiz():
    print("Let's Play A python Quiz!!")
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
def Working():
#
# import speech_recognition
# import pyttsx3
#
# recognizer = speech_recognition.Recognizer()
# while True:
#
#     try:
#         with speech_recognition.Microphone() as mic:
#             recognizer.adjust_for_ambient_noise(mic, duration=0.5)
#             audio = recognizer.listen(mic)
#
#             text = recognizer.recognize_google(audio)
#             text = text.lower().split()
    text=input("Enter Your Choice:")

    if text.lower()== "wikipedia":
        wikipedia()
    elif text.lower()== "news":
        news()
    elif text.lower()== "quiz":
        pyquiz()
    elif text.lower()== "text to audio":
        speak()
    elif text.lower()== "temperature" or "weather":
        weather()
    elif text.lower()== "google search":
        query = input("Enter Search Query : ")
        webbrowser.open_new(google_search(query).url)
        google_search(query)
    elif text.lower()== "open":
        AppOpen()
    elif text.lower()=="Close":
        AppClose()

            # print(f'Father: {text}')

    # except speech_recognition.UnknownValueError:

        # recognizer = speech_recognition.Recognizer()
        # continue
Working()

