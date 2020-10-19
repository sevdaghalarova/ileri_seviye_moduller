"Mail atmak icin SMTP serverine ihtiyacimiz olacagi icin GMAIL SMTP serverine baglanacagiz"
import smtplib #smtp servera baglanmak icin
from email.mime.multipart import MIMEMultipart #mailin yapisini olusturmak icin
from email.mime.text import MIMEText #maile ne yazilacagini bununla belirliyoruz
import sys

# Biz bir tane mail yapisi olusturuyoruz. Mimemultipart modulunu kullanarak
message=MIMEMultipart()
message["From"] = "sevdaghalarova@gmail.com"
message["To"] = "sevdaghalarova@gmail.com"
message["Subject"] = "Bu bir SMTP mesajidir"

    # mailin icini olusturalim
text = """
    Bu maili SMTP ile gonderiyorum
    Sevda Aghalarova
    """
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