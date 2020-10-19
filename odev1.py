"""Bilgisayarınızdaki tüm mp4,txt ve pdf dosyalarını os modülüyle arayın ve bunların nerede
bulunduklarını ve isimlerini ayrı ayrı
"pdf_dosyalari.txt","mp4_dosyaları.txt","txt_dosyaları.txt" adlı dosyalara kaydedin."""
import os
for klasor_yolu,klasor_islemi,dosya_islemi in os.walk("/Users/sevdaagalarova/Desktop"): # bu yoldaki tum dosyalari getirir
    for i in dosya_islemi:
        if i.endswith("pdf"): # py ile biten dosyalari ekrana getirir
            with open("PDF_dosyalari.txt", "w", encoding="utf-8") as file:
                   file.write(i+"\n")
        elif i.endswith("py"):
            with open("py_dosya.txt", "w", encoding="utf-8") as file1:
                   file1.write(i+"\n")



