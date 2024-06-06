import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
 
img = cv.imread('opencv_logo.png')
assert img is not None, "file could not be read, check with os.path.exists()"
 
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
 
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()





import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
 
img = cv.imread('opencv-logo-white.png')
assert img is not None, "file could not be read, check with os.path.exists()"
 
blur = cv.blur(img,(5,5))
 
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()




blur = cv.GaussianBlur(img,(5,5),0)




median = cv.medianBlur(img,5)




blur = cv.bilateralFilter(img,9,75,75)




