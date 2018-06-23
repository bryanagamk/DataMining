class Agregasi:
    def band(self):
        from PIL import Image
        import numpy as np
        from numpy import zeros
        from MultibandImageClustering.clusterProses import Cluster
        import random
        # initial loop from index 0
        paths = []
        paths[0] = "../DataSource/multiband_data/gb1.GIF"

        paths[1] = "../DataSource/multiband_data/gb2.GIF"

        paths[2] = "../DataSource/multiband_data/gb3.GIF"

        paths[3] = "../DataSource/multiband_data/gb4.GIF"

        paths[4] = "../DataSource/multiband_data/gb5.GIF"

        paths[5] = "../DataSource/multiband_data/gb7.GIF"
        numb_of_data = len(paths)
        index = 0

        # initial variabel
        image_temp = Image.open(
            "../DataSource/multiband_data/gb1.GIF")
        final_data = zeros([image_temp.size[0] * image_temp.size[1], numb_of_data])
        im = {}
        while index < numb_of_data:
            name = str(index)
            im[index] = Image.open(paths[index])
            i = 0
            for x in range(0, im[index].size[0]):
                for y in range(0, im[index].size[1]):
                    pix_val = im[index].getpixel((x, y))
                    final_data[i][index] = pix_val
                    i += 1
            index += 1
        # print(final_data)
        # call clustering proses
        k = Cluster.hierarcial(final_data, int(4))
        cluster_uniq = np.unique(k)
        # data after cluster proses
        data_with_cluster = np.insert(final_data, 6, k, axis=1)

        # print(cluster_uniq)
        # np.savetxt('data_cluster.csv',data_with_cluster, delimiter=' ')

        # create image
        # create n-random rgb color by n-cluster
        def colors(n):
            ret = []
            r = int(random.random() * 256)
            g = int(random.random() * 256)
            b = int(random.random() * 256)
            step = 256 / n
            for i in range(n):
                r += step
                g += step
                b += step
                r = int(r) % 256
                g = int(g) % 256
                b = int(b) % 256
                ret.append((r, g, b))
            return ret

        warna = colors(int(4))
        im2 = Image.new("RGB", (image_temp.size[0], image_temp.size[1]))
        pixels = im2.load()
        i = 0
        for x in range(0, image_temp.size[0]):
            for y in range(0, image_temp.size[1]):
                for z in range(0, int(4)):
                    if data_with_cluster[i][6] == cluster_uniq[z]:
                        pixels[x, y] = warna[z]
                # if data_with_cluster[i][6] == 0:
                #     pixels[x,y] = warna[0]
                # elif data_with_cluster[i][6] == 1:
                #     pixels[x,y] = warna[1]
                # else:
                #     pixels[x,y] = warna[2]
                # print(x,y,i)
                i += 1
                # pixels[x, y] = warna1
        # print(pixels)
        return im2
