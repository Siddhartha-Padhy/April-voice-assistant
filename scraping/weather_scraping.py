import requests
from bs4 import BeautifulSoup
import datetime

def weather_scrape(CITY,COUNTRY):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }

    URL = "https://www.timeanddate.com/weather/" + COUNTRY.lower() + "/" + "/" + CITY.lower()

    response = requests.get(URL,headers=headers).text
    soup = BeautifulSoup(response,'lxml')
    first = soup.find('div',attrs={'id':'qlook'})
    temp = str(first.find('div',attrs={'class':'h2'}).text)
    temp=temp.replace("&nbsp;",u"\N{DEGREE SIGN}" )
    condition = str(first.find('p').text)

    table = soup.find('table',attrs={'class':'table table--left table--inner-borders-rows'})
    rows = table.find_all('tr')

    file = open("Assistant/text_files/weather_today.txt","w")
    file.write(str(datetime.date.today())+"\n")
    file.write("Temperature: "+temp+"\n")
    file.write("Condition: "+condition+"\n")
    file.close()

    with open("Assistant/text_files/weather_today.txt","a", encoding="utf-8") as f:
        for row in rows:
            prop = str(row.find('th').text)
            value = str(row.find('td').text)
            
            if prop=="Pressure: " or prop=="Humidity: ":
                text = prop + value + "\n"
                f.write(text)
            
            if prop=="Visibility: ":
                value = value.replace("&nbsp;"," ")
                text = prop + value + "\n"
                f.write(text)