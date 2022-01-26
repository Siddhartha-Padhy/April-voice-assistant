import datetime
from bs4 import BeautifulSoup
import requests
import concurrent.futures

def writer(headline):
    with open("Assistant/text_files/news_today.txt","a") as f:
        value = headline.a.text
        f.write(value + "\n")

def news_scrape():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }

    URL = "https://www.indiatoday.in/"

    response= requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text,'lxml')

    headline_block = soup.find('ul',attrs={'class':'itg-listing'})
    headlines = headline_block.find_all('li')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        file = open("Assistant/text_files/news_today.txt","w")
        file.write(str(datetime.date.today())+"\n")
        file.close()

        for headline in headlines:
            executor.submit(writer,headline)
