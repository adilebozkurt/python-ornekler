# hata çeşitleri
# 1. SyntaxError:
# çalışma zamnaı hataları
# mantık hataları
# demetler
# listelerh
# sözlükler
# kümeler
# fonksiyonlar(gömülü fonksiyonlar, özel fonksiyonlar(modül))
#import math


# def personel_bilgi(adsoyad, c_yıl, yas, cinsiyet, maas):
#     print("adsoyad\t\t:",adsoyad)
#     print("c_yıl\t\t:",c_yıl)
#     print("yaş\t\t:",yas)
#     print("cinsiyet\t:",cinsiyet)
#     print("maaş\t\t:",maas)
# personel_bilgi("Ahmet Yılmaz","2004",23,"erkek",5000)


# def kare_bul(i):
#     print(i**2)
# kare_bul(12)



# def onkat(n):
#     return n*10
# y= onkat(3)
# print(y)



# import random
# for i in range(1):
#     print(random.randrange(1,100))


# import random
# for i in range(6):
#     print(random.randrange(1,50), end=" ")



# import random
# liste = ["ahmet","emir","elif","baran","yiğit","sinem","volkan"]
# print(random.sample(liste,3))



# kullanıcıdan 1-5 arasında bir sayı isteyiniz. kullanıcı 3 sayısını girdiğinde break komutu ile döngüden çıkarak "3 sayısı girildi ve döngüden çıkıldı" mesajı veren algoritmayı yaz.

# while True:
#     try:
#         sayı = int(input("1-5 arasında bir sayı giriniz: "))
#         if sayı < 1 or sayı > 5:
#             print("Lütfen 1-5 arasında bir sayı giriniz.")
#             continue
#         if sayı == 3:                                                 # try bloğu içindeki kodlar hata vermediği sürece çalışır.
#             print("3 sayısı girildi ve döngüden çıkıldı")                # eğer hata verirse except bloğuna geçer.
#             break
#         else:
#             print("girilen sayı doğru")
#     except ValueError:
#         print("Lütfen geçerli bir sayı giriniz.")



 ##elemanları alfabedeki ilk 8 harf olan bir liste oluşturarak e harfine gelindiğinde döngüden çıkan algoritmayı yazınız
# harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# for harf in harfler:
#     if harf == 'e':
#         print("e harfine gelindi ve döngüden çıkıldı")
#         break
#     print(harf)







 ##random metodu ile 0-20 arasında bir sayı seçerek kullanıcıdan bu sayıyı tahmin etmesini isteyin daha sonra kullan.tahminine göre arttır ya da azalt diye yönlendiren algoritmayı yazınız.


# import random

# sayı = random.randint(0, 20)
# print("0-20 arasında bir sayı tuttum,tahmin edebilecek misin?")

# while True:
#     try:
#         tahmin = int(input("Tahmininiz: "))
#         if tahmin < 0 or tahmin > 20:
#             print("Lütfen 0-20 arasında bir sayı giriniz.")
#             continue
#         if tahmin < sayı:
#             print("Daha büyük bir sayı girin.")
#         elif tahmin > sayı:
#             print("Daha küçük bir sayı girin.")
#         else:
#             print("Tebrikler! Doğru tahmin ettiniz.")
#             break
#     except ValueError:
#         print("Lütfen geçerli bir sayı giriniz.")







##ödev== 4 karakterli bir şifre oluşturulmasını isteyen kodu while, break ve continue kullanarak yazınız.






##1-30 arasındaki sayıları bir liste haline getirerek sadece tek sayıları yazdıran kod

# sayılar = list(range(1, 31))
# tek_sayılar = []

# for sayı in sayılar:
#     if sayı % 2 != 0:
#         tek_sayılar.append(sayı)

# print(tek_sayılar)




# yazılımdas en önemli şey class( sınıf )
# bunu yazdıysan yazılımcısındır
# haftaya class yapısını göreceğiz




# while True:
#     if acil_durdurma_butonu_basilir:  # Eğer butona basıldıysa
#         motoru_durdur()  # Aracın motorlarını durdur
#         hareketi_durdur()  # Tüm hareket sistemlerini durdur
#         guvenli_modu_aktif_et()  # Güvenli modda kal (örneğin, durma pozisyonuna çekil)
#     elif acil_durdurma_butonu_cekilirse:  # Eğer buton çekildiyse
#         motoru_baslat()  # Motorları yeniden başlat
#         araci_hareket_ettir()  # Aracı tekrar hareket ettir





# def yaz():
#     print('merhaba Dünya')
# yaz()
# yaz()


# y=20
# def fonksiyon():
#     global y
#     y=5
#     print("fonksiyon içi y:",y)
# fonksiyon()






