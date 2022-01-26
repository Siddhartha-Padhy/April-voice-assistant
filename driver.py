import datetime     #for date and time
from scraping.news_scraping import news_scrape      #for getting the news
from scraping.weather_scraping import weather_scrape        #for getting weather information
from scraping.crypto import crypto_scrape       #for getting crypto prices
from all_apis import *      #for all the functions using api
from config import config       #for all functions and constants in config file
from google_search import *     #for google search
import os       #for terminating all the threads when the program is closed


#terminating all the threads, including the main thread, when exit command is used
def quit_command():
    config.speak("Turning off. Have a good day.")
    os._exit(1)


#function to read ToDo_list
def read_todo_list():
    heading = "Reading To-Do List"
    response = []
    with open("Assistant/text_files/ToDo_list.txt", "r") as f:
        for line in f:
            response.append(line)

    return (heading, response)


#function to append to ToDo list
def add_todo_list():
    config.speak("Enter task")
    task = config.listen()
    desc = [task]
    if task == None:
        config.speak("Task Please")
        heading, desc = add_todo_list()
    else:
        with open("Assistant/text_files/ToDo_list.txt", "a") as f:
            f.write(task+"\n")
        heading = "Task Added"
    return (heading, desc)


#function to tell today's date
#returns heading(today's date and day) and an empty list
def say_date():
    week_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    today = str(datetime.date.today())
    date = datetime.datetime.now()
    day = str(week_days[date.weekday()])
    complete = "Today: " + day+" "+today
    heading = complete
    return (heading, [""])


"""
Function to return heading and a list of crypto stocks with prices.
Calls the crypto_scrape function if the date in crypto.txt file doesn't match current date.
Else reads the crypto.txt file.
"""
def get_crypto():
    heading = "Crypto Prices Today:"
    response = []
    with open("Assistant/text_files/crypto.txt","r") as f:
        if f.readline().strip() != str(datetime.date.today()):
            crypto_scrape()
            heading, response = get_crypto()
        else:
            for line in f:
                response.append(line)
        
    return (heading, response)


"""
Function to return heading and a list of news headlines.
Calls the news_scrape function if the date in news_today.txt file doesn't match current date.
Else reads the news_today.txt file.
"""
def read_news():
    heading = "Today's Headlines"
    response = []
    with open("Assistant/text_files/news_today.txt","r") as f:
        if f.readline().strip() != str(datetime.date.today()):
            news_scrape()
            heading, response = read_news()
        else:
            for line in f:
                response.append(line)

    return (heading, response)


"""
Function to return heading and a list of weather conditions.
Calls the weather_scrape function if the date in weather_today.txt file doesn't match current date.
Else reads the weather_today.txt file.
"""
def weather_info():
    heading = "Weather Today"
    response = []
    with open("Assistant/text_files/weather_today.txt","r") as f:
        if f.readline().strip() != str(datetime.date.today()):
            weather_scrape(CITY, COUNTRY)
            heading, response = weather_info()
        else:
            for line in f:
                response.append(line)
    return (heading, response)


"""
The main driver code.
Gets the respective heading and desc list according the the command given by the user.
Uses the constant lists to compare the command.
Returns heading and desc
"""
def main_driver(command):
    if any(intro in command for intro in INTRODUCTION):
        head, desc = config.introduce()

    elif any(v_joke in command for v_joke in JOKE):
        head, desc = joke()

    elif any(inspiration in command for inspiration in INSPIRE):
        head, desc = inspire()

    elif any(dic in command for dic in DICTIONARY):
        head, desc = definition()
    
    elif any(crypto in command for crypto in CRYPTO):
        head, desc = get_crypto()

    elif any(news in command for news in NEWS):
        head, desc = read_news()

    elif any(weather in command for weather in  WEATHER):
        head, desc = weather_info()

    elif any(read_todo in command for read_todo in READ_TODO):
        head, desc = read_todo_list()

    elif any(write_todo in command for write_todo in WRITE_TODO):
        head, desc = add_todo_list()

    elif any(camera in command for camera in CAMERA):
        head, desc = config.pic_cam()

    elif any(date in command for date in DATE):
        head, desc = say_date()

    elif any(google in command for google in GOOGLE):
        head, desc = g_search()

    elif any(quit_cmd in command for quit_cmd in EXIT):
        quit_command()

    elif any(sleep_cmd in command for sleep_cmd in SLEEP):
        head = "Sleep"
        desc = None
    
    else:
        head = None
        desc = None

    return head, desc
