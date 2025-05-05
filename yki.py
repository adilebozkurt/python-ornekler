import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QLabel, QPushButton, QGroupBox, 
                           QLCDNumber, QComboBox)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QImage
import random

class GroundControlStation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("İnsansız Kara Aracı Yer Kontrol İstasyonu")
        self.setGeometry(100, 100, 1200, 800)
        
        # Ana widget ve layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout(main_widget)
        
        # Sol panel - Harita ve kamera görüntüsü
        left_panel = QVBoxLayout()
        
        # Harita alanı
        map_group = QGroupBox("Harita")
        map_layout = QVBoxLayout()
        self.map_label = QLabel()
        self.map_label.setFixedSize(600, 400)
        self.map_label.setStyleSheet("background-color: #2c3e50;")
        map_layout.addWidget(self.map_label)
        map_group.setLayout(map_layout)
        left_panel.addWidget(map_group)
        
        # Kamera görüntüsü
        camera_group = QGroupBox("Kamera Görüntüsü")
        camera_layout = QVBoxLayout()
        self.camera_label = QLabel()
        self.camera_label.setFixedSize(600, 300)
        self.camera_label.setStyleSheet("background-color: #34495e;")
        camera_layout.addWidget(self.camera_label)
        camera_group.setLayout(camera_layout)
        left_panel.addWidget(camera_group)
        
        # Sağ panel - Kontrol ve durum bilgileri
        right_panel = QVBoxLayout()
        
        # Durum bilgileri
        status_group = QGroupBox("Araç Durumu")
        status_layout = QVBoxLayout()
        
        # Hız göstergesi
        speed_layout = QHBoxLayout()
        speed_layout.addWidget(QLabel("Hız:"))
        self.speed_lcd = QLCDNumber()
        self.speed_lcd.setDigitCount(3)
        speed_layout.addWidget(self.speed_lcd)
        speed_layout.addWidget(QLabel("km/s"))
        status_layout.addLayout(speed_layout)
        
        # Batarya durumu
        battery_layout = QHBoxLayout()
        battery_layout.addWidget(QLabel("Batarya:"))
        self.battery_lcd = QLCDNumber()
        self.battery_lcd.setDigitCount(3)
        battery_layout.addWidget(self.battery_lcd)
        battery_layout.addWidget(QLabel("%"))
        status_layout.addLayout(battery_layout)
        
        # GPS durumu
        gps_layout = QHBoxLayout()
        gps_layout.addWidget(QLabel("GPS:"))
        self.gps_status = QLabel("Bağlı")
        self.gps_status.setStyleSheet("color: green;")
        gps_layout.addWidget(self.gps_status)
        status_layout.addLayout(gps_layout)
        
        status_group.setLayout(status_layout)
        right_panel.addWidget(status_group)
        
        # Kontrol paneli
        control_group = QGroupBox("Kontrol")
        control_layout = QVBoxLayout()
        
        # Mod seçimi
        mode_layout = QHBoxLayout()
        mode_layout.addWidget(QLabel("Mod:"))
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["Manuel", "Otonom", "Yarı-Otonom"])
        mode_layout.addWidget(self.mode_combo)
        control_layout.addLayout(mode_layout)
        
        # Kontrol butonları
        button_layout = QVBoxLayout()
        
        # İleri/Geri kontrolü
        forward_back_layout = QHBoxLayout()
        self.backward_btn = QPushButton("Geri")
        self.forward_btn = QPushButton("İleri")
        forward_back_layout.addWidget(self.backward_btn)
        forward_back_layout.addWidget(self.forward_btn)
        button_layout.addLayout(forward_back_layout)
        
        # Sol/Sağ kontrolü
        left_right_layout = QHBoxLayout()
        self.left_btn = QPushButton("Sol")
        self.right_btn = QPushButton("Sağ")
        left_right_layout.addWidget(self.left_btn)
        left_right_layout.addWidget(self.right_btn)
        button_layout.addLayout(left_right_layout)
        
        # Durma butonu
        self.stop_btn = QPushButton("DUR")
        self.stop_btn.setStyleSheet("background-color: red; color: white;")
        button_layout.addWidget(self.stop_btn)
        
        control_layout.addLayout(button_layout)
        control_group.setLayout(control_layout)
        right_panel.addWidget(control_group)
        
        # Layout'ları ana layout'a ekle
        layout.addLayout(left_panel, 2)
        layout.addLayout(right_panel, 1)
        
        # Timer for updating status
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_status)
        self.timer.start(1000)  # Update every second
        
    def update_status(self):
        # Simulate random values for demonstration
        self.speed_lcd.display(random.randint(0, 100))
        self.battery_lcd.display(random.randint(20, 100))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GroundControlStation()
    window.show()
    sys.exit(app.exec_()) 
    