#Loading dependencies
import cv2 as cv
import random
import numpy as np
from matplotlib import pyplot as plt
from functions import isValid, mean_filter, exor

#Loading images
original = cv2.imread('images\Copyright Image.jpg',0)
watermark = cv2.imread('images\Original Watermark.jpg', 0)
original_height, original_width = original.shape

ret,watermark = cv2.threshold(watermark,127,255,cv2.THRESH_BINARY)

#Plotting images
#plt.imshow(watermark,'gray')
#plt.imshow(original, 'gray')

#Master and ownership share generation
master = np.zeros((watermark.shape[0], watermark.shape[1], 1), np.uint8)
ownership = np.zeros((watermark.shape[0], watermark.shape[1], 1), np.uint8)

pwd = 2018 #Encryption Key
random.seed(a=pwd) #Initialize internal state of the random number generator
random_pts = random.sample(range(original_height*original_width), watermark.shape[0]*watermark.shape[1])

i = 0
j = 0
threshold = 90 #Generally, it is taken as global mean of original image
for k in random_pts:
    x = (int)(k / original_width)
    y = k % original_width
    if mean_filter(original, x, y) > threshold:
        master[i,j] = 255
    j += 1
    if j == watermark.shape[0]:
        j = 0
        i += 1

cv2.imwrite('images\Original Master Image.jpg', master)

for i in range(watermark.shape[0]):
    for j in range(watermark.shape[1]):
        ownership[i, j] = exor(master[i, j], watermark[i, j])
        
cv2.imwrite('images\Ownership Image with Trusted Neutral Party.jpg', ownership)
