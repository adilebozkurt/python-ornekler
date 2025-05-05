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













import tkinter as tk

def start_connection():
    status_label.config(text="Bağlantı Başlatıldı", fg="green")

def stop_connection():
    status_label.config(text="Bağlantı Durduruldu", fg="red")

root = tk.Tk()
root.title("YKI Arayüzü")
root.geometry("300x200")

status_label = tk.Label(root, text="Bağlantı Durumu: Kapalı", fg="gray")
status_label.pack(pady=10)

start_btn = tk.Button(root, text="Bağlantıyı Başlat", command=start_connection)
start_btn.pack(pady=5)

stop_btn = tk.Button(root, text="Bağlantıyı Durdur", command=stop_connection)
stop_btn.pack(pady=5)

root.mainloop()




import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class YKI_GUI_Publisher(Node):

    def __init__(self):
        super().__init__('yki_gui_publisher')
        self.publisher_ = self.create_publisher(String, 'yki_baglanti', 10)

    def send_connection_signal(self, signal):
        msg = String()
        msg.data = signal
        self.publisher_.publish(msg)
        self.get_logger().info(f'Gönderilen mesaj: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = YKI_GUI_Publisher()
    node.send_connection_signal("BAŞLAT")
    rclpy.shutdown()

if __name__ == '__main__':
    main()


start_btn = tk.Button(root, text="Bağlantıyı Başlat", command=lambda: yki_node.send_connection_signal("BAŞLAT"))





 