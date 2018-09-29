#Loading dependencies
import cv2
import random
import numpy as np
from matplotlib import pyplot as plt
from functions import isValid, mean_filter

#Global constants initialisation
original_width = 915
original_height = 515
watermark_width = 500
watermark_height = 500
original_size = original_height*original_width
watermark_size = watermark_height*watermark_width
pwd = 2018 #encryption key
threshold = 90

#Same random pixels selection based on encryption key
random.seed(a=pwd) 
random_pts = random.sample(range(original_size), watermark_size)

modified = cv2.imread('images\Copyright Image with Visible Watermark & Contrast Enhancement.jpg',0)
extracted_master = np.zeros((watermark_width, watermark_height, 1), np.uint8)

i = 0
j = 0
for k in random_pts:
    x = (int)(k / original_width)
    y = k % original_width
    if mean_filter(modified, x, y) > threshold:
        extracted_master[i,j] = 255
    j += 1
    if j == watermark_height:
        j = 0
        i += 1

cv2.imwrite('images\Extracted Master Image.jpg', extracted_master)
