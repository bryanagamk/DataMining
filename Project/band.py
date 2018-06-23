import os, sys, json, cv2, imutils
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image

def clustering(feature,cluster,algoritma):
	npFeature = np.float32(feature)
	if algoritma == "kmeanspp":
		algo = cv2.KMEANS_PP_CENTERS
	else:
		algo = cv2.KMEANS_RANDOM_CENTERS

	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 1.0)
	ret, label, center = cv2.kmeans(npFeature, cluster, None, criteria, 200, algo)

	print("Label : ")
	print(label)
	print("Panjang Label : {}".format(len(label)))

	file = open("label.txt", "w")
	file.write(str(label))

	file.close()

	return label

def coloring(algoritma, labeledList32, cluster):
	color = [[255,0,0],[0,255,0],[0,0,255],[255,255,0],[0,255,255]]
	coloredLabeled = []
	for i in range(0, len(labeledList32)):
		tempLabel = []
		for j in range(0, len(labeledList32[0])):
			tempLabel.append(color[labeledList32[i][j]])
		coloredLabeled.append(tempLabel)

	# print(coloredLabeled)
	file = open("colored.txt", "w")
	file.write(str(coloredLabeled))

	file.close()

	img = np.asarray(coloredLabeled, dtype=np.uint8)
	cv2.imwrite("static/img/result/result"+algoritma+str(cluster)+".jpg", img)

	# cv2.imshow('image', np.array(coloredLabeled))
	# cv2.waitKey(0)

def createFeature(algoritma, cluster):
	directory = "static/img"
	extension = "jpg"
	feature = []
	count = 1
	for filename in os.listdir(directory):		
		if os.path.splitext(filename)[1] == ".jpg":
			pathfilename = directory + "/" + filename
			fname = os.path.splitext(filename)[0]

			img =  cv2.imread(pathfilename)
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

			tempList = []

			print("PROCESS : Generating Feature Band {}".format(count))
			for i in range(img.shape[0]):
				for j in range(img.shape[1]):
					tempList.append(img[i][j][0])

			print("SUCCESS : Band {} Generated".format(count))
			print("PROCESS : Atempting to append to feature list")
			feature.append(tempList)
		count += 1

	transposeList = np.array(feature).T.tolist()
	file = open("dataFitur.txt", "w")
	file.write(str(transposeList))

	file.close()

	labeledList = clustering(transposeList,cluster, algoritma)
	labeledList = np.array(labeledList)
	labeledList32 = np.reshape(labeledList, (32,32))

	coloring(algoritma, labeledList32, cluster)