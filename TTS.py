from gtts import gTTS
from tempfile import TemporaryFile
import os
import vlc

tts = gTTS(text='Good morning', lang='ja')
tts.save("good.mp3")



player = vlc.MediaPlayer("good.mp3")
player.play()

exit_now = raw_input("Do you like to exit now (Y)es (N)o  ? ")











