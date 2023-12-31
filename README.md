# SlideCastAI
The main goal of this repository is to learn about current AIs that can turn text into audio. On top of that, we will carry out experiments that will involve explaining the content of slides and, furthermore, turn it into a dynamic podcast.


## Text-To-Speech systems
### Background
Text-to-Speech systems are designed to read written text aloud, using synthesized speech that sounds as natural as possible. TTS technology has evolved significantly, with modern systems using advanced machine learning techniques, often based on neural networks, to produce highly natural and human-like speech in various languages and accents.

These kind of systems work in the following way:
1. `Text Analysis`: The first step consists on examining the text to determine the structure and meaning of words, taking into account things along the lines of sentence structure, syntax, and punctuation.
2. `Language Processing`: Subsequently, the software utilizes linguistic algorithms to find the correct pronunciation and intonation for each word.
3. `Voice Generation`: The software creates the voice waveform.
4. `Audio Rendering`: Finally, the so-called waveform is turned into an audio file.

### Used Text-To-Speech systems
#### Free systems
In order to carry out this project, we used two libraries (`gTTS`, `pyttsx3`):
- `gTTS`: It is a Python library that interfaces with Google Translate's text-to-speech API. It's a simple and easy-to-use tool that converts text into spoken words.
- `pyttsx3`: This is a text-to-speech conversion library in Python that works offline. It interacts with native speech engines on different operating systems.

#### Payment systems
Furthermore, we will also take advantage of the free trials of certain TTS products: [Amazon Polly](https://aws.amazon.com/polly/?nc1=h_ls), [Lovo AI](https://lovo.ai/), [Speechify](https://speechify.com/?source=fb-for-mobile&landing_url=https%3A%2F%2Fspeechify.com%2Ftext-to-speech-online%2F&gclid=Cj0KCQiA1rSsBhDHARIsANB4EJYVsoTZmEBFRouCp0CGRgPRlZgA_gvhabvCXzV0afzWh7yU_6pe5LgaAryrEALw_wcB&via=uniteai), [Murf](https://murf.ai/?pscd=get.murf.ai&ps_partner_key=ZjZvZXlx&ps_xid=eQon6QSl3GhGZR&gsxid=eQon6QSl3GhGZR&gspk=ZjZvZXlx&gclid=Cj0KCQiAv8SsBhC7ARIsALIkVT1JPXIksu6GGM5st_3JbDllOiEmOoKruqvfiIoQCxeby-yFQ7YGh2waArflEALw_wcB), [ElevenLabs](https://elevenlabs.io/?pscd=try.elevenlabs.io&ps_partner_key=YW50b2luZXRhcmRpZjU2NTA&ps_xid=lHCeM4tyg4TpQw&gsxid=lHCeM4tyg4TpQw&gspk=YW50b2luZXRhcmRpZjU2NTA), and [PlayHT](https://play.ht/?via=uniteai). 


## Process
In order to carry out this project, we may follow these steps:
1. Choose a lecture/slide that we may want to turn into a podcast.
2. Pass it to ChatGPT to obtain explanations.
3. Pass the explanations to multiple Text-To-Speech (TTS) systems.
4. Compare results.

However, we may also want to test how specific we must be in order to reach an "ideal" explanation. To do so, several promtps will be tested out, each being more specific than the previous one.

### Prompts 
- Prompt #1:
```ruby
I need you to inspect the file that I submit you. I am going to give you some instructions that I want you to follow strictly.
The main goal is to generate a txt file explaining in a dynamic way the slides/lectures I give you.

Instructions: Generate a text that explains the topic. Make sure you:
1. DO NOT USE POINTS. Use paragraphs talking as if you were a professor. 
2. Explain very easily each of the slides.
3. Give examples to explain everything.
4. Make it dynamic.
```

- Prompt #2:
```ruby
I need you to inspect the file that I submit you. I am going to give you some instructions that I want you to follow strictly. 

Goal: The main goal is to generate a txt file explaining in a dynamic way the slides/lectures I give you.

Instructions:
1. DO NOT USE POINTS. Use paragraphs talking as if you were a professor. 
2. DO NOT SUMMARIZE. Explain all of the slides.
3. Explain each of the slides with examples.
4. Make it dynamic.
```

- Prompt #3:
```ruby
I need you to inspect the file that I submit you. I am going to give you some instructions that I want you to follow strictly. 

Goal: The main goal is to generate a txt file explaining in a dynamic way the slides/lectures I give you.

Instructions:
1. DO NOT USE POINTS. Use paragraphs talking as if you were a professor. 
2. DO NOT SUMMARIZE. Explain all of the slides.
3. Do not include titles to introduce topics. Say things a person would say when introducing parts of a presentation (Okay, so now I am going to talk about..., We will continue with...).
4. Explain each of the slides with examples.
5. Make it dynamic.
```

- Prompt #4:
```ruby
I need you to inspect the file that I submit you. I am going to give you some instructions that I want you to follow strictly. 

Goal: The main goal is to generate a txt file explaining in a dynamic way the slides/lectures I give you.

Instructions:
1. DO NOT USE POINTS. Use paragraphs talking as if you were a professor. 
2. DO NOT SUMMARIZE. Explain all of the slides.
3. Do not include titles to introduce topics. Say things a person would say when introducing parts of a presentation (Okay, so now I am going to talk about..., We will continue with...).
4. Explain each of the slides with examples.
5. Make it dynamic.
6. Include real-world applications to prove the usefulness of what you are explaining.
```

### Results
Once we chose the lectures we wanted to turn into podcasts, we performed the following steps:
1. Give ChatGPT a prompt and upload such documents.











