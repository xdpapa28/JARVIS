import subprocess
import os
import time
from datetime import datetime
import sys
now = datetime.now()
t=now.strftime('%I:%M:%p')
print(t)

inp = subprocess.getoutput("termux-speech-to-text")
time.sleep(1)
print("\033[95m You said: ",str(inp))

def system():
     if inp == "":
         subprocess.call(["termux-tts-speak","please tell something sir"])

     elif "hello" in inp:
         subprocess.call(["termux-tts-speak","hallow sir "])
     elif "pagal really i love you" in inp:
         subprocess.call(["termux-tts-speak","ummm love you tooo sir. I never break your heart.I always under your permission "])
     elif "I love you" in inp:
         subprocess.call(["termux-tts-speak","it's a computer virus and it's disturb half world. "])
     elif "who am i" in inp:
         subprocess.call(["termux-tts-speak","You are my master. Your Name Ankit Yadav.You are too smart.I too impressed that my name Jarvis. Love you sir "])
       elif "lock screen" in inp:
        os.system("termux-screen off")          
       elif "flight mode on" in inp:
        os.system("termux-flight mode on")              
       elif "Chrome on" in inp:
        os.system("termux-chrome on")                  
      elif "wi-fi" in inp:
        os.system("termux-wi-fi on")                       
      elif "data off" in inp:
        os.system("termux-data off")                           
      elif "data on" in inp:
        os.system("termux-data on")                               
     elif "telegram" in inp:
        os.system("termux-open https://telegram/")                                    
     elif "Abb kaam per lago" in inp:
        subprocess.call(["termux-tts-speak","I am ready sir kis project per kaam karna hai "])                                            
     elif "close" in inp:
         subprocess.call(["termux-tts-speak","ok sir wait a second"])
         time.sleep(1)
         sys.exit()
     elif "how are you" in inp:
        subprocess.call(["termux-tts-speak","i am good sir nd you "])
     elif "battery" in inp:
         subprocess.call(["termux-battery-status"])
         
     elif "sleep" in inp:
         subprocess.call(["termux-tts-speak","ok sir i am going to sleep for 5 second"])
         time.sleep(5)
         
     elif "call me" in inp:
         os.system("termux-telephony-call +91")
     elif "torch on" in inp:
         os.system("termux-torch on")
     elif "torch off" in inp:
         os.system("termux-torch off")
         
     elif "YouTube" in inp:
         os.system("termux-open https://m.youtube.com")
     elif "Google" in inp:
         os.system("termux-open https://www.google.co.in/")    
         
     elif "contact" in inp:
         os.system("termux-contact-list")
         
     elif "who are you" in inp:
         subprocess.call(["termux-tts-speak","I am your virtual assistanct, My name is Jarvis sir"])
     elif "Jarvis" in inp:
         subprocess.call(["termux-tts-speak","hallow sir "])
     elif "time" in inp:
         subprocess.call(["termux-tts-speak",t])
         
     elif "what are you doing" in inp:
        subprocess.call(["termux-tts-speak","i am busy with you "])
        
     elif "are you busy" in inp:
         subprocess.call(["termux-tts-speak","i am always free for you"])
     
     elif "name" in inp:
         subprocess.call(["termux-tts-speak","you can call me Jarvis "])
     
     
     elif "who made you" in inp:
         subprocess.call(["termux-tts-speak","I made by Ankit sir"])
     elif "video" in inp:
         os.system("termux-open https://www.google.com/search?q=video")
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     else:
       subprocess.call(["termux-tts-speak","I am not cooded for that"])

system()

os.system("python main.py")