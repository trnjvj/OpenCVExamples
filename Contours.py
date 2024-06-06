import numpy as np
import cv2 as cv
 
im = cv.imread('test.jpg')
assert im is not None, "file could not be read, check with os.path.exists()"
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)




import numpy as np
import cv2 as cv
 
img = cv.imread('star.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
 
cnt = contours[0]
M = cv.moments(cnt)
print( M )




cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])




area = cv.contourArea(cnt)



perimeter = cv.arcLength(cnt,True)




epsilon = 0.1*cv.arcLength(cnt,True)
approx = cv.approxPolyDP(cnt,epsilon,True)



hull = cv.convexHull(points[, hull[, clockwise[, returnPoints]]])



hull = cv.convexHull(cnt)




k = cv.isContourConvex(cnt)





x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)




rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img,[box],0,(0,0,255),2)




(x,y),radius = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv.circle(img,center,radius,(0,255,0),2)




ellipse = cv.fitEllipse(cnt)
cv.ellipse(img,ellipse,(0,255,0),2)





rows,cols = img.shape[:2]
[vx,vy,x,y] = cv.fitLine(cnt, cv.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)




x,y,w,h = cv.boundingRect(cnt)
aspect_ratio = float(w)/h



area = cv.contourArea(cnt)
x,y,w,h = cv.boundingRect(cnt)
rect_area = w*h
extent = float(area)/rect_area



area = cv.contourArea(cnt)
hull = cv.convexHull(cnt)
hull_area = cv.contourArea(hull)
solidity = float(area)/hull_area



area = cv.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)




(x,y),(MA,ma),angle = cv.fitEllipse(cnt)



mask = np.zeros(imgray.shape,np.uint8)
cv.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
#pixelpoints = cv.findNonZero(mask)



min_val, max_val, min_loc, max_loc = cv.minMaxLoc(imgray,mask = mask)



mean_val = cv.mean(im,mask = mask)



leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])




hull = cv.convexHull(cnt,returnPoints = False)
defects = cv.convexityDefects(cnt,hull)




import cv2 as cv
import numpy as np
 
img = cv.imread('star.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(img_gray, 127, 255,0)
contours,hierarchy = cv.findContours(thresh,2,1)
cnt = contours[0]
 
hull = cv.convexHull(cnt,returnPoints = False)
defects = cv.convexityDefects(cnt,hull)
 
for i in range(defects.shape[0]):
 s,e,f,d = defects[i,0]
 start = tuple(cnt[s][0])
 end = tuple(cnt[e][0])
 far = tuple(cnt[f][0])
 cv.line(img,start,end,[0,255,0],2)
 cv.circle(img,far,5,[0,0,255],-1)
 
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()




dist = cv.pointPolygonTest(cnt,(50,50),True)



import cv2 as cv
import numpy as np
 
img1 = cv.imread('star.jpg', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('star2.jpg', cv.IMREAD_GRAYSCALE)
assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"
 
ret, thresh = cv.threshold(img1, 127, 255,0)
ret, thresh2 = cv.threshold(img2, 127, 255,0)
contours,hierarchy = cv.findContours(thresh,2,1)
cnt1 = contours[0]
contours,hierarchy = cv.findContours(thresh2,2,1)
cnt2 = contours[0]
 
ret = cv.matchShapes(cnt1,cnt2,1,0.0)
print( ret )





>>> hierarchy
array([[[ 1, -1, -1, -1],
 [ 2, 0, -1, -1],
 [ 3, 1, -1, -1],
 [ 4, 2, -1, -1],
 [ 5, 3, -1, -1],
 [ 6, 4, -1, -1],
 [ 7, 5, -1, -1],
 [-1, 6, -1, -1]]])





>>> hierarchy
array([[[ 1, -1, -1, -1],
 [ 2, 0, -1, -1],
 [-1, 1, -1, -1]]])




>>> hierarchy
array([[[ 3, -1, 1, -1],
 [ 2, -1, -1, 0],
 [-1, 1, -1, 0],
 [ 5, 0, 4, -1],
 [-1, -1, -1, 3],
 [ 7, 3, 6, -1],
 [-1, -1, -1, 5],
 [ 8, 5, -1, -1],
 [-1, 7, -1, -1]]])




>>> hierarchy
array([[[ 7, -1, 1, -1],
 [-1, -1, 2, 0],
 [-1, -1, 3, 1],
 [-1, -1, 4, 2],
 [-1, -1, 5, 3],
 [ 6, -1, -1, 4],
 [-1, 5, -1, 4],
 [ 8, 0, -1, -1],
 [-1, 7, -1, -1]]])





