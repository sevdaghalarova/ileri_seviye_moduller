import requests # verileri cekmek icin
from bs4 import BeautifulSoup #verileri almak icin
url="https://yellowpages.com.tr/ara?q=eskisehir"
responce=requests.get(url) # verileri cektik
html_icerigi=responce.content
soup=BeautifulSoup(html_icerigi,"html.parser") # html icerigini aliyoruz
for i in soup.find_all("p"): # tum p degerlerini aliriz
    pass
    #print(i.text) # p-nin text kismini alir
    #print("*******************************")

print(soup.find_all("div",{"class":"yp-poi-box-2"}))