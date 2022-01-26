import pyttsx3      #for audio output
import speech_recognition as sr     #for audio input
import cv2      #for taking pictures with camera
from cv2 import *
import datetime     #for date and time

"""
NAME: Name of the voice assistant
VERSION: Version of voice assistant
ADMIN: Name of administrator
CITY: Name of user's city
COUNTRY: Name of your country
"""
NAME = "April"
VERSION = "1.1.0"
ADMIN = "Siddharth Padhy"
CITY = ""   #Name of City here.
COUNTRY = "India"


"""
BOOKMARK: Bookmarks Dictionary for the google search
    Keys: name with which admin calls the website
    Values: URL to the website
"""
BOOKMARKS = {
    "geeksforgeeks" : "https://www.geeksforgeeks.org/",
    "github" : "https://github.com/",
    "youtube" : "https://www.youtube.com/"
}


"""
Commands List: categorizing the commands
"""
INTRODUCTION = ["introduce","introduction"]
WRITE_TODO = ["write todo","write to do","right todo","right to do"]
READ_TODO = ["read todo","read to do","read my todo","read my to do"]
CAMERA = ["camera","picture","photo"]
DATE = ["date","day"]
GOOGLE = ["Google","google"]
WEATHER = ["weather"]
NEWS = ["news","headlines"]
CRYPTO = ["crypto","currency"]
JOKE = ["joke"]
INSPIRE = ["inspire"]
DICTIONARY = ["dictionary","word","meaning"]
SLEEP = ["sleep","wait","rest"]
EXIT = ["exit","quit","turn off"]

"""
List of features of the voice assistant
"""
FEATURES = [
    "Give an introduction. Command is introduce",
    "Add to todo list. Command is write todo",
    "Read todo list. Command is read todo",
    "Take a picture. Command is camera",
    "Tell today's date. Command is date",
    "Make a google search. Command is google",
    "Tell today's weather. Command is weather",
    "Tell today's news headlines. Command is news",
    "Tell today's crypto currency prices. Command is crypto",
    "Tell a joke. Command is joke",
    "Tell an inspirational quote. Command is inspire",
    "Search the meaning of a word in the dictionary. Command is dictionary",
    "You can make me wait using the command sleep and wake me up by speaking my name",
    "You can turn me off using the command exit"
]

class config:
    def listen():
        # Listen for a voice input, returns the string said.
        sample_rate = 48000     #Sample rate is how often values are recorded
        chunk_size = 2048       #Chunk is like a buffer. It stores 2048 samples(bytes of data) here.

        r= sr.Recognizer()
        with sr.Microphone(sample_rate = sample_rate, chunk_size=chunk_size ) as source:
            try:
                audio = r.listen(source)
                MyText = r.recognize_google(audio)
                return(MyText)

            except Exception as e:
                return


    """
    Function to speak the text provided.
    * For Male voice use voices[0] in setProperty function
    * For Female voice use voices[0] in setProperty function
    """
    def speak(text):
        engine = pyttsx3.init('sapi5')
        
        engine.setProperty('rate', 150)     # setting up new voice rate

        voices = engine.getProperty('voices')       # getting voices property
        engine.setProperty('voice', voices[1].id)   # setting another voice property
        engine.say(text)
        engine.runAndWait()


    """
    Function to introduce the voice assistant along with the commands
    """
    def introduce():
        heading = "Introduction"
        text = "I am "+ NAME + ", version " + VERSION + ", serving " + ADMIN + ". "
        text += "The following are my features along with their commands. You can check the commands in the config.py file."

        response = [text]

        for feature in FEATURES:
            response.append(feature)
        response.append("So, that's all. Now lets get started.")

        return (heading, response)


    """
    Function to take a picture from the web cam. If more cameras are present select the camera and enter the cam_port accordingly.
    """
    def pic_cam():
        config.speak("Say Cheese!")
        cam_port = 0
        cam = cv2.VideoCapture(cam_port)
        

        result, image = cam.read()

        if result:
            heading = "Launched Camera"
            cv2.imshow("Camera", image)
            cv2.waitKey(0)
            config.speak("Shall I save it?")
            ans = config.listen()
            if ans != None:
                if "yes" in ans:
                    current = str(datetime.datetime.now())
                    current = current.replace(":","-")
                    current = current.replace(" ","-")
                    file_name = "Assistant/assets/" + str(current) + ".png"
                    cv2.imwrite(file_name, image)
                    return (heading, ["Picture saved to assets."])
                else:
                    return (heading, ["Picture wasn't saved."])
            else:
                return (heading, ["Picture wasn't saved."])

        else:
            print("No image detected. Please try again.")
            config.pic_cam()