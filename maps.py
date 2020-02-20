import sys
import requests
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from style import Ui_MainWindow


class Maps(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_map)

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_PageUp:
            self.scale_up()
        if key == QtCore.Qt.Key_PageDown:
            self.scale_down()

    def scale_down(self):
        if self.scale > 0:
            self.lineEdit_3.setText(str(int(self.scale) - 1))
            self.scale -= 1
            self.open_map()

    def scale_up(self):
        if self.scale < 17:
            self.lineEdit_3.setText(str(int(self.scale) + 1))
            self.scale += 1
            self.open_map()

    def open_map(self):
        self.lat = float(self.lineEdit.text())
        self.long = float(self.lineEdit_2.text())
        self.scale = int(self.lineEdit_3.text())
        map_request = 'https://static-maps.yandex.ru/1.x/?ll=' + str(self.long) + ',' + str(self.lat)
        map_request += '&z=' + str(self.scale) + '&size=600,450&l=map'
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
