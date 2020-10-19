from PIL import Image,ImageFilter
image=Image.open("susa.jpg")
#image.show() #resmi goster

image.rotate(180).save("r.jpg") # resmi istedigimiz derecede dondurup kayd ediyoruz
image.convert(mode="L").save("g.jpg") # siyah beyaz

boyut=(400,400) # farkli boyut veriyoruz
image.thumbnail(boyut) # boyutu degisiyoruz
image.save("boyut.jpg")
image.filter(ImageFilter.GaussianBlur(5)).save("blur.jpg") #resmi blurlastir

image2=Image.open("kelbecer.jpg")
kirp=(350,400,350,200)
image2.crop(kirp).save("kelbecer2.jpg") #resmi kirpiyor
