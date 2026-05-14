print("program strated")
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()


# Function to make assistant speak
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# Function to listen to user voice
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        # Reduce background noise
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source, timeout=5)

            # Convert speech to text
            command = recognizer.recognize_google(audio)

            print("You said:", command)

            return command.lower()

        except sr.WaitTimeoutError:
            print("Listening timed out")
            return ""

        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""

        except sr.RequestError:
            print("Internet error")
            return ""

        except Exception as e:
            print("Error:", e)
            return ""


# Main function
def main():

    speak("Hello, I am your voice assistant")

    while True:

        command = listen()

        # Skip empty commands
        if command == "":
            continue

        elif "hello" in command:
            speak("Hello, how are you?")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        elif "date" in command:
            today = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {today}")

        elif "search" in command:

            speak("What should I search?")

            search_query = listen()

            if search_query != "":
                url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(url)

                speak(f"Searching for {search_query}")

        elif "exit" in command or "stop" in command:
            speak("Goodbye")
            break

        else:
            speak("Sorry, I did not understand")


# Run program
if __name__ == "__main__":
    main()