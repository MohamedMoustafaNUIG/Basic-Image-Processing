#pip install matplotlib
from matplotlib import pyplot as plt
#pip install scikit-image
from skimage import data
from skimage.color import rgb2gray
from skimage.io import imread
from skimage.feature import blob_dog, blob_log, blob_doh
#Shouldnt need installation
from math import sqrt
import os
#get current directory
cwd = os.path.abspath(__file__+"/..")
#read image
im = imread(cwd + "/sky.jpg", as_grey=True)

cm_gray = plt.get_cmap('gray')
plt.imshow(im, cmap=cm_gray)
plt.show()

blobs_log = blob_log(im, max_sigma=30, num_sigma=10, threshold=.1)
blobs_log[:,2] = blobs_log[:,2] * sqrt(2)
numrows = len(blobs_log)
print("Number of stars counted : ", numrows)

fig, ax = plt.subplots(1,1)
plt.imshow(im, cmap=cm_gray)
#circle all blobs in plot
for blob in blobs_log:
	y, x, r = blob
	c = plt.Circle((x,y), r+5, color='lime', linewidth=2, fill=False)
	ax.add_patch(c)
#show plot
plt.show()