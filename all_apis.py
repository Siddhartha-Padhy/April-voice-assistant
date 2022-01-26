"""
Contains all the API related functions.
All the API's used are available for free without requiring any key.
"""

import requests
import random
from config import *


"""
Function to get a random joke from website https://icanhazdadjoke.com
"""
def joke():
    heading = "Presenting a joke"
    f = "https://icanhazdadjoke.com/slack"
    data=requests.get(f)
    resj=data.json()
    value = resj["attachments"][0]["text"]
    return (heading, [value])

"""
Function to get an inspirational quote using api https://type.fit/api/quotes
A json file containing 1643 quotes is received
"""
def inspire():
    f = "https://type.fit/api/quotes"
    # 1643 quotes in the api
    data=requests.get(f)
    resj=data.json()
    index = int(random.random()*1643)
    heading = "Quote by " + str(resj[index]['author'])
    text = str(resj[index]['text'])
    return (heading, [text])


"""
Function to get the definition of a word.
"""
def definition():
    config.speak("Enter word")
    word = config.listen()
    heading = word
    response = []
    if word != None:
        f = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
        data = requests.get(f)
        resj = data.json()
        heading = word

        ans = str(resj[0]['meanings'][0]['definitions'][0]['definition'])
        ans += "\nFor Example, " + str(resj[0]['meanings'][0]['definitions'][0]['example'])

        response.append(ans)
    else:
        heading, response = definition()
    
    return (heading, response)
