import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Multiband Image Clustering')
        self.setGeometry(50, 50, 640, 480)

        hbox_btn = QHBoxLayout()
        hbox_label = QHBoxLayout()
        vbox = QVBoxLayout()

        # Button Load Image 1
        self.button1 = QPushButton("Load Image 1")
        self.button1.clicked.connect(lambda: self.showDialog(1))
        hbox_btn.addWidget(self.button1)

        # Label Image 1
        self.label1 = QLabel("Image 1")
        hbox_label.addWidget(self.label1)

        # Button Load Image 2
        self.button2 = QPushButton("Load Image 2")
        self.button2.clicked.connect(lambda: self.showDialog(2))
        hbox_btn.addWidget(self.button2)

        # Label Image 2
        self.label2 = QLabel("Image 2")
        hbox_label.addWidget(self.label2)

        # Button Load Image 3
        self.button3 = QPushButton("Load Image 3")
        self.button3.clicked.connect(lambda: self.showDialog(3))
        hbox_btn.addWidget(self.button3)

        # Label Image 3
        self.label3 = QLabel("Image 3")
        hbox_label.addWidget(self.label3)

        # Button Load Image 4
        self.button4 = QPushButton("Load Image 4")
        self.button4.clicked.connect(lambda: self.showDialog(4))
        hbox_btn.addWidget(self.button4)

        # Label Image 4
        self.label4 = QLabel("Image 4")
        hbox_label.addWidget(self.label4)

        # Button Load Image 5
        self.button5 = QPushButton("Load Image 5")
        self.button5.clicked.connect(lambda: self.showDialog(5))
        hbox_btn.addWidget(self.button5)

        # Label Image 5
        self.label5 = QLabel("Image 5")
        hbox_label.addWidget(self.label5)

        # Button Load Image 6
        self.button6 = QPushButton("Load Image 6")
        self.button6.clicked.connect(lambda: self.showDialog(6))
        hbox_btn.addWidget(self.button6)

        # Label Image 6
        self.label6 = QLabel("Image 6")
        hbox_label.addWidget(self.label6)

        vbox.addLayout(hbox_btn)
        vbox.addLayout(hbox_label)

        # Button Run
        self.button_run = QPushButton("Run")
        # self.button_run.clicked.connect()
        vbox.addWidget(self.button_run)

        # Label Final Image
        self.label_final = QLabel("Final Image")
        vbox.addWidget(self.label_final)

        vbox.addStretch()
        self.setLayout(vbox)

    def showDialog(self, button_id):
        # Open the file dialog to select an image file.
        fname, _ = QFileDialog.getOpenFileName(self, "Open File", "../Multiband Data/gb1.GIF", "JPEG (*.JPEG *.jpeg *.JPG *.jpg *.JPE *.jpe *JFIF *.jfif);; PNG (*.PNG *.png);; GIF (*.GIF *.gif);; Bitmap Files (*.BMP *.bmp *.DIB *.dib);; TIFF (*.TIF *.tif *.TIFF *.tiff);; ICO (*.ICO *.ico)")
        pixmap = QPixmap(fname)

        if button_id == 1:
            self.label1.setPixmap(pixmap)

            arr_gray_1 = []
            arr_index_1 = []

            # Convert QPixmap to QImage
            image = QPixmap.toImage(pixmap)

            # Obtain image size
            image_width = image.width()
            image_height = image.height()

            print('Gambar 1')
            for x in range(image_width):
                for y in range(image_height):
                    qrgb = image.pixel(x, y)
                    gray = qGray(qRed(qrgb), qGreen(qrgb), qBlue(qrgb))
                    arr_gray_1 += [gray]
                    arr_index_1 += [(x, y)]
                    print("({},{}) = {}".format(x, y, gray))

        elif button_id == 2:
            self.label2.setPixmap(pixmap)

            arr_gray_2 = []
            arr_index_2 = []

            # Convert QPixmap to QImage
            image = QPixmap.toImage(pixmap)

            # Obtain image size
            image_width = image.width()
            image_height = image.height()

            print('Gambar 2')
            for x in range(image_width):
                for y in range(image_height):
                    qrgb = image.pixel(x, y)
                    gray = qGray(qRed(qrgb), qGreen(qrgb), qBlue(qrgb))
                    arr_gray_2 += [gray]
                    arr_index_2 += [(x, y)]
                    print("({},{}) = {}".format(x, y, gray))

        elif button_id == 3:
            self.label3.setPixmap(pixmap)

            arr_gray_3 = []
            arr_index_3 = []

            # Convert QPixmap to QImage
            image = QPixmap.toImage(pixmap)

            # Obtain image size
            image_width = image.width()
            image_height = image.height()

            print('Gambar 3')
            for x in range(image_width):
                for y in range(image_height):
                    qrgb = image.pixel(x, y)
                    gray = qGray(qRed(qrgb), qGreen(qrgb), qBlue(qrgb))
                    arr_gray_3 += [gray]
                    arr_index_3 += [(x, y)]
                    print("({},{}) = {}".format(x, y, gray))

        elif button_id == 4:
            self.label4.setPixmap(pixmap)

            arr_gray_4 = []
            arr_index_4 = []

            # Convert QPixmap to QImage
            image = QPixmap.toImage(pixmap)

            # Obtain image size
            image_width = image.width()
            image_height = image.height()

            print('Gambar 4')
            for x in range(image_width):
                for y in range(image_height):
                    qrgb = image.pixel(x, y)
                    gray = qGray(qRed(qrgb), qGreen(qrgb), qBlue(qrgb))
                    arr_gray_4 += [gray]
                    arr_index_4 += [(x, y)]
                    print("({},{}) = {}".format(x, y, gray))

        elif button_id == 5:
            self.label5.setPixmap(pixmap)

            arr_gray_5 = []
            arr_index_5 = []

            # Convert QPixmap to QImage
            image = QPixmap.toImage(pixmap)

            # Obtain image size
            image_width = image.width()
            image_height = image.height()

            print('Gambar 5')
            for x in range(image_width):
                for y in range(image_height):
                    qrgb = image.pixel(x, y)
                    gray = qGray(qRed(qrgb), qGreen(qrgb), qBlue(qrgb))
                    arr_gray_5 += [gray]
                    arr_index_5 += [(x, y)]
                    print("({},{}) = {}".format(x, y, gray))

        elif button_id == 6:
            self.label6.setPixmap(pixmap)

            arr_gray_6 = []
            arr_index_6 = []

            # Convert QPixmap to QImage
            image = QPixmap.toImage(pixmap)

            # Obtain image size
            image_width = image.width()
            image_height = image.height()

            print('Gambar 6')
            for x in range(image_width):
                for y in range(image_height):
                    qrgb = image.pixel(x, y)
                    gray = qGray(qRed(qrgb), qGreen(qrgb), qBlue(qrgb))
                    arr_gray_6 += [gray]
                    arr_index_6 += [(x, y)]
                    print("({},{}) = {}".format(x, y, gray))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = App()
    application.show()
    sys.exit(app.exec())