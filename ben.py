import os
os.system ("espeak 'Hello ,sir'")
who = input ()                                                                                                        if who == 'who are you':
    os.system ("espeak 'I am Ben'")
    os.system ("espeak 'How can help you'")


continues = input ("open google to press -g / play song to perss -p " )


if continues == 'g':
    os.system ("espeak ' opening google'")
    os.system ("w3m 'google.com'")

if continues == 'p':
    os.system ("espeak 'opening  playing  list'")
    os.system ("espeak 'choose a song' ")
    print ("Bad liar -b")
    print ("Fly -f")
    print ("Desi_kalakaar -d")
    print ("Psycho -p")


play = input ()
if play == 'b':
    os.system ("play 'Bad_Liar.mp3'")
if play == 'f':
    os.system ("play 'Fly.mp3'")
if play == 'd':
    os.system ("play 'Desi_Kalakaar.mp3'")
if play == 'p':
    os.system ("play 'Psycho.mp3'")



else :
    os.system ("espeak 'Thank you'")
    os.system ("cmatrix")
    os.system ("exit")
    os.system ("logout")
