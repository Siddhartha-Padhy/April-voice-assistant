# Web Scrapping Crypto

from bs4 import BeautifulSoup
import requests
import datetime

def crypto_scrape():
    URL="https://coinmarketcap.com/"
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        }

    req=requests.get(URL, headers=headers)

    soup=BeautifulSoup(req.text,"html.parser")
    tbody=soup.tbody
    trs=tbody.contents
    prices=[]
    with open('Assistant/text_files/crypto.txt', 'w') as f:
        f.write(str(datetime.date.today())+"\n")
        for tr in trs[:10]:
            name,val=tr.contents[2:4]
            price={}
            price['Name']=name.p.text
            price['Price']=val.a.text
            f.write(price['Name'] + ": " + price['Price'] + "\n")
            prices.append(price)
