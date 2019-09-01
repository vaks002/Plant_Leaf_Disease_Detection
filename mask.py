import imp
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
import numpy as np
import cv2
import os
from PIL import Image


train= 'kmean'


path = 'clusteredImages'
os.mkdir(path)

images = []
for filename in os.listdir(train):
	print('Ajay111\n')

	floc = filename

	print(filename)

	RGBim = Image.open(str(train) + '\\' + floc ).convert('RGB')
	HSVim = RGBim.convert('HSV')


	# Make numpy versions
	RGBna = np.array(RGBim)
	HSVna = np.array(HSVim)

	# Extract Hue
	H = HSVna[:,:,0]

	# Find all green pixels, i.e. where 100 < Hue < 140
	lo,hi = 100,140
	# Rescale to 0-255, rather than 0-360 because we are using uint8
	lo = int((lo * 255) / 360)
	hi = int((hi * 255) / 360)
	green = np.where((H>lo) & (H<hi))

	# Make all green pixels black in original image
	RGBna[green] = [0,0,0]

	count = green[0].size
	print("Pixels matched: {}".format(count))
	Image.fromarray(RGBna).save(os.path.join(path , filename))


cv2.waitKey(0)
cv2.destroyAllWindows()
	




