import streamlit as st
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import pyperclip

def record_audio(filename, duration, fs):
    # Record audio
    st.write("Recording audio...")
    my_recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait()
    # Save audio to file
    sf.write(filename, my_recording, fs)

def transcribe_audio(filename):
    # Transcribe audio to text
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
    return text

def main():
    st.title("Audio Recorder and Transcriber")
    
    duration = st.slider("Recording Duration (seconds):", min_value=1, max_value=10, value=5)
    
    if st.button("Start Recording"):
        filename = "recorded_audio.wav"
        fs = 44100
        record_audio(filename, duration, fs)
        st.write("Recording complete.")
        st.audio(filename, format='audio/wav')
        
        st.write("Transcribing audio...")
        text = transcribe_audio(filename)
        st.write("Transcription:")
        st.write(text)
        
        if st.button("Copy Text to Clipboard"):
            pyperclip.copy(text)
            st.write("Text copied to clipboard!")
    
if __name__ == "__main__":
    main()
