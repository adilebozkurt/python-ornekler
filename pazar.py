# sayı = ""
# list = []
# print("Çıkmak için 'q' yazın")
# while True:
#     sayı = input("Bir sayı giriniz: ")
#     if sayı == "q":
#         break
#     try:
#         sayı = int(sayı)
#         list.append(sayı)
#     except ValueError:
#         print("Lütfen geçerli bir sayı giriniz veya çıkmak için 'q' yazınız.")

# if list:
#     list.sort()
#     print("En büyük sayı:", list[-1])
# else:
#     print("Hiçbir sayı girilmedi.")


##############################################################################


# girdi=input("Sayıları boşlukla ayırarak gir:")
# sayi_listesi=list(map(int,girdi.split()))
# en_buyuk=max(sayi_listesi)
# print("En büyük sayı:",en_buyuk)


##############################################################################


# sepet={}
# while True:
#     urun=input("Ürün adı (bitir yazınca durur):")
#     if urun =="bitir":
#         break

#     fiyat=int(input("Fiyatı nedir?"))
#     sepet[urun]=fiyat

# print("\n---sepet---")
# toplam=0
# for urun, fiyat in sepet.items():
#     print(f"{urun}: {fiyat} TL")
#     toplam+=fiyat

# print("Toplam Tutar:",toplam,"TL")


########################################################################################################3


# sepet={}
# while True:
#     urun=input("Ürün adı(bitir yazınca durur):")
#     if urun =="bitir":
#         break

#     fiyat=int(input("Fiyatı nedir?"))

#     if fiyat>50:
#         indirimli_fiyat= int(fiyat*0.9)
#         print(f"{urun} için %10 indirim uygulandı. Yeni fiyat:{indirimli_fiyat}")
#         sepet[urun]=indirimli_fiyat

#     else:
#         sepet[urun]=fiyat


# print("\n--- sepet(İndirimli Fiyatlar) ---")
# toplam=0

# for urun, fiyat in sepet.items():
#     print(f"{urun}:{fiyat},TL")
#     toplam+=fiyat

# print("Toplam Tutar:",toplam,"TL")



########################################################################################

# notlar={}

# while True:
#     isim=input("Öğrenci adı(bitir yazınca durur)")
#     if isim=="bitir":
#         break   

#     notu=int(input("Notu kaç?:"))
#     notlar[isim]= notu

# print("\n--- Durumlar ---")

# for isim, notu in notlar.items():
#     if notu>=50:
#         print(f"{isim}: -> Geçti({notu})")

#     else:
#         print(f"{isim}: -> Kaldı({notu})")



##################################################################################################



# notlar={}

# while True:
#     isim=input("Öğrenci adı(bitir yazınca durur)")
#     if isim=="bitir":
#         break   

#     notu=int(input("Notu kaç?:"))
#     notlar[isim]= notu

# print("\n--- Durumlar ---")

# for isim, notu in notlar.items():
#     if notu>=50:
#         print(f"{isim}: -> Geçti({notu})")

#     else:
#         print(f"{isim}: -> Kaldı({notu})")

# toplam=0

# for notu in notlar.values():
#     toplam+=notu

# ortalama= toplam/ len(notlar)
# print(f"\nSınıf Ortalaması: {ortalama:.2f}")


###########################################################################


# def durum_belirle(notu):
#     if notu >= 50:
#         return "Geçti"
#     else:
#         return "Kaldı"

# isim=input("Öğrenci adı:")
# notu=int(input("Notu kaç ?:"))

# sonuc=durum_belirle(notu)

# print(f"{isim} {sonuc}({notu})")

############################################################################3


yas=int(input("Yaşınızı giriniz:"))
if yas<18:
    print(False)

else:
    print(True)