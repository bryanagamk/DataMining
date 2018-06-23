import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy
from PIL import Image

# Fungsi untuk menghitung jarak euclidean
def euclidean_distance(data, centroids):
	row, col = np.shape(data)
	c_row, c_col = np.shape(centroids)
	distances = np.zeros((row, c_row))

	for x in range(row):
		dist_arr = []
		for c in centroids:
			dist = 0
			for i in range(len(c)):
				dist += pow((data[x][i] - c[i]), 2)
			dist_arr.append(np.sqrt(dist))
		distances[x] = dist_arr

	return distances

# fungsi untuk generate centroid
def generate_centroid(data, n_clusters):
	row, col = np.shape(data)
	centroids = np.zeros((n_clusters, col))
	for i in range(n_clusters):
		for j in range(col):
			centroids[i][j] = np.random.uniform(np.min(data[:, j]), np.max(data[:, j]))

	return centroids

def main():
	#image load
	im1 = Image.open('../DataSource/multiband_data/gb1.GIF', 'r')
	pic1 = im1.load()
	im2 = Image.open('../DataSource/multiband_data/gb2.GIF', 'r')
	pic2 = im1.load()
	im3 = Image.open('../DataSource/multiband_data/gb3.GIF', 'r')
	pic3 = im1.load()
	im4 = Image.open('../DataSource/multiband_data/gb4.GIF', 'r')
	pic4 = im1.load()
	im5 = Image.open('../DataSource/multiband_data/gb5.GIF', 'r')
	pic5 = im1.load()
	im6 = Image.open('../DataSource/multiband_data/gb7.GIF', 'r')
	pic6 = im1.load()

	width, height = im1.size
	pixel_img1 = list(im1.getdata())
	pixel_img2 = list(im2.getdata())
	pixel_img3 = list(im3.getdata())
	pixel_img4 = list(im4.getdata())
	pixel_img5 = list(im5.getdata())
	pixel_img6 = list(im6.getdata())

	data = np.array([list(a) for a in zip(pixel_img1, pixel_img2, pixel_img3, pixel_img4, pixel_img5, pixel_img6)])
	k = 5
	C = generate_centroid(data, k)

	# print("Generated centroids")
	# print("=========================")
	# print(C, "\n")

	# inisialisasi clusters dan centroid lama
	old_C = np.zeros(C.shape)
	clusters = np.zeros(len(data))

	# lakukan perulangan untuk mengkomputasi K-Means
	while True:
		# hitung jarak data dengan centroid
		D = euclidean_distance(data, C)
		# dapatkan tiap cluster data
		clusters = np.argmin(D, axis=1)


		# salin centroid ke centroid lama
		old_C = deepcopy(C)

		# hitung ulang centroid baru dengan menghitung rata-rata dari data tiap cluster
		for i in range(k):
			points = [data[j] for j in range(len(data)) if clusters[j] == i]


			# jika ada cluster yang kosong maka lanjutkan proses karena menghasilkan NaN jika diteruskan
			if len(points) == 0:
				continue
			C[i] = np.mean(points, axis=0)

		# jika sudah konvergen maka hentikan perulangan
		if np.array_equal(C, old_C):
			break



	new_cluster = np.zeros([len(clusters), 3])
	warna = np.array([(0,0,255), (0,0,128), (150,75,0), (255,215,0), (0,255,0), (255,0,255), (255,0,0), (128,0,0), (255,192,203), (128,128,128)])
	for i in range(k):
		for x in range(len(clusters)):
			if clusters[x] == i:
				new_cluster[x]= warna[i]

	new_cluster = new_cluster.astype(int)
	new_cluster = tuple(map(tuple, new_cluster))


	img = Image.new('RGB', (width,height), "black") # create a new black image
	pixels = img.load() # create the pixel map

	x = 0
	for i in range(img.size[0]):    # for every col:
		for j in range(img.size[1]):    # For every row 
			pixels[i,j] = new_cluster[x]# set the colour accordingly
			x+=1

	# img.show()
	return img

if __name__ == "__main__":
	main()
