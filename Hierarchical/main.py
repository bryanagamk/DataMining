#
# TODO: 1 Ambil data
# TODO: 2 Hitung jarak euclidian
# TODO: 3 Gabungkan 2 Kelompok dengan selisih jarak terdekat
# TODO: 4 ulangi langkah 2 & 3
# TODO: 5 lakukan cluster analysis
#

import pandas as pd
import numpy as np
from copy import deepcopy

# Fungsi untuk mendapatkan centroid
def get_centroid(data):
    if data.ndim > 1:
        return np.mean(data, axis=0)
    else:
        return data

# Fungsi untuk menghitung jarak euclidean
def euclidean_distance(data, data2):
    dist = 0
    for i in range(len(data)):
        dist += pow((data[i] - data2[i]), 2)

    return np.sqrt(dist)


def loadDataset():
    # load dataset
    df = pd.read_csv("iris.csv")
    df['species'] = df['species'].astype('category')
    data = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values
    labels = df['species'].cat.codes.values

    return data, labels


def clustering(len_clusters, clusters, k):
    iter = 0
    # perulangan untuk melakukan clustering
    while len_clusters > k:
        nearest = [[0, 0], 99999]  # variabel untuk menyimpan jarak antar 2 node terdekat
        # perulangan level 1: untuk item 1
        for i, item in enumerate(clusters[iter]):
            c_item = get_centroid(data[item])
            # perulangan level 2: untuk item 2 (pembanding)
            for j, item2 in enumerate(clusters[iter]):
                c_item2 = get_centroid(data[item2])
                if i != j:  # cari hanya data tidak sama dengan dirinya sendiri
                    dist = euclidean_distance(c_item, c_item2)  # cari jarak dengan euclidean
                    if nearest[1] >= dist:  # jika jarak lebih kecil maka ubah variabel nearest
                        nearest = [[i, j], dist]

        items_temp = []  # variabel sementara untuk item yang akan masuk ke cluster ke-i (selanjutnya)
        for x, item in enumerate(clusters[iter]):
            if x not in nearest[0]:  # jika bukan yang terdekat maka langsung tambahkan ke array
                items_temp.append(item)

        # tambahkan node dengan jarak terdekat
        d = np.append(clusters[iter][nearest[0][0]], clusters[iter][nearest[0][1]])
        items_temp.append(d)

        # terakhir clusternya
        clusters.append(items_temp)

        # tambahkan iterasi dan kurangi jumlah cluster
        iter += 1
        len_clusters -= 1

        print("\n-------------------------------MERGE--------------------")
        print("MERGE: ", nearest[0])
        print("Sisa cluster: ", len_clusters)

    print("\n-------------------------------RAW CLUSTER------------------")
    print(clusters[-1])

    # dapatkan hitungan cluster terakhir
    clusters = clusters[-1]

    # hitung cluster dan centroid
    Clusters = np.zeros(len(data))

    for i in range(k):
        for clus in (clusters[i]):
            Clusters[clus] = i

    # hitung centroid
    Centroids = []
    for i in range(k):
        points = [data[j] for j in range(len(data)) if Clusters[j] == i]
        # jika ada cluster yang kosong maka lanjutkan proses karena menghasilkan NaN jika diteruskan
        if len(points) == 0:
            continue
        cent = np.mean(points, axis=0)
        Centroids.append(cent.tolist())

    Centroids = np.array(Centroids)  # ubah ke numpy array supaya dapat dilakukan operasi numpy

    return Clusters, Centroids


# kembalikan rasio eror terkecil
def error_ratio(clusters, labels):
    clus = deepcopy(clusters)
    max_label = np.max(np.unique(labels))
    num_of_labels = len(np.unique(labels))
    error = []

    # coba semua kemungkinan pada label cluster
    # dengan cara mengganti 0 ke 1, 1 ke 2
    for l in range(num_of_labels):
        miss = 0
        if l > 0:
            clus += 1
            clus[clus > max_label] = 0

        for x in range(len(clus)):
            if clus[x] != labels[x]:
                miss += 1

        error.append((miss / len(labels)) * 100)

    return np.min(error)


# Fungsi untuk menghitung variance
def cluster_variance(data, clusters, k):
    n = []
    cv = []
    var = []
    vw = 0
    vb = 0

    # kelompokkan data tiap cluster
    for x in range(k):
        n.append([data[i] for i in range(len(data)) if clusters[i] == x])

    # hitung variance tiap cluster
    for x in range(k):
        d = n[x]  # data pada cluster x
        d_mean = np.mean(n[x], axis=0)  # rata-rata dari data pada suatu cluster
        sum_of_d = 0  # sigma perhitungan data variance

        for di in d:
            res = np.matrix(di - d_mean)
            res = res * res.T  # pangkat dari matriks / vektor
            sum_of_d += res

        # simpan variance tiap cluster
        var.append((1 / (len(n[x]) - 1)) * sum_of_d)

    # within variance
    sum_of_vw = 0  # sigma perhitungan data variance within
    for x in range(k):
        num_of_data_i = len(d[x])
        sum_of_vw += (num_of_data_i - 1 * var[x])

    # simpan variance within (vw)
    vw = (1 / (len(data) - 1)) * sum_of_vw

    # between variance
    sum_of_vb = 0
    for x in range(k):
        num_of_data_i = len(d[x])  # jumlah data tiap cluster
        d_mean = np.mean(n[x], axis=0)  # rata-rata dari data tiap cluster
        grand_mean = np.mean(data, axis=0)  # rata-rata dari seluruh data cluster

        mean_sub_mean = np.matrix(d_mean - grand_mean)
        mean_sub_mean = mean_sub_mean * mean_sub_mean.T
        sum_of_vb += (num_of_data_i * mean_sub_mean)

        # simpan variance between (vb)
    vb = (1 / (k - 1)) * sum_of_vb

    # Hitung total variance
    v = vw / vb

    return v.item()


# Fungsi untuk menghitung SSE
def cluster_sse(data, clusters, k):
    n = []
    cv = []
    var = []
    m = 0
    result = 0
    vb = 0

    # kelompokkan data tiap cluster
    for x in range(k):
        n.append([data[i] for i in range(len(data)) if clusters[i] == x])

    # hitung sse
    for i in range(k):
        s_mean = np.mean(n[i], axis=0)
        # print(s_mean)
        for j in range(len(n[i])):
            # print(n[i][j])
            ms = np.fabs(n[i][j] - s_mean)
            res = np.matrix(ms)
            res = res * res.T  # pangkat dari matriks / vektor
            result += res

    return (result / len(data)).item()


# fungsi CPI
def cluster_cpi(data, centroid, label):
    cpi_hasil = 0
    c_array = []
    c_real = []
    c_r = []
    c_sum = []
    k_label = np.unique(label)
    # mengambil centroid real
    for i in range(len(k_label)):
        c_array.append([data[x] for x in range(len(label)) if label[x] == i])
    for i in range(len(k_label)):
        c_real.append(np.mean(c_array[i], axis=0))

    c_r = (np.fabs(centroid - c_real))

    c_sum = (np.sum(c_r, axis=1))

    cpi_hasil = np.min(c_sum)
    return cpi_hasil


if __name__ == '__main__':

    data, labels = loadDataset()
    print(data)
    print(labels)

    k = 3
    clusters = [np.array([x for x in range(len(data))])]  # inisialisasi awal, semua data dianggap cluster sendiri
    len_clusters = len(clusters[0])  # panjang cluster

    Clusters, Centroids = clustering(len_clusters, clusters, k)

    print("\n-------------------------------CLUSTER------------------")
    print(Clusters)

    print("\n-------------------------------CENTROID------------------")
    print(Centroids)

    print("\n-------------------------------CLUSTER VALIDATION-----------------")
    # Hitung Error Ratio
    error = error_ratio(Clusters, labels)
    print("\nERROR RATIO: ", error, "%")

    # hitung variance
    variance = cluster_variance(data, Clusters, k)
    print("\nVARIANCE: ", variance)

    # hitung SSE
    sse = cluster_sse(data, Clusters, k)
    print("\nSSE: ", sse)

    # hitung cpi
    cpi = cluster_cpi(data, Centroids, labels)
    print("\nCPI: ", cpi)