import cv2 as cv
import numpy as np
 
img = cv.imread('j.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)




dilation = cv.dilate(img,kernel,iterations = 1)




opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)




closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)




gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)



tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)



blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)



# Rectangular Kernel
>>> cv.getStructuringElement(cv.MORPH_RECT,(5,5))
array([[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]], dtype=uint8)
 
# Elliptical Kernel
>>> cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
array([[0, 0, 1, 0, 0],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 0, 1, 0, 0]], dtype=uint8)
 
# Cross-shaped Kernel
>>> cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
array([[0, 0, 1, 0, 0],
 [0, 0, 1, 0, 0],
 [1, 1, 1, 1, 1],
 [0, 0, 1, 0, 0],
 [0, 0, 1, 0, 0]], dtype=uint8)




