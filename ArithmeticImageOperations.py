>>> x = np.uint8([250])
>>> y = np.uint8([10])
 
>>> print( cv.add(x,y) ) # 250+10 = 260 => 255
[[255]]
 
>>> print( x+y ) # 250+10 = 260 % 256 = 4
[4]




img1 = cv.imread('ml.png')
img2 = cv.imread('opencv-logo.png')
assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"
 
dst = cv.addWeighted(img1,0.7,img2,0.3,0)
 
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()




# Load two images
img1 = cv.imread('messi5.jpg')
img2 = cv.imread('opencv-logo-white.png')
assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"
 
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]
 
# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
 
# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
 
# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
 
# Put logo in ROI and modify the main image
dst = cv.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
 
cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()




