"""
Film sitesinden filmlerin ismi ve imdb oylarini alacagiz
"""

import requests # verileri cekmek icin
from bs4 import BeautifulSoup #verileri almak icin
url="https://www.imdb.com/chart/top"
responce=requests.get(url) # verileri cektik
html_icerigi=responce.content
soup=BeautifulSoup(html_icerigi,"html.parser") # html icerigini aliyoruz
a=float(input("Rating: "))
basliklar=soup.find_all("td",{"class":"titleColumn"}) # film isimleri
imdb=soup.find_all("td",{"class":"ratingColumn imdbRating"}) #imdb ratingleri

for baslik,rating in zip(basliklar,imdb):
    baslik=baslik.text
    rating=rating.text

    baslik=baslik.strip()
    baslik=baslik.replace("\n","")

    rating=rating.strip()
    rating=rating.replace("\n","")
    if float(rating)>a:
        print("Film ismi: {} Rating: {}".format(baslik,rating))



