from sklearn.cluster import KMeans

import numpy as np
from skimage import io

def color_quantize(img,n_clusters):
    """
    returns color quantized version of the input img
    """

    height, width = img.shape[:-1]
    img_reshaped = img.reshape((img.shape[0]*img.shape[1], -1))
    kmeans = KMeans(n_clusters, max_iter=10)

    kmeans.fit(img_reshaped)
    labels = kmeans.labels_.reshape((height, width))
    centers = kmeans.cluster_centers_
    img_quant = centers[labels]
    return np.asarray(img_quant, dtype='uint8')


def to_reconst_kmeg(img_file_nm,  n_clusters, reconst_file):
    img = io.imread(img_file_nm)
    img_quant = color_quantize(img, n_clusters)
    io.imsave(reconst_file, img_quant)



