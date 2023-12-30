# Import necessary libraries:
from gtts import gTTS


# Create a function that takes as input the file and converts it to speech:
def text_to_speech_from_file(file_path):
    # Read the text from the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Convert text to speech
    tts = gTTS(text, lang='en')
    tts.save('output.mp3')


# Example
# STEP 1: Indicate the file path
input_file_path = ''

# STEP 2: Convert and save the text to speech
text_to_speech_from_file(input_file_path)
