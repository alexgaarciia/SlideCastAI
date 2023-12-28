# Import the necessary library:
import pyttsx3

# Change the voice/language:
engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    print(f"ID: {voice.id}, Name: {voice.name}")

engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')


# Convert text to audio:
engine.say("Hello, this is a text-to-speech test.")
engine.runAndWait()
