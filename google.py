from gtts import gTTS


def text_to_speech_from_file(file_path, output_filename):
    # Read the text from the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Convert text to speech
    tts = gTTS(text, lang='en')
    tts.save(output_filename)
    print(f"Saved as {output_filename}")


# File paths
input_file_path = 'data/Exploratory_Data_Analysis_Guide_for_Beginners.txt'  # Replace with your file path
output_filename = 'output.mp3'

# Convert and save the text to speech
text_to_speech_from_file(input_file_path, output_filename)
