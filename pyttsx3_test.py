# Import necessary libraries:
import pyttsx3


# Create a function that takes as input the file and converts it to speech:
def text_to_speech_from_file(file_path):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Change the voice/language and rate:
    engine.setProperty('rate', 150)
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

    # Read the text from the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()


# Example
# STEP 1: Indicate the file path
input_file_path = 'data/Intro_to_Machine_Learning_Explanation.txt'

# STEP 2: Convert and save the text to speech
text_to_speech_from_file(input_file_path)
