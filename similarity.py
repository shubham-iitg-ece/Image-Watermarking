#loading dependencies
import cv2
import random
import numpy as np
from matplotlib import pyplot as plt
from functions import exor

#Global constants intialisation
original_width = 915
original_height = 515
watermark_width = 500
watermark_height = 500
original_size = original_height*original_width
watermark_size = watermark_height*watermark_width
pwd = 2018 #Encryption key
threshold = 90

#Same random pixels selection based on encryption key
random.seed(a=pwd) 
random_pts = random.sample(range(original_size), watermark_size)

ownership = cv2.imread('images\Ownership Image with Trusted Neutral Party.jpg', 0)

#Extracting watermark from modified image using encryption key and
#ownership image from the neutral party
extracted_master = cv2.imread('images\Extracted Master Image.jpg', 0)
extracted_watermark = np.zeros((watermark_width, watermark_height, 1), np.uint8)

i = 0
j = 0
for i in range(watermark_height):
        for j in range(watermark_width):
            extracted_watermark[i, j] = exor(extracted_master[i, j], ownership[i, j])

cv2.imwrite('images\XORed Output.jpg', extracted_watermark)

#Extracted watermark processing to remove redundant noise
extracted_watermark = (255-extracted_watermark)
kernel = np.ones((4,4),np.uint8)
extracted_watermark = cv2.medianBlur(extracted_watermark, 3)
extracted_watermark = cv2.morphologyEx(extracted_watermark, cv2.MORPH_OPEN, kernel)
extracted_watermark = cv2.morphologyEx(extracted_watermark, cv2.MORPH_CLOSE, kernel)
extracted_watermark = (255-extracted_watermark)

#Saving extracted watermark
cv2.imwrite('images\Extracted Watermark.jpg', extracted_watermark)

#Comparing original and extracted watermark
watermark = cv2.imread('images\Original Watermark.jpg', 0)
ret,watermark = cv2.threshold(watermark,127,255,cv2.THRESH_BINARY)
result = cv2.matchTemplate(extracted_watermark,watermark,cv2.TM_CCOEFF_NORMED)
print('Similarity between original watermark and extracted watermark is %.2f.' %result)
if(result>0.7):
    print('Copyright Claimed!')
else:
    print('False Claim!')
