class Cluster:
    def hierarcial(data,ncluster):
        from sklearn.cluster import AgglomerativeClustering
        ahcModel = AgglomerativeClustering(n_clusters=ncluster,linkage='average', affinity="euclidean")
        ahc = ahcModel.fit_predict(data)
        return ahc