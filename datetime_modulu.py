from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL,"")
suan=datetime.now() # simdiki zamani gosterir

print(datetime.ctime(suan)) # zamani gosterir

print(datetime.strftime(suan,"%Y")) # sadece yil bilgisini alir
print(datetime.strftime(suan,"%B")) # sadece ay bilgisini alir
print(datetime.strftime(suan,"%D")) #sadece GUN bilgisini alir
print(datetime.strftime(suan,"%X")) #sadece saat bilgisini alir
print(datetime.strftime(suan,"%A")) #sadece gun  ismini alir

print(datetime.timestamp(suan)) #suanki zamani saniye cinsinden gosterir
print(datetime.fromtimestamp(2400933321)) # verdigimiz saniyeyi tarihe cevirir

