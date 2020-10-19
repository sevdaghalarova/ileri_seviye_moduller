"""
Bu dosyayı okuyarak, her bir kişiye isimleriyle beraber mail göndermeye çalışın.
Dosya formatı şu şekilde olacak.
"""

import smtplib #smtp servera baglanmak icin
from email.mime.multipart import MIMEMultipart #mailin yapisini olusturmak icin
from email.mime.text import MIMEText #maile ne yazilacagini bununla belirliyoruz
import sys
with open("mailler.txt","r") as file:

    for i in file:
        i=i[:]
        liste=i.split(",")


# Biz bir tane mail yapisi olusturuyoruz. Mimemultipart modulunu kullanarak
message=MIMEMultipart()
message["From"] = "sevdaghalarova@gmail.com"
message["To"] =liste[1]
message["Subject"] = "Bu bir SMTP mesajidir"

    # mailin icini olusturalim
text = liste[0]
    # Yazinin mesaj yapisina gitmesi icin bir tane mesaj_govdesi objesi olusturub (Mimetext modulu ile) icine yazimizi gondericez
message_body = MIMEText(text, "plain")  # plain duz bir yazi olmasi anlamina gelir
    # simdi bu mesaj_govdesini mail yapimiza atalim
message.attach(message_body)  # attach metodu ile bunu yapiyorum


#   Simdi SMTP serverine baglanalim
try:

    # SMTP objesi olusturalim
    mail=smtplib.SMTP("smtp.gmail.com",587) # 587 smtp gmail portu
    mail.ehlo() #bu code yazmakla smtp serverine baglandik
    mail.starttls() #girecegimiz kullanici adi ve sifrelerin sifrelenmesi icin bu kodu giriyoruz
    mail.login("sevdaghalarova@gmail.com","ilqar2012") #mail ve sifremizi yaziyoruz
    mail.sendmail(message["From"],message["To"],message.as_string()) #artik mailimizi gondericez, kimden gitdi kime gitdi ve Mimemultiparti stringe ceviriyoruz
    print("Mail basariyla gonderildi")
    mail.close()
except:
    sys.stderr.write("Bir sorun olustu")
    sys.stderr.flush()
