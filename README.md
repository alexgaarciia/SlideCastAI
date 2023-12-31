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
In order to carry out this project, we used two libraries (`gTTS`, `pyttsx3`):
- `gTTS`: It is a Python library that interfaces with Google Translate's text-to-speech API. It's a simple and easy-to-use tool that converts text into spoken words.
- `pyttsx3`: This is a text-to-speech conversion library in Python that works offline. It interacts with native speech engines on different operating systems.

Furthermore, we will also take advantage of the free trials of certain TTS products:
<div align="center">
    <table>
        <tr>
            <td align="center">Amazon Polly</td>
            <td align="center">LovoAI</td>
            <td align="center">Speechify</td>
            <td align="center">Murf</td>
            <td align="center">ElevenLabs</td>
            <td align="center">PlayHT</td>
        </tr>
        <tr>
            <td><a href="https://aws.amazon.com/polly/?nc1=h_ls"><img src="https://github.com/alexgaarciia/SlideCastAI/blob/main/images/logos/amazon_polly.png" width="100px"/></a></td>
            <td><a href="https://lovo.ai/"><img src="https://github.com/alexgaarciia/SlideCastAI/blob/main/images/logos/lovo_ai.jpg" width="100px"/></a></td>
            <td><a href="https://speechify.com/?source=fb-for-mobile&landing_url=https%3A%2F%2Fspeechify.com%2Ftext-to-speech-online%2F&gclid=Cj0KCQiA1rSsBhDHARIsANB4EJYVsoTZmEBFRouCp0CGRgPRlZgA_gvhabvCXzV0afzWh7yU_6pe5LgaAryrEALw_wcB&via=uniteai"><img src="https://github.com/alexgaarciia/SlideCastAI/blob/main/images/logos/speechify.png" width="100px"/></a></td>
            <td><a href="https://murf.ai/?pscd=get.murf.ai&ps_partner_key=ZjZvZXlx&ps_xid=eQon6QSl3GhGZR&gsxid=eQon6QSl3GhGZR&gspk=ZjZvZXlx&gclid=Cj0KCQiAv8SsBhC7ARIsALIkVT1JPXIksu6GGM5st_3JbDllOiEmOoKruqvfiIoQCxeby-yFQ7YGh2waArflEALw_wcB"><img src="https://github.com/alexgaarciia/SlideCastAI/blob/main/images/logos/murf_ai.png" width="100px"/></a></td>
            <td><a href="https://elevenlabs.io/?pscd=try.elevenlabs.io&ps_partner_key=YW50b2luZXRhcmRpZjU2NTA&ps_xid=lHCeM4tyg4TpQw&gsxid=lHCeM4tyg4TpQw&gspk=YW50b2luZXRhcmRpZjU2NTA"><img src="https://github.com/alexgaarciia/SlideCastAI/blob/main/images/logos/eleven_labs.png" width="100px"/></a></td>
            <td><a href="https://play.ht/?via=uniteai"><img src="https://github.com/alexgaarciia/SlideCastAI/blob/main/images/logos/play_ht.png" width="100px"/></a></td>
        </tr>
    </table>
</div>


## Process
In order to carry out this project, we may follow these steps:
1. Choose a lecture/slide that we may want to turn into a podcast.
2. Pass it to ChatGPT to obtain explanations.
3. Pass the explanations to multiple Text-To-Speech (TTS) systems.
4. Compare results.

However, we may also want to test how specific we must be in order to reach an "ideal" explanation. To do so, several prompts will be tested out, each being more specific than the previous one.

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
1. Give ChatGPT a prompt:
<p align = "center">
   <img src="https://github.com/alexgaarciia/SlideCastAI/blob/main/images/instructions/initial_instructions.png" width = 600>
</p>

2. Upload a desired document:
<p align = "center">
   <img src="https://github.com/alexgaarciia/SlideCastAI/blob/main/images/instructions/uploading_doc.png" width = 600>
</p>

After uploading a lecture, we would normally expect ChatGPT to give us a link to a **txt file**. These files can be found in the folder [data](https://github.com/alexgaarciia/SlideCastAI/tree/main/data).

3. After finishing with all of the files on which we wanted to try a certain prompt, we would normally indicate ChatGPT that new instructions will be given:
<p align = "center">
   <img src="https://github.com/alexgaarciia/SlideCastAI/blob/main/images/instructions/new_instructions.png" width = 600>
</p>

Afterwards, we would test these file on the TTS systems that we talked about above. Nonetheless, before that, it would be interesting to compare all of the prompts that we tried, all the way from `Prompt #1` to `Prompt #4`. 

#### Prompt comparison
Let's start with [**Prompt #1**](https://github.com/alexgaarciia/SlideCastAI/tree/main/data/Prompt%20%231), where we provided ChatGPT several things. First off, we specified that some instructios must be followed strictly and that we want as an output a txt file that explains some slides. Then, four general instructions were provided: `DO NOT USE POINTS` (with this we are trying to make the explanations more real), `Explain very easily each of the slides` (this instruction could make the podcast to not feel very heavy; this may be useful with advanced topics), `Give examples to explain everything` (following the structure of a regular class, examples are provided to make students undertand concepts better), and `Make it dynamic`.

The difference with [**Prompt #2**](https://github.com/alexgaarciia/SlideCastAI/tree/main/data/Prompt%20%232) is not huge, since the structure of the prompt changed a little bit and a new instuction was included: `DO NOT SUMMARIZE`. With this, we wanted ChatGPT to not skip slides, since some high-yield information may be lost; we are ensuring that each of the slides (relevant or irrelevant) are checked.

Moving on with [**Prompt #3**](https://github.com/alexgaarciia/SlideCastAI/tree/main/data/Prompt%20%233), we tried to make texts more "human-like" with a new instruction: `Do not include titles to introduce topics. Say things a person would say when introducing parts of a presentation (Okay, so now I am going to talk about..., We will continue with...)`.

Finally, [**Prompt #4**](https://github.com/alexgaarciia/SlideCastAI/tree/main/data/Prompt%20%234) intended to make lectures more dynamic stating real-world applications of the concepts we are trying to explain. With this we are showing students that we study these concepts for a reason.

If we were to check the generated files, we could see that being more specific from prompt to prompt worked. Let's take a look at the table from below:

Prompt #1      |  Prompt #2      | Prompt #3       | Prompt #4
:---------------:|:---------------:|:---------------:|:---------------:
Summarized version of the lecture (does not go into too much technical depth). Explains well the basics and provides some examples.  | Contains more concepts from the slides (suitable for deeper understanding of the filed).  | More human-like instructions (feels closer to real lectures) | Adds a focus on practical applications 

#### Comparison of TTS libraries/platforms
|    Model   | Voice Quality | Language and Accent Support | Customization | Comments|
|:-------:|:-------:|:-------:|:-------:|:-------:|
| gTTS |    Robotic    |    50+ languages and multiple accents    |    Slow/Fast    |    Easy to implement but robotic voice    |
| pyttsx3  |    Robotic    |    French, Spanish (Spain), English (US), Korean    |    Speed    |    Easy to implement but robotic voice    |
| Amazon Polly |    Robotic    |    30+ languages    |    Voice, pronunciation    |    In the free version we can only try a maximum of 3000 characters per project; the voice does not sound real; allows to download generated audio    | 
| LovoAI  |    Human-like    |    Over 100 different languages and accents    |   Voice    |    The free trial only has 20 minutes of audio generation; the voice feels real    |
| Speechify |    Human-like    |    30+ languages    |    Voice, Speed    |    The free trial allows to convert only 5 documents to audio; the voice feels real    |
| Murf  |    Human-like    |    20 languages    |    Voice, Emotion, Pitch, Speed    |    Only 10 minutes of voice generation    |
| ElevenLabs |    Human-like    |    30 languages    |    Voice, Stability, Clarity + Similarity Enhancement, Style Exaggeration    |    You can only use 10,000 characters with the free version and you can only convert to audio documents with a maximum of 2500 characters; takes too long to process but the voice is realistic     |  
| PlayHT  |    Human-like    |    60+    |    Speed    |    You can use 12,500 characters (used as desired); it is fast and allows to download files    | 
