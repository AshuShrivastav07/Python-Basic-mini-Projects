# Modules
import androidhelper as ah
import datetime as dt

#import weather_forecast as wf
# Code

print("    Clock ")

droid = ah.Android()


#gretting with time

import time

talk = droid.recognizeSpeech("Talk Now",None,None)

currentTime = int(time.strftime('%H'))
time= time.strftime("%I:%M:%S:%p")

if talk[1]=="what is the time":
    print("Time is ",time)
    if currentTime < 12 :
        droid.ttsSpeak("Good Morning Sir, time is "+ str(time))
    elif currentTime > 12 :
        droid.ttsSpeak('Good afternoon Sir time is'+ str(time))
    elif currentTime > 6 :
        droid.ttsSpeak('Good evening Sir time is'+ str(time))
#print("You said: " + speech[1])

