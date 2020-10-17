import os
#print(os.getcwd()) #bulundugumuz dizini gosterir
#  os.chdir("")  #bulundugumuz dizini degistirir
#print(os.listdir("/Users/sevdaagalarova/Desktop")) #verilen dizindeki dosyalari listeler
#os.mkdir("test1") #bulundugum dizinde klasor olusturur
#os.makedirs("Test1/Test2") #bulundugum dizinde klasor icinde klasor olusturur
# os.rmdir("test1") #verilen klasoru siler
# os.removedirs("test1/Test2") #verilen dizinde klasor icinde klasoru birlikde siler
#os.rename("test1","Deneme") # verilen dosyanin ismini degistirir
#os.stat("Deneme") # verilen dosya ile ilgili bilgileri getirir
for klasor_yolu,klasor_islemi,dosya_islemi in os.walk("/Users/sevdaagalarova/Desktop"): # bu yoldaki tum dosyalari getirir
    for i in dosya_islemi:
        if i.endswith(".py"): # py ile biten dosyalari ekrana getirir
            print(i)


