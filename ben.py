import subprocess
import os

record = 1
while record < 50:
    i = subprocess.getoutput("termux-speech-to-text")
    record = record + 1 
    print (i)
    if i == 'hello':
        os.system("espeak 'hello sir' -s 100")
    elif i == 'hai':
        os.system("espeak 'ooo you call me' -s 100")
    elif i == 'good morning':
        os.system("espeak 'good moring have a very nice bay' -s 100")
    elif i == 'what is your name':
        os.system("espeak 'i am termux assistant' -s 100")
    elif i == 'name':
        os.system("espeak 'i am just your termux' -s 100")
    elif i == 'open youtube':
        os.system("espeak 'opening youtube' -s 100")
        os.system("termux-open https://m.youtube.com")
    elif i == 'open google':
        os.system("espeak 'opening google' -s 100")
        os.system("termux-open https://www.google.co.in/")
    elif i == 'stop':
        os.system("espeak 'ok sir bye' -s 100")
        break 
os.system("exit")      
