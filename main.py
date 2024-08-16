import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        try:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio)
            response_label.config(text=f"You said: {user_input}")
            speak_text(f"You said {user_input}")
        except sr.UnknownValueError:
            response_label.config(text="Sorry, I didn't catch that.")
            speak_text("Sorry, I didn't catch that.")
        except sr.RequestError:
            response_label.config(text="Network error.")
            speak_text("Network error.")


root = tk.Tk()
root.title("Voice Assistant")
root.geometry("400x400")
root.configure(bg="#F0F8FF")

mic_image = Image.open("assets/mic_icon.png")
mic_image = mic_image.resize((100, 100), Image.Resampling.LANCZOS)

mic_photo = ImageTk.PhotoImage(mic_image)

mic_button = Button(root, image=mic_photo, command=listen, borderwidth=0, bg="#F0F8FF")
mic_button.pack(pady=50)

response_label = Label(root, text="Click the mic to speak", font=("Helvetica", 16), bg="#F0F8FF")
response_label.pack(pady=20)

root.mainloop()
