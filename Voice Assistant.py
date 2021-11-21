import speech_recognition as sr
import pyttsx3
import pywhatkit

def talking():
    pyttsx3.speak("Hello sir, Jarvis at your service. what can i do for you?")
    
def weather():
 pywhatkit.search("Weather")

def Youtube(cmd):
  pyttsx3.speak("Playing on Youtube")
  pywhatkit.playonyt(cmd)
def Gsearch(cmd):
  pyttsx3.speak("Here is what I found")
  pywhatkit.search(cmd)

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
print("Starting Jarvis..")
talking()
while 1==1:
   print("Listening....")
   try:
                      with sr.Microphone() as src :
                        voice = listener.listen(src)
                        cmd= listener.recognize_google(voice)
                        print(cmd)
                        cmd=cmd.lower()
                       
                        if "weather" in cmd :
                           weather()
                      
                        elif "play" in cmd:
                           Youtube(cmd)
                      
                        elif "information" in cmd:
                            Gsearch(cmd)
                      
                        elif "hello jarvis" in cmd :
                          pyttsx3.speak("Hello Sir")
            
                        elif "goodbye" in cmd:
                          pyttsx3.speak("Goodbye, Sir")
                        elif "stop" in cmd:
                          break
                                                    
   except:
            pyttsx3.speak("Sorry I couldn't hear you. Try saying it again")
            pyttsx3.speak(" You can Try saying, weather today for weather updates or information about for specific information on something")
                        
