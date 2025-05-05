# print("Merhaba python kampı")
# isim="Engin Demiroğ"
# print(isim)

# tc="12345678910"
# floatsayi=10.5
# print(type(tc))
# print(type(floatsayi))

# durum=False
# print(type(durum))



# istenenkredi=100000
# hesap=9555
# minimumOlmasıGerkenHesap=10000

# if hesap>=minimumOlmasıGerkenHesap:
#     print("Kredi verilebilir")
#     print("ödemeler hesaplandı")
# elif hesap>=9000 and hesap<=9500:
#     print("Müdüre sorulacak")
# elif hesap>=9501 and hesap<=9999:
#     print("Genel müdüre sorulacak")
# else:
#     print("Kredi almak için bakiyeniz yetersiz")
# print("işlem sonu")



# istenenkredi=100000
# hesap=9555
# minimumOlmasıGerkenHesap=10000

# if hesap>=minimumOlmasıGerkenHesap:
#     print("Kredi verilebilir")
#     print("ödemeler hesaplandı")
# elif hesap>=9000 and hesap<=9500:
#     print("Müdüre sorulacak")
# elif hesap>=9501 and hesap<=9999:
#     print("Genel müdüre sorulacak")
# else:
#     print("Kredi almak için bakiyeniz yetersiz")
# print("işlem sonu")


# urunler=["Laptop","Mouse","Keyboard"]
# print(urunler)
# #print(type(urunler))
# urunler.append("Telefon")
# print(urunler)


# ogrenciler1=["İlker","Cavit","Berkay"]
# ogrenciler2=["Kerem","Halil","Murat"]

# ogrenciler1=ogrenciler2
# ogrenciler2[0]="Engin"
# print(ogrenciler2)
# print(ogrenciler1)


# sayi1=10
# sayi2=20
# sayi1=sayi2
# sayi2=60
# print(sayi2)
# print(sayi1)

# referans tip-> list
# değer tip-> int

  
# isim="Engin"
# print(isim[0])


# bosliste=[]


# sayi1=int(input("Birinci sayıyı giriniz:"))
# sayi2=int(input("ikinci sayıyı giriniz:"))
# print("Lütfen yapmak istediğiniz işlemi seçin: ")
# print("1.Toplama")
# print("2.Çıkarma")
# print("3.Çarpma")
# print("4.Bölme")
# secim=input("Seçiminiz yapınız(1/2/3/4):")
# if secim=="1":
#     print("Toplama işlemi sonucunuz:",sayi1+sayi2)
# elif secim=="2":
#     print("Çıkarma işlemi sonucunuz:",sayi1-sayi2)
# elif secim=="3":
#     print("Çarpma işlemi sonucunuz:",sayi1*sayi2)
# elif secim=="4":
#     if sayi2!=0:
#         print("Bölme işlemi sonucunuz:",sayi1/sayi2)
#     else:
#         print("Bir sayı sıfıra bölünemez")
# else:
#     print("Geçersiz bir seçim yaptınız.")



# sehirler=["Ankara","İstanbul","İzmir",]

# for sehir in sehirler:
#     print(sehir)


# for sayi in range(10):
#     print(sayi)

# for i in range(1,10,2):
#     print(i)

# for sayi in range(0,10,2):
#     print(sayi)


# sayac=1
# while sayac<=10:
#     print(sayac)
#     sayac=sayac+1


# isim=input("Adınız:")
# print("isim:",isim)

# sayi=int(input("sayı:"))
# print(sayi)


# sayi=int(input("sayı:"))
# if sayi<0:
#     print(sayi,"negatiftir")
# elif sayi>0:
#     print(sayi,"pozitiftir")
# else:
#     print("sıfırdır")



# try:
#     sayi=int(input("sayı:"))
#     if sayi<0:
#         print(sayi,"negatiftir")
#     elif sayi>0:
#         print(sayi,"pozitiftir")
#     else:
#         print("sıfırdır")

#     if sayi%2==0:
#         print(sayi,"çifttir")
#     else:
#         print(sayi,"tektir")

# except ValueError:
#     print("Lütfen geçerli bir tam sayı giriniz")



# def selamver():
#     print("merhaba")
# def kredihesapla():
#     print("kredi hesaplandı")

# kredihesapla()


# isim=12.0
# print(type(isim))


# sayi=input("sayı:")
# try:
#     tam_sayi=int(sayi)
#     ondalikli_sayi=float(sayi)

#     print(f"Tam sayı olarak:{tam_sayi}")
#     print(f"Ondalıklı sayı olarak:{ondalikli_sayi}")

# except ValueError:
#     print("Lütfen geçerli bir sayı giriniz")


# try:
#     sayi1=float(input("Birinci sayıyı giriniz:"))
#     sayi2=float(input("ikinci sayıyı giriniz:"))    
#     print("Toplama=",sayi1+sayi2,"Çıkarma=",sayi1-sayi2,"Çarpma=",sayi1*sayi2,"Bölme=",sayi1/sayi2)
# except ValueError:
#     print("Lütfen geçerli bir sayı giriniz")



# try:
#     sayi1=float(input("Birinci sayıyı giriniz:"))
#     sayi2=float(input("İkinci sayıyı giriniz:"))

#     print("Toplama:",sayi1,"+",sayi2,"=",sayi1+sayi2)
#     print("Çıkarma:",sayi1,"-",sayi2,"=",sayi1-sayi2)
#     print("Çarpma:",sayi1,"*",sayi2,"=",sayi1*sayi2)

#     if sayi2!=0:
#         print("Bölme:",sayi1,"/",sayi2,"=",sayi1/sayi2)
#     else:
#         print("İkinci sayı sıfır olduğu için sayı sıfıra bölünemez")  

# except ValueError:
#     print("Lütfen geçerli bir sayı giriniz")     



# kullanici_not=int(input("Notunuzu giriniz:"))
# if kullanici_not>=90:
#     print("Harf notunuz:A")
# elif kullanici_not>=80 and kullanici_not<=89:
#     print("Harf notunuz:B")
# elif kullanici_not>=70 and kullanici_not<=79:
#     print("Harf notunuz:C")
# elif kullanici_not>=60 and kullanici_not<=69:
#     print("Harf notunuz:D")
# else:
#     print("Harf notunuz:F")



# try:
#     kullanici=int(input("Lütfen notunuzu giriniz"))

#     if kullanici<0 or kullanici>100:
#         print("Lütfen 0 ile 100 arasında bir sayı giriniz")
#     elif kullanici>=90:
#         print("Harf notunuz:A")
#     elif kullanici>=80:
#         print("Harf notunuz:B")
#     elif kullanici>=70:
#         print("Harf notunuz:C")
#     elif kullanici>=60:
#         print("Harf notunuz:D")
#     else:
#         print("Harf notunuz:F")

# except ValueError:
#     print("Lütfen geçerli bir sayı giriniz")



# try:
#     şifre="1234"
#     girilen_şifre=input("şifrenizi giriniz:")
#     if not girilen_şifre.isdigit():
#         raise ValueError("şifre sadece rakamlardan oluşmalıdır")
#     if şifre==girilen_şifre:
#         print("şifre geçerli")
#     else:
#         print("şifre geçersiz")
# except ValueError as e:
#     print(f"Hata:{e}")


 
# sayi=int(input("Bir sayı giriniz:"))
# if sayi%2==0:
#     print(sayi,"çift sayıdır")
# else:
#     print(sayi,"tek sayıdır")


# try:
#     sayi=int(input("Bir sayı giriniz:"))

#     if sayi%2==0:
#         print(sayi,"çift sayıdır")
#     else:
#         print(sayi,"tek sayıdır")

# except ValueError:
#     print("Lütfen geçerli bir tam satı giriniz")


# try:
#     yas=int(input("Yaşınızı giriniz:"))
    
#     if yas>=0:
#      if yas<18:
#          print("Reşit değilsiniz")
#      else:
#         print("Reşisiniz")
#     else:
#         print("Yaşınız negatif olamaz")

# except ValueError:
#    print("Lütfen geçerli bir sayı giriniz")


# try:
#     yas=int(input("Yaşınızı giriniz:"))

#     if yas<0:
#         print("Yaşınız negatif olamaz")
#     elif yas<18:
#         print("Reşit değilsiniz")
#     else:
#         print("Reşitsiniz")
    
# except ValueError:
#     print("Lütfen geçerli bir sayı giriniz")



# try:
#     a=float(input("Birinci kenar uzunluğunu giriniz:"))
#     b=float(input("İkinci kenar uzunluğunu giriniz:"))
#     c=float(input("Üçüncü kenar uzunluğunu giriniz:"))
     
#     if a+b>c and a+c>b and b+c>a:
#         print("Geçerli bir üçgen")
#     else:
#         print("Geçerli bir üçgen değil")

# except ValueError:
#     print("Lütfen geçerli bir sayı giriniz")



# for i in range(1,11):
#     print



# sayi=int(input("Bir sayı giriniz:"))
# toplam=0

# for i in range(1,sayi+1):
#     if sayi>0:
#         toplam=toplam+i
#     else:
#         print("Lütfen pozitif bir sayı giriniz")
# print("Toplam=",toplam)




# try:
#     # Kullanıcıdan pozitif bir sayı al
#     sayi = int(input("Bir pozitif sayı giriniz: "))
    
#     # Negatif bir sayı girilirse hata mesajı göster
#     if sayi <= 0:
#         print("Lütfen pozitif bir sayı giriniz.")
#     else:
#         toplam = 0
#         for i in range(1, sayi + 1):
#             toplam += i
#         print("1'den", sayi, "sayısına kadar olan sayıların toplamı:", toplam)
        
# except ValueError:
#     print("Lütfen geçerli bir tam sayı giriniz.")



# for i in range(1,51):
#     if i%2==0:
#         print(i)
    


# while True:
#     sayi=int(input("Bir sayı giriniz:"))
#     if sayi==0:
#         print("Döngü sonlandırıldı")
#          break
#     else:
#         print("Girilen sayı:",sayi)
#         


# for i in range(1,21):
#     if i%5==0:
#         continue
#     print(i)



# parola="1453"
# while True:
#     parola_1=input("parolanızı giriniz:")
#     if parola==parola_1:
#         print("Giriş başarılı")
#         break
    

# şifre="1453"
# girilen_şifre=""
# while girilen_şifre!=şifre:
#     girilen_şifre=input("şifrenizi giriniz:")
#     if şifre==girilen_şifre:
#         print("Giriş başarılı")
#     else:
#         print("Yanlış şifre, tekrar deneyiniz")



# sayi=int(input("Bir sayı giriniz:"))
# çarpim=1
# for i in range(1,11):
#     çarpim=i*sayi
#     print(sayi,"x",i,"=",çarpim,sep="")
# print()



# toplam=0
# adet=0
# for i in range(1,11):
#     sayi=int(input("Bir sayı giriniz:"))
#     if sayi>0:
#         toplam=toplam+sayi
#         adet=adet+1
# if adet>0:
#    ortalama=toplam/adet
#     print("Ortlama",ortalama)
#  else:
#     print("Hiç pozitif sayı girilmedi")



# kelime="python"
# kullanici=""
# while kullanici!=kelime:
#     kullanici=input("Kelime tahmin ediniz:")
#     if kullanici==kelime:
#         print("Tebrikler doğru kelimeyi tahmin ettiniz")
#         break
# print("oyun bitti")


              ### Baran'a sorulacak

# sayi=int(input("Bir sayı giriniz:"))
# adet=0
# for i in range(2,sayi):
#     if sayi%i==0:
#         adet+=1
#         break
# if adet==0:
#     print(sayi,"Asal sayıdır")
# else:
#     print(sayi,"Asal sayı değildir")



# N=int(input("Bir sayı giriniz:"))
# toplam=0
# for i in range(1,N+1):
#     if i%2==0:
#         toplam=toplam+i
# print("1 ile",N,"arasındaki çift sayıların toplamı:",toplam)



# n=int(input("kaç elemanlı bir Fibonacci dizisi istersiniz:"))
# a,b=0,1
# print("Fibonacci Dizisi:")
# for i in range(n):
#     print(a,end=" ")
#     a,b=b,a+b



# sayi1=int(input("Birinci sayıyı giriniz:"))
# sayi2=int(input("İkinci sayıyı giriniz:"))
# print("Yapmak istediğiniz işlemi seçiniz(1/2/3/4):")
# print("1.Toplama")
# print("2.Çıkarma")
# print("3.Çarpma")
# print("4.Bölme")
# secim=int(input("Seçiminiz:"))
# if secim==1:
#     print("Toplama:",sayi1+sayi2)
# elif secim==2:
#     print("Çıkarma:",sayi1-sayi2)
# elif secim==3:
#     print("Çarpma:",sayi1*sayi2)
# elif secim==4:
#     if sayi2!=0:
#         print("Bölme:",sayi1/sayi2)
#     else:
#         print("Bir sayı sıfıra bölünemez")



# sayi=int(input("Bir sayı giriniz:"))
# faktoriyel=1
# for i in range(1,sayi+1):
#     faktoriyel=faktoriyel*i
# print(sayi,"faktoriyel:",faktoriyel)



# sayi=int(input("Bir sayı giriniz:"))
# carpim=1
# for i in range(1,11):
#     carpim=i*sayi
#     print(sayi,"x",i,"=",carpim,sep="")



# sayi=int(input("Bir sayı giriniz:"))
# if sayi%2==0:
#     print(sayi,"çift sayıdır")
# else:
#     print(sayi,"tek sayıdır")


# toplam=0
# for i in range(1,11):
#     sayi=int(input(str(i)+".sayıyı giriniz:"))
#     if sayi>0:
#         toplam+=sayi
# print("Toplam:",toplam)



# sayi=int(input("Bir sayı giriniz:"))
# if sayi%3==0:
#     print("Evet,bölünüyor")
# else:
#     print("Hayır bölünmüyor")




# toplam=0
# for i in range(1,11):
#     sayi=int(input(str(i)+".sayıyı giriniz:"))
#     if sayi>0:
#         toplam+=sayi
#     print("Toplam:",toplam)



# adet=0
# for i in range(2,101):
#     asal=True
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             asal=False
#             break
#     if asal:
#         print(i,end=" \n")


# kullaniciadi="egemyo"
# doğru="1955"
# giriş_hakkı=3
# hatasayısı=0
# while hatasayısı!=3:
#     kullanici=input("Kullanıcı adınızı giriniz:")
#     şifre=input("Şifrenizi giriniz:")
#     if kullaniciadi==kullanici and doğru==şifre:
#         print("Giriş yapıldı")
#         break
#     else:
#         hatasayısı+=1
#         print("hatalı giriş")
# if hatasayısı==3:
#         print("giriş hakkınız bitti")        



# toplam=0
# for i in range(1,11):
#     sayi=int(input(str(i)+". sayı giriniz:"))
#     if sayi>0:
#         toplam+=sayi
# print("Toplam:",toplam)


# for i in range(2,101):
#     asal=True
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             asal=False
#             break
#     if asal:
#         print(i)    


# sayi=int(input("sayı:"))
# toplam=0
# for i in range(1,sayi):
#     if sayi%i==0:
#         toplam+=i
# if toplam==sayi:
#     print(sayi,"Mükemmel sayıdır")
# else:
#     print(sayi,"mükemmek sayı değildir")



# sayi=int(input("sayı:"))
# toplam=0
# adet=0
# for i in range(sayi-1,0,-1):
#     if sayi%i==0:
#          toplam+=i
#          adet+=1
#     if adet==3:
#           break
# if toplam==sayi:
#          print(sayi,"yarı mkemmel sayıdır")
# else:
#     print(" yarı mükemmel sayı değildir")    


# n=int(input("sayı:"))
# for i in range(1,n+1):
#         print("*"*i)
# print()



# for i in range(1,11):
#     for j in range(1,11):
#         if i==1 or j==1 or  i==10 or i==5:
#             print("E",end=" ")
#         else:
#             print(" ",end="")
#     print()



# a = 5  
# b = 2.5  
# c = "Merhaba"  
# print(type(a), type(b), type(c))



# isim=input("İsminiz:")
# yas=int(input("Yaşınız:"))
# print("Merhaba",isim,",",yas,"yaşındasınız")


# sayi=int(input("sayı:"))
# if sayi%2==0:
#     print(sayi,"çift sayıdır")
# else:
#     print(sayi,"tek sayıdır")


# sayi=int(input("sayı:"))
# if sayi>0:
#     print(sayi,"sıfırdan büyüktür")
# elif sayi<0:
#     print(sayi,"sıfırdan küçüktür")
# else:
#     print("sıfır")



# toplam=0
# for i in range(1,11):
#     toplam+=i
# print("Toplam:",toplam)


# sayi=int(input("sayı:"))
# adet=0
# for i in range(2,sayi):
#     if sayi%i==0:
#      adet+=1
#      break
# if adet==0:
#    print("asaldır")
# else:
#    print("asal değil")



# toplam=0
# n=1
# while n>0:
#     toplam+=n
#     n+=1
#     if n==11:
#         break
# print(toplam)



# n=int(input("kaç elemanlı Fibonacci dizisi istersiniz:"))
# a,b=0,1
# print("Fibonacci Dizis")
# for i in range(n):
#     print(a,end=" ")
#     a,b=b,a+b



# sayi=int(input("sayı:"))
# for i in range(2,sayi+1):
#     asal=True
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             asal=False
#             break
#     if asal:
#         print(i)




# A=1
# sayi=int(input("sayı:"))
# for i in range(1,sayi+1):
#     if i%3==0:
#        A=i**2
#        print(A)



# adet=0
# for i in range(1,11):
#     n=int(input(str(i)+".sayı:"))
#     if n%2==1:
#         adet+=1
# print(adet)



# a=""
# for i in range(1,11):
#     n=int(input(str(i)+".sayı:"))
#     if n%2==0:
#         a+=str(n)+" "
# print(a)



# adet=0
# for i in range(1,11):
#     n=int(input(str(i)+".sayı:"))
#     if n<0:
#         adet+=1
# print(adet)



# x=""
# for i in range(1,11):
#     n=int(input(str(i)+".sayı:"))
#     if n<0:
#         x+=str(n)+"  "
# print(x)

 

# adet=0
# for i in range(1,11):
#     n=int(input(str(i)+".sayı:"))
#     if n<100 and n>1:
#         adet+=1
# print(adet)



# toplam=0
# for i in range(1,11):
#     n=int(input(str(i)+".sayı:"))
#     if n<100 and n>0:
#         toplam+=n
# print(toplam)




# toplam=0
# adet=0
# for i in range(1,11):
#     n=int(input(str(i)+".sayı:"))
#     if n<100 and n>0:
#         toplam+=n
#         adet+=1
# ortalama=toplam/adet
# print(ortalama)



# en_buyuk=None
# for i in range(1,11):
#     sayi=int(input(str(i)+".sayı:"))
#     if en_buyuk is None or sayi > en_buyuk:
#         en_buyuk=sayi
# print("Girilen en büyük sayı:",en_buyuk)



# for i in range(1,101):
#     print(i)

    
# for i in range(1,51):
#     if i%2==1:
#         print(i)


# kelime=input("bir kelime giriniz:")
# for i in range(5):
#     print(kelime)


# sayı=int(input("Bir sayı giriniz:"))
# faktor=1
# for i in range(1,sayı+1):
#     faktor*=i
# print(sayı,"!","=",faktor)


# a=0
# for i in range(1,21):
#    a=i**2
#    print(a) 


# sayi=int(input("Bir sayı giriniz:"))
# for i in range(sayi,0,-1):
#     print(i)



# en_buyuk=None
# toplam=0
# for i in range(1,11):
#     sayi=int(input("Bir sayı giriniz:"))
#     if en_buyuk is None or  sayi>en_buyuk:
#         en_buyuk=sayi
#     toplam=toplam+sayi
# print("Toplam:",toplam)
# print("En büyük sayı=",en_buyuk)



# kelime=input("Bir kelime giriniz:")
# for harf in kelime:
#     print(harf)

 

# for i in range(5):
#     sayi=int(input("sayı:"))
#     if sayi%3==0 and sayi%5==0:
#         print(sayi)


# sayi=int(input("Fibonacci dizesi kaç basamaktan oluşuyor olsun: "))
# print("Fibonacci Dizisi")
# a,b=0,1
# for i in range(sayi+1):
#     a,b=a+b,a
#     print(a,end=" ")



# n = int(input("Bir sayı girin: "))
# i = 1
# while i <= n:
#     hyperbolic_result = i * i + 1  
#     is_prime = True
#     if hyperbolic_result < 2:
#         is_prime = False
#     else:
#         j = 2
#         while j * j <= hyperbolic_result:
#             if hyperbolic_result % j == 0:
#                 is_prime = False
#                 break
#             j += 1
#     if is_prime:
#         print(i, "->", hyperbolic_result)
#     i += 1


# sayi=0
# while sayi<200000:
#     adet=0
#     toplam=0
#     sayi+=1
#     for i in str(sayi):
#         adet+=1
#     for i in str(sayi):
#         toplam+=int(i)**adet
#     if toplam==sayi:
#         print(sayi,"sayısı Armstrong sayısıdır")




# sayi=int(input("sayı:"))
# for i in range(1,sayi+1):
#     sayi2=(i**2)+1
#     adet=0
#     for j in range(2,int(sayi2**0.5)+1):
#         if sayi2%j==0:
#             adet+=1
#             break
#     if adet==0:
#         print(i,"->",sayi2,"hiperboliktir")


# for i in range(2,600851475144):
#     asal=True
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             asal=False
#     if 600851475143%i==0 and asal:
#         print(i)



# n = 20
# while True:
#     bolendir = True
#     for i in range(1, 21):
#         if n% i != 0:
#             bolendir= False
#             break
#     if bolendir:
#         break
#     n+= 20

# print(n)



# toplam=0
# toplam2=0
# for i in range(1,101):
#     toplam+=i**2
#     toplam2+=i
# print(toplam2**2-toplam)



# adet=0
# sayı=1
# while adet!=10001:
#     sayı+=1
#     asal=True
#     for i in range(2,int(sayı**0.5)+1):
#         if sayı%i==0:
#             asal=False
#             break
#     if asal:
#         adet+=1
# print(sayı)

    

# for i in range(1,21):
#     if i%3!=0:
#         continue
#     print(i)


# n=int(input("n:"))
# for i in range(n-1,1,-1):
#     if i%5==2:
#         break
# print(i)



# sayilar = [10, 20, 30, 40]

# print(sayilar[0])  # İlk eleman (10)
# print(len(sayilar))  # Listenin uzunluğu (4)

# for sayi in sayilar:
    # print(sayi)

# sayilar.append(50)  # [10, 20, 30, 40, 50]
# print(sayilar)



# sayi=int(input("Bir sayı giriniz:"))
# if sayi>0:
#     print("Pozitif sayı")
# elif sayi<0:
#     print("Negatif sayı")
# else:
#     print("Sayı sıfırdır")


# sayi=int(input("Bir sayı giriniz:"))
# if sayi%2==0:
#     print("Bu sayı çifttir")
# else:
#     print("Bu sayı tektir")


# for i in range(1,6):
#     for j in range(1,11):
#         print(i,"x",j,"=",i*j,end="\t") 
#     print()


# liste=[]
# for i in range(1,6):
#     sayi=int(input(str(i)+".sayıyı giriniz:"))
#     liste.append(sayi)
# print("Girilen sayılar:",liste)
# print("En büyük sayı:",max(liste))
# print("En küçük sayı:",min(liste))



# pozitif_sayılar=[]
# negatif_sayılar=[]
# for i in range(1,11):
#     sayi=int(input(str(i)+".sayıyı giriniz:"))
#     if sayi==0:
#         continue
#     elif sayi>0:
#         pozitif_sayılar.append(sayi)
#     else:
#         negatif_sayılar.append(sayi)
# print("Pozitif sayılar:",pozitif_sayılar)
# print("Negatif sayılar:",negatif_sayılar)



# liste=[12,-5,3,-7,9,-1,0,4]
# pozitif_sayi=[]
# negatif_sayi=[]
# for i in liste:
#     if i>0:
#         pozitif_sayi.append(i)
#     elif i<0:
#         negatif_sayi.append(i)
#     else:
#         continue
# print("Pozitif sayılar:",pozitif_sayi)
# print("Negatif sayılar:",negatif_sayi)



# liste1=[]
# liste=[1,2,3,4,5]
# for i in range(len(liste)-1,-1,-1):
#     liste1.append(liste[i])
# print(liste1)



# liste=[1,3,7,1,5,1,8,1]
# count=0
# döngü=0
# while döngü<len(liste):
#     if liste[döngü]==1:
#         count+=1
#     döngü+=1
# print(count)



# liste=[]
# for i in range(1,11):
#     liste.append(i)
# for sayi in liste:
#     print(sayi**2)



# sayı=int(input("Bir sayı giriniz:"))
# while sayı>1:
#     sayı=sayı//2
#     print(sayı)




# liste=[[1,2,3],[4,5,6],[7,8,9]]
# for i in liste:
#     print(i)
#     for j in i:
#         print(j)



# liste=[-3,2,0,-5,4,8,0,-1]
# for i in liste:
#     if i > 0:
#         print(i," pozitif")
#     elif i<0:
#       print(i," negatif")
#     else:
#         print("sıfır")



# liste=[]

# sayı=int(input("Bir sayı giriniz:"))
# for i in range(2,sayı):
#     adet=0
#     for j in range(2,i):    
#         if i%j==0:
#             adet+=1
#             break
#     if adet==0:
#         liste.append(i)
# print(liste)




# sayı=int(input("Bir sayı giriniz:"))
# liste=[]
# for i in range(1,sayı):
#     if i%2==0:
#         liste.append(i)
# print(liste)
# if sayı<10:
#     print("sayı çok küçük")
# else:
#     print("sayı yeterince büyük")


# sayı=1
# toplam=0
# while sayı!=0:
#     sayı=int(input("sayı:"))
#     toplam+=sayı
#     if sayı==0:
#         break
# print(toplam)



# sayı=1
# çarpım=1
# while sayı!=0:
#     sayı=int(input("Bir sayı giriniz:"))
#     if sayı!=0:
#         çarpım=çarpım*sayı
# print(çarpım)



# toplam=0
# çarpım=1
# sayı=1
# while sayı!=0:
#     sayı=int(input("sayı:"))
#     if sayı!=0:
#         çarpım=çarpım*sayı
#         toplam+=1
# print("sayıların çarpımı:",çarpım)
# print("0 hariç kullanıcıdan alınan sayıların adedi",toplam)



# toplam=0
# adet=0
# while adet<5:
#     sayı=int(input("sayı:"))
#     if sayı>=0 and sayı<=100:
#         adet+=1
#         toplam+=sayı
# ortalama=toplam/5
# print(ortalama)



# a=int(input('a:'))
# b=int(input('b:'))
# yedek=a
# a=b
# b=yedek
# print('a:',a)
# print('b:',b)



# s1=1
# s2=1
# print(s1)
# print(s2)
# for i in range(3,8):
#     sonuç=s1+s2
#     print(i,".adım:",sonuç)
#     s1=s2
#     s2=sonuç



# Fibonacci dizisinin 7. adımına kadar olan elemanlarını yazdıran program

# fibonacci = [0, 1]  # Fibonacci dizisinin ilk iki elemanı

# for i in range(2, 7):
#     yeni_deger = fibonacci[-1] + fibonacci[-2]
#     fibonacci.append(yeni_deger)

# print("Fibonacci dizisinin 7. adımına kadar olan elemanları:", fibonacci)



# s1=1
# s2=1
# while True:
#     sonuc=s1+s2
#     if sonuc>1000:
#         print(s2)
#         break
#     s1=s2
#     s2=sonuc



# a, b = 0, 1  # Fibonacci dizisinin ilk iki terimi
# while b < 1000:  # 3 basamağa sahip sayıları kontrol etmek için 1000'den küçük olmalı
#     a, b = b, a + b  # Fibonacci dizisinin sonraki terimlerini hesapla
# print(a)  # 3 basamağa sahip en büyük değeri yazdır



# a,b=0,1
# while b<1000:
#     a,b=b,a+b
# print(a)



# sayı=1
# while sayı!=0:
#     sayı=int(input("sayı:"))
#     if sayı==0:
#      break
#     fakto=1
#     for i in range(1,sayı+1):
#        fakto=fakto*i
#     print(fakto)



# sayı=1
# toplam=0
# en_buyuk=None

# while sayı!=0:
#     sayı=int(input("sayı:"))
#     if sayı!=0:
#         toplam+=sayı
#         if en_buyuk is None or sayı>en_buyuk:
#             en_buyuk=sayı

# print("toplam:",toplam)
# print("en büyüu sayı:",en_buyuk)




# while True:
#     kullaniciadi=input("kullanıcı adınızı giriniz:")
#     sifre=input("şifrenizi giriniz:")
#     if kullaniciadi=="egemyo" and sifre=="1955":
#         print("Sisteme giriş yapıldı")
#         break
#     else:
#         print("yanlış şifre ve kullanıcı adı")



# hatalı_giriş=0
# while True:
#     kullaniciadi=input("kullanıcı adınızı giriniz:")
#     sifre=input("şifrenizi giriniz:")
#     if kullaniciadi=="egemyo" and sifre=="1955":
#         print("sisteme giriş yapıldı")
#         break
#     else:
#         hatalı_giriş+=1
#         print("yanlış şifre ve kullanıcı adı")

#         if hatalı_giriş==3:
#             print("deneme sınırı aşıldı")
#             break
      


# sayı=[1,2,3,4,5,6]
# sayı[0]="0"
# print(len(sayı))


# liste=[]
# for i in range(1,11):
#     liste.append(i)
# print(liste)



# liste=[]
# for i in range(1,11):
#     if i%2==0:
#         liste.append(i)
# print(liste)



# çiftler=list()
# for i in range(1,11):
#     if i%2==0:
#         çiftler.append(i)
# print(çiftler)



# m=["elma","armut","çilek"]
# tut=""
# for i in range(0,len(m),1):
#     tut+=m[i]
# print(tut)



# liste=[]
# for i in range(1,11):
#     liste.append(i)
# print(liste)


# çift=[]
# for i in range(1,11):
#     if i%2==0:
#         çift.append(i)
# print(çift)



# liste=["elma","armut","çilek"]
# liste2=[]
# for i in range(len(liste)-1,-1,-1):
#     liste2.append(liste[i])
# print(liste2)



# liste=[]
# for i in range(1,6):
#     sayı=int(input("sayı:"))
#     liste.append(sayı)
# print(liste)




# liste=[]
# toplam=0
# çarpım=1
# for i in range(1,7):
#     sayı=int(input("sayı:"))
#     liste.append(sayı)
#     toplam+=sayı
#     çarpım=çarpım*sayı
# ortalama=toplam/6
# print(liste,"toplam=",toplam,"çarpım:",çarpım,"ortlama=",ortalama)




# toplam=0
# başarılı=0
# başarısız=0
# notlar=[]
# for i in range(1,6):
#     ognot=int(input(str(i)+".öğrencinin notunu giriniz:"))
#     notlar.append(ognot)
#     toplam+=ognot
# ortalama=toplam/5
# for i in range(len(notlar)):
#     if notlar[i]>=ortalama:
#         başarılı+=1
#     else:
#         başarısız+=1
# print(başarılı,"Başarılı")
# print(başarısız,"Başarısız")




# liste=[]
# carp=1
# for i in range(6):
#     sayı=int(input(str(i)+".sayıyı giriniz:"))
#     liste.append(sayı)
# enb=max(liste)
# enk=min(liste)
# carp=enb*enk
# print("En büyük sayı:",enb)
# print("En küçük:",enk)
# print("Çarpımları:",carp)



# liste=[]
# for i in range(6):
#     sayı=int(input("sayı:"))
#     liste.append(sayı)
# enb=max(liste)
# adim=[]
# for i in range(6):
#     if liste[i]==enb:
#         adim.append(i+1)
# print("En büyük sayı:",enb)
# print("Bu sayı şu adımlarda girildi",adim)



# liste=[]
# while len(liste)<5:
#     sayi=int(input('Sayı:'))
#     if (sayi>=0) and (sayi<=100):
#         liste.append(sayi)
# for i in range(0,5,1):
#     print(liste[i])




# not_sayilari = [0] * 5  # 1'den 5'e kadar olan notlar için sayaç listesi

# # 10 öğrencinin notunu al
# for i in range(10):
#     while True:
#         try:
#             not_ = int(input(f"{i+1}. öğrencinin notunu giriniz (1-5): "))
#             if 1 <= not_ <= 5:  
#                 not_sayilari[not_ - 1] += 1  # Notu liste indeksine göre artır
#                 break
#             else:
#                 print("Lütfen 1 ile 5 arasında bir not giriniz!")
#         except ValueError:
#             print("Hatalı giriş! Lütfen sadece sayı giriniz.")

# # Sonuçları yazdır
# print("\nNot Dağılımı:")
# for i in range(5):
#     if not_sayilari[i] > 0:  # Sadece alınan notları yazdır
#         print(f"{i+1} alan öğrenci sayısı: {not_sayilari[i]}")





# Notlar=[0,0,0,0,0]
# for i in range(10):
#     ogrnot=int(input(str(i+1)+". notu giriniz"))
#     Notlar[ogrnot-1]=Notlar[ogrnot-1]+1
# for i in range(5):
#     if Notlar[i]!=0:
#         print(i+1,"notunu alan",Notlar[i],"kişi")





# a=[]
# b=[]
# c=[]
# for i in range(5):
#     sayı=int(input("sayı:"))
#     a.append(sayı)
 
#     k=int(input("k:"))
#     b.append(k)
# for i in range(5):
#     c.append(a[i]+b[i])
# print("c dizisi:",c)




# A=[]
# B=[]
# C=[]
# for i in range(10):
#     sayı=int(input("sayı:"))
#     A.append(sayı)
# kesme=int(input("Kesme değerini (1 ile 9 arasında)giriniz:"))
# B=A[:kesme]
# C=A[kesme:]
# print("B dizisi:",B)
# print("C dizisi:",C)



# a=[]
# b=[]
# c=[]
# for i in range(5):
#     sayı=int(input("sayı:"))
#     a.append(sayı)
#     sayı1=int(input("sayıgir:"))
#     b.append(sayı1)
# c=a+b
# print(c)


# sayı=0
# veri=[]
# while len(veri)<100:
#     sayı+=1
#     if sayı%3==0 and sayı%7==0:
#         veri.append(sayı)
# print(veri)




# sayı=2
# veri=[]
# while len(veri)<100:
#     asal=True
   
#     for i in range(2,int(sayı**0.5)+1):
#         if sayı%i==0:
#             asal=False
#             break
#     if asal:
#             veri.append(sayı)
#     sayı+=1
# for eleman in veri:
#      print(eleman)



# tek_liste=[]
# çift_liste=[]
# for i in range(5):
#     sayı=int(input("sayı:"))
#     if sayı%2==0:
#         çift_liste.append(sayı)
#     else:
#         tek_liste.append(sayı)
    
# print(tek_liste,"tek adet sayısı:",len(tek_liste))
# print(çift_liste," çift adet sayısı:",len(çift_liste))




# veri_listesi=set()
# while len(veri_listesi)<5:
#     sayı=int(input("sayı:"))
#     if sayı in veri_listesi:
#         print("bu sayı zaten eklenmiş")
#     else:
#         veri_listesi.add(sayı)
# print("tekrarsız liste:",list(veri_listesi))



# liste=["elma","armut","çilek"]
# for i in range(len(liste)):
#     print(liste[i])



# liste=["elma","armut","çilek"]
# for veri in liste:
#     print(veri)



# liste=["elma","armut","muz"]
# print("armut"in liste)
# print("kivi"in liste)



# liste=set()
# while len(liste)<10:
#         sayı=int(input("sayı:"))
#         if sayı in liste:
#             print("bu sayıyı girdiniz lütfen başka sayı giriniz")
#         else:
#             liste.add(sayı)
# print(liste)



# for i in range(1,21):
#     fakto=1
#     for j in range(1,i+1):
#         fakto=fakto*j
#     print(i,"!=",fakto,sep="\t")


# for i in range(2,101):
#     adet=0
#     for j in range(2,i):
#         if i%j==0:
#             adet+=1
#             break
#     if adet==0:
#         print(i)



# for i in range(5):
#     sayı=int(input("sayı:"))
#     adet=0
#     for j in range(2,sayı):
#         if sayı%j==0:
#             adet+=1
#             break
#     if adet==0:
#         print("asal")
#     else:
#         print("Asal değil")


# sayı=int(input("sayı:"))
# basamak=0
# while sayı>0:
#     sayı=sayı//10
#     basamak+=1
# print(basamak)




# sayı=int(input("sayı:"))
# z=1
# for i in range(1,sayı+1):
#     fakto=1
#     for j in range(1,i+1):
#         fakto=fakto*j
#     z*=i/fakto
# print(fakto)



# sayı=int(input("sayı:"))
# z=0
# for i in range(1,sayı+1):
#     pay=1
#     for j in range(1,i+1):
#         pay=pay*i
#     pay=pay+5*i

#     payda=1
#     for k in range(1,i+1):
#         payda=payda*k
#     payda-=8
#     z=z+(pay/payda)
# print(z)




# enb=-1
# enk=100
# for i in range(8):
#     sayı=int(input("sayı:"))
#     if sayı>enb:
#        enb=sayı
#     if sayı<enk:
#         enk=sayı
# print("En büyük sayı:",enb)
# print("En küçük sayı:",enk)




# toplam=0
# enb=-1
# enk=11
# for i in range(5):
#     sayı=int(input("sayı:"))
#     if sayı>enb:
#         enb=sayı
#     if sayı<enk:
#         enk=sayı
#     toplam+=sayı
# toplam=toplam-enb-enk
# ortalama=toplam/3
# print(ortalama)



# enb=-1
# for i in range(10):
#     sayı=int(input("sayı:"))
#     if sayı>enb:
#         enb=sayı
#         adet=0
#     if sayı==enb:
#         adet+=1
# print(adet)



# final=set()
# while len(final)<5:
#     sayı=int(input("sayı:"))
#     if sayı>1:
#         for i in range(2,sayı):
#             if sayı%i==0:
#                 break
#         else:
#             final.add(sayı)
# print(final)



 




