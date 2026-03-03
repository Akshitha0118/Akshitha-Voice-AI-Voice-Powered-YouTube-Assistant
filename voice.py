import streamlit as st
import speech_recognition as sr
import pywhatkit as pk
from gtts import gTTS

recognizer = sr.Recognizer()

def speak(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    st.audio("response.mp3")

def hear():
    cmd = ""
    try:
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = recognizer.listen(source)
            cmd = recognizer.recognize_google(audio)
            cmd = cmd.lower()
    except Exception as e:
        st.error(f"Error: {e}")
    return cmd

st.title("🎤 Akshitha Voice Bot")

if st.button("Start Listening"):
    command = hear()
    st.write("You said:", command)

    if "play" in command:
        song = command.replace("play", "")
        response = "Playing " + song
        st.success(response)
        speak(response)
        pk.playonyt(song)