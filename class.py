#class
# class Class1:
#     str = "text"
#     num = 10

#     def print_text(self):
#         print(self.str)


# class Car:
#     def __init__(self, name, type, engine, hp):
#         self.name = name
#         self.type = type
#         self.engine = engine
#         self.hp = hp

# car_1 = Car("BMW", "Sedan", "2.0", 190)




# class kişi:
#     def __init__(self, isim, yas):
#         self.isim = isim
#         self.yas = yas

#     def yazdır(self):
#         print("Merhaba, adım", self.isim, "ve ben", self.yas, "yaşındayım.")

# p1 = kişi("Yiğit", 23)
# p1.yazdır()





# class kişi:
#     def __init__(self, isim, yas):
#         self.isim = isim
#         self.yas = yas

#     def yazdır(self):
#         print("Merhaba, adım", self.isim, "ve ben", self.yas, "yaşındayım.")

# p1 = kişi(input("Adınızı giriniz: "), int(input("Yaşınızı giriniz: ")))
# p1.yazdır()





# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def getX(self):
#         return self.x
#     def getY(self):
#         return self.y
 
# pointA = Point(3, 4)
# x = pointA.getX()
# y = pointA.getY()
# print("("+str(x)+","+str(y)+")")






# import math
# class Point:
#     def __init__(self, x, y):
#         self.xCoord = x
#         self.yCoord = y
#     def getX(self):
#         return self.xCoord
#     def getY(self):
#         return self.yCoord
#     def shift(self, xInc, yInc):
#         self.xCoord += xInc
#         self.yCoord += yInc
    
#     def distance(self, otherPoint):
#         xDiff = self.xCoord - otherPoint.getX()
#         yDiff = self.yCoord - otherPoint.getY()
#         return math.sqrt((xDiff**2 + yDiff**2))
    
# #main route
# pointA = Point(5,7)
# pointB = Point(0,0)

# x=pointA.getX()
# y=pointA.getY()
# print("A("+str(x)+","+str(y)+")")


# pointA.shift(2,17)
# x=pointA.getX()
# y=pointA.getY()
# print("Yeni A("+str(x)+","+str(y)+")")

# d=pointA.distance(pointB)
# print('A-B arası mesafe:',d)













# import tkinter as tk

# def start_connection():
#     status_label.config(text="Bağlantı Başlatıldı", fg="green")

# def stop_connection():
#     status_label.config(text="Bağlantı Durduruldu", fg="red")

# root = tk.Tk()
# root.title("YKI Arayüzü")
# root.geometry("300x200")

# status_label = tk.Label(root, text="Bağlantı Durumu: Kapalı", fg="gray")
# status_label.pack(pady=10)

# start_btn = tk.Button(root, text="Bağlantıyı Başlat", command=start_connection)
# start_btn.pack(pady=5)

# stop_btn = tk.Button(root, text="Bağlantıyı Durdur", command=stop_connection)
# stop_btn.pack(pady=5)

# root.mainloop()




# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import String

# class YKI_GUI_Publisher(Node):

#     def __init__(self):
#         super().__init__('yki_gui_publisher')
#         self.publisher_ = self.create_publisher(String, 'yki_baglanti', 10)

#     def send_connection_signal(self, signal):
#         msg = String()
#         msg.data = signal
#         self.publisher_.publish(msg)
#         self.get_logger().info(f'Gönderilen mesaj: "{msg.data}"')

# def main(args=None):
#     rclpy.init(args=args)
#     node = YKI_GUI_Publisher()
#     node.send_connection_signal("BAŞLAT")
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()


# start_btn = tk.Button(root, text="Bağlantıyı Başlat", command=lambda: yki_node.send_connection_signal("BAŞLAT"))




#####################################################################################################3
                                    #6.05.2025 dersi#
# veri modeli 
# 1-linked list, 
#2-kuyruk
#          } limked list ifade edilir
#3-yığın
#4-tree


# ağaçlar(trees):
# dallanmalar, bi durumdan bi kaç tane durum çıkabilir
# her ağaç yapısını liste metodu olarak gösterebiliriz
#Tanımlar:
#1-düğüm: ağaç yapısının en üstünde bulunan düğüm
#2-kök: ağaç yapısının en üstünde bulunan düğüm
#3-dal(çocuk): ağaç yapısının en üstünde bulunan düğümden aşağıya doğru giden kısımlar
#4-yaprak: ağaç yapısının en altında bulunan düğümler
#5-yükseklik: ağaç yapısının en üstünden en altına kadar olan kısım
#parent: ağaç yapısının en üstünde bulunan düğümden aşağıya doğru giden kısımlar
#child: ağaç yapısının en üstünde bulunan düğümden aşağıya doğru giden kısımlar     
#sibling: ağaç yapısının en üstünde bulunan düğümden aşağıya doğru giden kısımlar
#root: ağaç yapısının en üstünde bulunan düğüm      
#leaf: ağaç yapısının en altında bulunan düğümler
#height: ağaç yapısının en üstünden en altına kadar olan kısım
#depth of three:bir düğümün kök düğümüne olan uzaklığıdır
#height of three:bir düğümün en altındaki yaprak düğüme olan uzaklığıdırance
#ancestor(ata:):bir düğümün parentı birinci ancestordur. parent'ın parent'ı ikinci ancestordur.kök kendi haricindeki tüm düğümlerin ancestor'ıdır.
#descendant:bir düğümün child'ı birinci descendant'dır. child'ın child'ı ikinci descendant'dır. yaprak kendi haricindeki tüm düğümlerin descendant'ıdır.
#ikili ağaç yapısı(Binary tree):her düğümün en fazla iki çocuğu vardır. bu çocuklar sol ve sağ çocuk olarak adlandırılır.
##sonlu  düğümler kümesidir,kök olarak adlandırılan özel bir düğüm vardır, her düğüm 
#full binary tree:her düğümün iki çocuğu vardır. bu çocuklar sol ve sağ çocuk olarak adlandırılır.
#complete binary tree:soldan sağa doğru düğümler eklendiğinde oluşan ağaçlara Complete binary tree denir. bu ağaçlarda yapraklar en altta ve en soldadır.
# general tree:her düğümün en az iki çocupu olabilme sınırı olmayan ağaçlardır 
#ikili arama ağacı:Boş olan veya her düğümü aşağıdaki şartlara uyan anahtara sahip ikili ağaçlara binari search tree denir.
###1-elemanlar (düğüm) kökünden büyük ve eşitse sağa, küçük ise sola doğru yerleştirilen ağaç türüdür.
#sıanv sorusu 


#ödev:
#full binary tree de n tane yaprak varsa bu ağaçta toplam 2n-1 tane düğüm vardır. 





#her düğümü ve ayrıtları olan küme ağaç değildir.bir çizgenin ağaç olması için her iki düğüm arasında sadece bir yol olmalıdır., devre (cycle,çevrim) olmamalıdır.


#### Ağaç Türleri ####
#kodlama ağacı(coding tree)=
#sözlük ağacı=
#  
