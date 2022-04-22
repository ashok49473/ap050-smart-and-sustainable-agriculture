import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)
engine.say("Hi vaasu, tinnavaa. em chestunnav?")

engine.runAndWait()