# renkler=["kırmızı","mavi","yeşil","sarı"]
# print("ilk renk:",renkler[0])
# print("son renk:",renkler[-1])
# print("toplam renk:",len(renkler))
# for i in range(len(renkler)-1,-1,-1):
#     print(renkler[i])


# lastlist=["a","b",["c","d","e"],"f"]
# print(lastlist[2][1])



# print("Sipariş takip sistemine hoş geldiniz.")
# print("çıkmak için 'q' yazın.\n")
# siparişler={}
# while True:
#     urun=input("ürün girin:")
#     if urun=="q":
#         break
#     if urun in siparişler:
#         siparişler[urun]+=1
#     else:
#         siparişler[urun]=1
# print("\nsipariş özeti:")
# for urun, adet in siparişler.items():
#     print(f"{urun}: {adet} adet")
# print("sipariş takip sisteminden çıkıldı.")
         

print("market sipariş sistemine hoş geldiniz")
print("çıkmak için 'q'tuşuna basınız")
siparişler={}
while True:
    urun=input("ürün giriniz:")
    if urun=="q":
        break
    if urun in siparişler:
        siparişler[urun]+=1
    else:
        siparişler[urun]=1
print("\nsipariş özeti:")
for urun, adet in siparişler.items():
    print(f"{urun}: {adet} adet")
print("sipariş takip sisteminden çıkıldı.")
    
