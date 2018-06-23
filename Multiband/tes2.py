import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel,
    QHBoxLayout, QVBoxLayout, QApplication, QFileDialog)
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def showDialog(self):
        # Open the file dialog to select an image file.
        fname, _ = QFileDialog.getOpenFileName(self, "Open File", "", "JPEG (*.JPEG *.jpeg *.JPG *.jpg *.JPE *.jpe *JFIF *.jfif);; PNG (*.PNG *.png);; GIF (*.GIF *.gif);; Bitmap Files (*.BMP *.bmp *.DIB *.dib);; TIFF (*.TIF *.tif *.TIFF *.tiff);; ICO (*.ICO *.ico)")
        self.label1 = QLabel("Image 1")
        self.label1.setPixmap(QPixmap(fname))

    def initUI(self):
        button1 = QPushButton("Load Image 1")

        button2 = QPushButton("Load Image 2")
        button3 = QPushButton("Load Image 3")
        button4 = QPushButton("Load Image 4")
        button5 = QPushButton("Load Image 5")
        button6 = QPushButton("Load Image 6")

        label1 = QLabel("Image 1")
        label2 = QLabel("Image 2")
        label3 = QLabel("Image 3")
        label4 = QLabel("Image 4")
        label5 = QLabel("Image 5")
        label6 = QLabel("Image 6")

        button1.clicked.connect(self.showDialog)

        hbox_btn = QHBoxLayout()
        hbox_btn.addStretch(1)
        hbox_btn.addWidget(button1)
        hbox_btn.addWidget(button2)
        hbox_btn.addWidget(button3)
        hbox_btn.addWidget(button4)
        hbox_btn.addWidget(button5)
        hbox_btn.addWidget(button6)

        hbox_label = QHBoxLayout()
        hbox_label.addStretch(1)
        hbox_label.addWidget(label1)
        hbox_label.addWidget(label2)
        hbox_label.addWidget(label3)
        hbox_label.addWidget(label4)
        hbox_label.addWidget(label5)
        hbox_label.addWidget(label6)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox_btn)
        vbox.addLayout(hbox_label)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())