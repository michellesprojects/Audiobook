#GUI to prompt for file 

from tkinter import Tk 
from tkinter.filedialog import askopenfile

Tk().withdraw()


fileobj = askopenfile()

#convert this file to text, then save as mp3 

booktext = fileobj.read()

from gtts import gTTS 

audiobook = gTTS(booktext, lang='en')


from pathlib import Path 

title = Path(fileobj.name).stem
audiobook.save(title+'.mp3')