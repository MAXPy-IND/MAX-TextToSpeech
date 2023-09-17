import speech_recognition as sr
from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text=text, lang="en")
    tts.save(filename)
    os.system(f"mpg321 {filename}")  # You can use other audio players if needed

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=5)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand what you said."
    except sr.RequestError:
        return "Sorry, I am having trouble accessing the Google API."

def chat():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        
        # Text-to-speech
        text_to_speech(user_input, "user_input.mp3")
        
        print("Bot: Processing...")
        
        # Speech-to-text
        bot_response = speech_to_text()
        
        # Display bot's response
        print(f"Bot: {bot_response}")
        
        # Text-to-speech
        text_to_speech(bot_response, "bot_response.mp3")

if __name__ == "__main__":
    print("Text-to-Speech Chat Bot /nMade By : max.py")
    print("Type 'exit' to quit.")
    chat()
