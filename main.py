import cv2
import numpy as np
from scipy import ndimage

originalImage = cv2.imread('124.jpg')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
  
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
 
# cv2.imshow('Original image',originalImage)
# cv2.imshow('Gray image', grayImage)
new = cv2.subtract(255, blackAndWhiteImage) 

# Rotating the img 
#result = ndimage.rotate(new, -10)

#cv2.imwrite('124_new.png',result)

cv2.imshow('Black white image', new)

cv2.waitKey(0)

cv2.destroyAllWindows()
