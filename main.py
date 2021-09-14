# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = "Thanks for appreciation! You may call it tabiyat main rawani. No, I have not published any book, yet. One of my internet friend, who lives in Bombay asked me to give him my poetry for Rekhta. And he got published my poetry at Rekhta. No doubt, Rekhta is a big platform with vast audience and multi-script support."
# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False,)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome2.mp3")

# Playing the converted file
os.system("mpg321 welcome.mp3")
