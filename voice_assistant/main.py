import webbrowser
import datetime
import pyjokes
import speech_recognition as sr
import pyttsx3

# Function to convert speech to text
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("--- Listening ---")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print("You said:", data)
            return data
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return ""
        except sr.RequestError:
            print("Could not request results.")
            return ""

# Function to convert text to speech
def speechtx(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change to voices[1].id for female
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

# Main logic
if __name__ == '__main__':
    speechtx("Hello! How can I help you?")

    while True:
        data1 = sptext().lower()

        if "your name" in data1:
            speechtx("My name is Peter")

        elif "old are you" in data1:
            speechtx("I am 2 years old")

        elif "time" in data1:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speechtx(f"The current time is {current_time}")

        elif "youtube" in data1:
            speechtx("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "joke" in data1:
            joke_1 = pyjokes.get_joke(language="en", category="neutral")
            print(joke_1)
            speechtx(joke_1)

        elif "exit" in data1 or "quit" in data1:
            speechtx("Thank you! Have a nice day.")
            break

        else:
            speechtx("Sorry, I didn't understand that.")
