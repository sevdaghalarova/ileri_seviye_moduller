"""
Doviz uygulamasi
"""

import requests # verileri cekmek icin
import sys
from bs4 import BeautifulSoup #verileri almak icin
url="https://data.fixer.io/api/latest?base="
birinci_doviz=input("Birinci doviz: ")

ikinci_doviz=input("Ikinci doviz: ")
miktar=float(input("Miktar: "))
responce=requests.get(url+birinci_doviz) # verileri cektik

#donulen verinin json() seklinde olmasini istiyoruz
json_data=responce.json()
try:
   print(json_data["rates"][ikinci_doviz]*miktar)
except KeyError:
    sys.stderr.write("Boyle doviz yoktur")
    sys.stderr.flush()







