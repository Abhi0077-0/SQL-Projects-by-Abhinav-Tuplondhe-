import speech_recognition as sr

def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        # r.pause_threshold = 5
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration=5)

    try:
        print("Recognizing...")
        query = r.recognize_google_cloud(audio, language= 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query

takeCommand()