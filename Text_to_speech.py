import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    print("Robo Speaker activated. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            speak("Goodbye!")
            break
        else:
            speak(user_input)

if __name__ == "__main__":
    main()


   
    