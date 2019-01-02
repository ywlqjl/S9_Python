'''
========================================
TP6_image YAN Wenli & PENG Hanyuan
========================================
'''
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
from PIL import Image
import numpy as np

imagepath_1 = 'test.png'  #.png
imagepath_2 = 'test_2.jpg'  #.jpg

# ---------------------- Read Image -------------------------------
# read image, et la test_iamge est déjà un np.array pour faire des traitements
# test_image = misc.imread(imagepath_1)
# test_image = mpimg.imread(imagepath_2)
test_image = Image.open(imagepath_2)
imResize = test_image.resize((150,100), Image.ANTIALIAS)
l_image = test_image.convert('L')
box = (0, 0, 1000, 700)              ##确定拷贝区域大小
region = test_image.crop(box)
# test_image.shape #(512, 512, 3)
#------------------ Show image original ---------------------------
# plt.imshow(imResize)
# plt.axis('off') #ne montre pas les axis
# plt.show()

# Afficher l'image originale et des résultats avec des éffets
plt.subplot(221)
plt.title('PIL read image original')
plt.imshow(test_image)
plt.subplot(222)
plt.title('imResize 150*100')
plt.imshow(imResize)
plt.subplot(223)
plt.title('grey')
plt.imshow(l_image)
plt.subplot(224)
plt.title('region with box')
plt.imshow(region)
plt.show()
