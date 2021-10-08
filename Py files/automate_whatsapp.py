import pywhatkit as kt
import getpass as gp
import datetime
from virtual import *
import datetime as dt

hr=dt.datetime.now().hour
min=dt.datetime.now().minute

def automateWhatsapp():
    print("Enter the phone number with the country code")
    speak("Enter the phone number with the country code")
    p_num=gp.getpass(prompt="Phone number: ", stream=None)
    print("Please speak your message")
    speak("Please speak your message")
    msg=takeCommand()
    print("I will send the message")
    speak("I will send the message")
    kt.sendwhatmsg(p_num,msg,hr,min+1)
#automateWhatsapp()
