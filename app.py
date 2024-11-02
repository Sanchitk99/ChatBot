import Features



def get_response(text):
    if text.lower() == "translate":
        print( "I can translate text for you. Please specify the text.")
        Features.translate_text(text,'hi')
    if text.lower()== "wikipedia":
        Features.MediaWiki()
        return
    elif text.lower()== "news":
        Features.news()
    elif text.lower()== "quiz":
        Features.pyquiz()
    elif text.lower()== "text to audio":
        Features.speak(text)
    elif text.lower()== "google search":
        query = input("Enter Search Query : ")
        Features.webbrowser.open_new(Features.google_search(query).url)
        Features.google_search(query)
    elif text.lower()== "open":
        Features.opener()
    elif text.lower()=="close":
        Features.closer()
    elif text.lower()=="translate":
        message = input("Enter Text you want to translate: :")
        print(Features.translate_text(message, 'hi'))
    elif text.lower() == "temperature" or "weather":
        Features.weather()



