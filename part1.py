import sys
import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from style import Ui_MainWindow


class Maps(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_map)

    def open_map(self):
        self.lat = self.lineEdit.text()
        self.long = self.lineEdit_2.text()
        self.scale = self.lineEdit_3.text()
        map_request = 'https://static-maps.yandex.ru/1.x/?ll=' + self.long + ',' + self.lat
        map_request += '&z=' + self.scale + '&size=450,450&l=map'
        response = requests.get(map_request)

        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)

        self.pixmap = QPixmap(self.map_file)
        self.label_4.setPixmap(self.pixmap)

app = QApplication(sys.argv)
maps = Maps()
maps.show()
sys.exit(app.exec_())
