# April-voice-assistant
April is your friendly voice assistant that can help you focus on your work by doing your side tasks and bring you the results on your command. Very intuitive and easy to use, providing quick results.

## Features
* In order to give commands you need to press the MIC button just once and it will listen to your commands. You need to press the MIC button once at the beginning of the program.
* At first you can have an introduction of your voice assistant and what are the tasks it can do.
* It will maintain your todo list.
* It can tell you the current date along with the day.
* It can open a webpage tab with the query you enter.
* It can take a picture of you on your command.
* It can give today's news headlines.
* It can give today's crypto currency stocks prices
* It can tell you a joke when you are bored.
* It can inspire you with an inspirational quote.
* It can give you today's weather information.
* It can tell you the meaning of a specific word.

## Installing the dependencies
Use the command provided below in the terminal/command prompt to install the dependencies.
```
pip install -r requirements.txt
```

## Setting up configurations
Open the config.py file and make necessary changes according to your convenience and personal information. Comments have been provided for help. Give yor name in the **ADMIN** variable and other personal details in the following variables. Enter the url of your bookmark websites and the name with which you call the websites in the **BOOKMARKS** variable.<br>
In the Commands List enter the words with which you want the respective commands to be executed. While giving commands your commands must include these words for execution of these commands.

## Executing the program
Run main.py file to execute the program. The assistant window will appear. To give commands the MIC button must be pressed once and your following commands will be executed automatically.<br>
You can make the assistant stop using the commands in **SLEEP** list in config.py file. When this command is passed the assistant will wait untill it's **NAME** is called. During this time no otrher command will be executed and the previous commands output will remain as such for user's reference.

## License
This program is only for education purpose. The web scrapped data has been taken from the following websites and has not been used in any harmful way:
* [TimeAndDate](https://www.timeanddate.com/): For weather information
* [IndiaToday](https://www.indiatoday.in/): For news headlines
* [CoinMarketCap](https://coinmarketcap.com/): For crypto currency stocks prices<br>
The following public apis have also been used that doesn't require any key or account to log in:
* https://icanhazdadjoke.com : For jokes
* https://type.fit/api/quotes : For inspirational quotes
* https://api.dictionaryapi.dev/api/v2/entries/en/ : For dictionary






