import cv2
  
originalImage = cv2.imread('121.jpg')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
  
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
 
# cv2.imshow('Original image',originalImage)
# cv2.imshow('Gray image', grayImage)
new = cv2.subtract(255, blackAndWhiteImage) 
cv2.imwrite('new.png',new)
cv2.imshow('Black white image', new)
cv2.waitKey(0)
cv2.destroyAllWindows()
