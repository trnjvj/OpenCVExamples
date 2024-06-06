e1 = cv.getTickCount()
# your code execution
e2 = cv.getTickCount()
time = (e2 - e1)/ cv.getTickFrequency()




img1 = cv.imread('messi5.jpg')
assert img1 is not None, "file could not be read, check with os.path.exists()"
 
e1 = cv.getTickCount()
for i in range(5,49,2):
 img1 = cv.medianBlur(img1,i)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print( t )
 
# Result I got is 0.521107655 seconds




# check if optimization is enabled
In [5]: cv.useOptimized()
Out[5]: True
 
In [6]: %timeit res = cv.medianBlur(img,49)
10 loops, best of 3: 34.9 ms per loop
 
# Disable it
In [7]: cv.setUseOptimized(False)
 
In [8]: cv.useOptimized()
Out[8]: False
 
In [9]: %timeit res = cv.medianBlur(img,49)
10 loops, best of 3: 64.1 ms per loop




In [10]: x = 5
 
In [11]: %timeit y=x**2
10000000 loops, best of 3: 73 ns per loop
 
In [12]: %timeit y=x*x
10000000 loops, best of 3: 58.3 ns per loop
 
In [15]: z = np.uint8([5])
 
In [17]: %timeit y=z*z
1000000 loops, best of 3: 1.25 us per loop
 
In [19]: %timeit y=np.square(z)
1000000 loops, best of 3: 1.16 us per loop





In [35]: %timeit z = cv.countNonZero(img)
100000 loops, best of 3: 15.8 us per loop
 
In [36]: %timeit z = np.count_nonzero(img)
1000 loops, best of 3: 370 us per loop




