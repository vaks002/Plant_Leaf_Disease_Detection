import imp
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
import numpy as np
import cv2
import os

train= 'train'


path = 'kmean'
os.mkdir(path)

images = []
for filename in os.listdir(train):
    img = cv2.imread(os.path.join(train,filename))
    (h1, w1) = img.shape[:2]


    image1 = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    image1 = image1.reshape((image1.shape[0] * image1.shape[1], 3))
    # clt = MiniBatchKMeans(n_clusters = 16)
    clt = KMeans(n_clusters = 4)

    labels1 = clt.fit_predict(image1)
    quant1 = clt.cluster_centers_.astype("uint8")[labels1]
    print("1st done")



#reshape the feature vectors to images
    quant1 = quant1.reshape((h1, w1, 3))
    image1 = image1.reshape((h1, w1, 3))

# convert from L*a*b* to RGB
    quant1 = cv2.cvtColor(quant1, cv2.COLOR_LAB2BGR)
    image1 = cv2.cvtColor(image1, cv2.COLOR_LAB2BGR)
    if img is not None:
        images.append(image1)

    cv2.imwrite(os.path.join(path , filename), quant1)


cv2.waitKey(0)
cv2.destroyAllWindows()