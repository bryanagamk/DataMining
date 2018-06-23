# TODO : 0 buat GUI template
# TODO : 1 Ambil data Image, nilai fitur image warna tiap pixel
# TODO : 2 cari lokasi pixel yang sama
# TODO : 3 gabungkan lokasi-lokasi pixel yang sama menjadi pixel kombinasi
# TODO : 4 taruh di feature space untuk clustering
# TODO : 5 lakukan clustering
# TODO : 6 coloring cluster
# TODO : 7 output gambar baru

import sys
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Multiband.multibandProses import Agregasi
from Multiband.multiband_kmeans import main
import random
import string

def result():
    res = main()
    rand = ''.join([random.choice(string.digits) for n in range(12)])
    imagePath = "result.jpg"
    res.save(imagePath)


def hierarchichal():
    cluster = 4
    paths = []
    paths[0] = paths.append("../DataSource/multiband_data/gb1.GIF")

    paths[1] = paths.append("../DataSource/multiband_data/gb2.GIF")

    paths[2] = paths.append("../DataSource/multiband_data/gb3.GIF")

    paths[3] = paths.append("../DataSource/multiband_data/gb4.GIF")

    paths[4] = paths.append("../DataSource/multiband_data/gb5.GIF")

    paths[5] = paths.append("../DataSource/multiband_data/gb7.GIF")

    # res = Agregasi.band(self)
    rand = ''.join([random.choice(string.digits) for n in range(12)])
    imagePath = "resultHierarchical.jpg"
    # res.save(imagePath)


def loop(img):
    pixmap = QPixmap(img)
    # Convert QPixmap to QImage
    image = QPixmap.toImage(pixmap)
    image_width = image.width
    image_height = image.height
    arr_gray = []
    arr_index = []

    for x in range(image_width):
        for y in range(image_height):
            qrgb = image.pixel(x, y)
            gray = qGray(qRed(qrgb), qGreen(qrgb), qBlue(qrgb))
            arr_gray += [gray]
            arr_index += [(x, y)]

    return arr_gray, arr_index

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
        self.button_run.clicked.connect(self.resultFinal)
        vbox.addWidget(self.button_run)

        # Label Final Image
        self.label_final = QLabel("Final Image")
        vbox.addWidget(self.label_final)

        vbox.addStretch()
        self.setLayout(vbox)

    def showResult(self):
        cluster = 4

        arr_temp = np.array([])

        img1 = "../DataSource/multiband_data/gb1.GIF"
        arr_temp = np.append(img1)
        img2 = "../DataSource/multiband_data/gb2.GIF"
        arr_temp = np.append(img2)
        img3 = "../DataSource/multiband_data/gb3.GIF"
        arr_temp = np.append(img3)
        img4 = "../DataSource/multiband_data/gb4.GIF"
        arr_temp = np.append(img4)
        img5 = "../DataSource/multiband_data/gb5.GIF"
        arr_temp = np.append(img5)
        img7 = "../DataSource/multiband_data/gb7.GIF"
        arr_temp = np.append(img7)


    def resultFinal(self):
        fname = "result"
        pixmap = QPixmap(fname)
        self.label_final.setPixmap(pixmap)


    def showDialog(self, button_id):
        # Open the file dialog to select an image file.
        fname, _ = QFileDialog.getOpenFileName(self, "Open File", "../DataSource/multiband_data/gb1.GIF", "JPEG (*.JPEG *.jpeg *.JPG *.jpg *.JPE *.jpe *JFIF *.jfif);; PNG (*.PNG *.png);; GIF (*.GIF *.gif);; Bitmap Files (*.BMP *.bmp *.DIB *.dib);; TIFF (*.TIF *.tif *.TIFF *.tiff);; ICO (*.ICO *.ico)")
        pixmap = QPixmap(fname)

        self.arr_temp = np.array([])
        arr_gray_1 = []
        arr_gray_2 = []
        arr_gray_3 = []
        arr_gray_4 = []
        arr_gray_5 = []
        arr_gray_6 = []

        if button_id == 1:
            self.label1.setPixmap(pixmap)


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
                    # print("({},{}) = {}".format(x, y, gray))

            temp = str(arr_gray_1)
            data = temp[1:len(arr_gray_1)-1]
            fo = open("band1.txt", "w")
            fo.write(data)
            fo.close()



        elif button_id == 2:
            self.label2.setPixmap(pixmap)

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
                    # print("({},{}) = {}".format(x, y, gray))

            temp = str(arr_gray_2)
            data = temp[1:len(arr_gray_2) - 1]
            fo = open("band2.txt", "w")
            fo.write(data)
            fo.close()

        elif button_id == 3:
            self.label3.setPixmap(pixmap)

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
                    # print("({},{}) = {}".format(x, y, gray))

            temp = str(arr_gray_3)
            data = temp[1:len(arr_gray_3) - 1]
            fo = open("band3.txt", "w")
            fo.write(data)
            fo.close()

        elif button_id == 4:
            self.label4.setPixmap(pixmap)

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
                    # print("({},{}) = {}".format(x, y, gray))

            temp = str(arr_gray_4)
            data = temp[1:len(arr_gray_4) - 1]
            fo = open("band4.txt", "w")
            fo.write(data)
            fo.close()

        elif button_id == 5:
            self.label5.setPixmap(pixmap)

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
                    # print("({},{}) = {}".format(x, y, gray))

            temp = str(arr_gray_5)
            data = temp[1:len(arr_gray_5) - 1]
            fo = open("band5.txt", "w")
            fo.write(data)
            fo.close()

        elif button_id == 6:
            self.label6.setPixmap(pixmap)

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
                    # print("({},{}) = {}".format(x, y, gray))

            temp = str(arr_gray_6)
            data = temp[1:len(arr_gray_6) - 1]
            fo = open("band6.txt", "w")
            fo.write(data)
            fo.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    # hierarchichal()
    result()
    application = App()
    application.show()
    app.exec()
    # sys.exit(app.exec())