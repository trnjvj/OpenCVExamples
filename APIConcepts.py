#include "opencv2/core.hpp"
...
cv::Mat H = cv::findHomography(points1, points2, cv::RANSAC, 5);
...

#include "opencv2/core.hpp"
using namespace cv;
...
Mat H = findHomography(points1, points2, RANSAC, 5 );
...

Mat a(100, 100, CV_32F);
randu(a, Scalar::all(1), Scalar::all(std::rand()));
cv::log(a, a);
a /= std::log(2.);

// create a big 8Mb matrix
Mat A(1000, 1000, CV_64F);
 
// create another header for the same matrix;
// this is an instant operation, regardless of the matrix size.
Mat B = A;
// create another header for the 3-rd row of A; no data is copied either
Mat C = B.row(3);
// now create a separate copy of the matrix
Mat D = B.clone();
// copy the 5-th row of B to C, that is, copy the 5-th row of A
// to the 3-rd row of A.
B.row(5).copyTo(C);
// now let A and D share the data; after that the modified version
// of A is still referenced by B and C.
A = D;
// now make B an empty matrix (which references no memory buffers),
// but the modified version of A will still be referenced by C,
// despite that C is just a single row of the original A
B.release();
 
// finally, make a full copy of C. As a result, the big modified
// matrix will be deallocated, since it is not referenced by anyone
C = C.clone();

T* ptr = new T(...);

Ptr<T> ptr(new T(...));

Ptr<T> ptr = makePtr<T>(...);

#include "opencv2/imgproc.hpp"
#include "opencv2/highgui.hpp"
 
using namespace cv;
 
int main(int, char**)
{
 VideoCapture cap(0);
 if(!cap.isOpened()) return -1;
 
 Mat frame, edges;
 namedWindow("edges", WINDOW_AUTOSIZE);
 for(;;)
 {
 cap >> frame;
 cvtColor(frame, edges, COLOR_BGR2GRAY);
 GaussianBlur(edges, edges, Size(7,7), 1.5, 1.5);
 Canny(edges, edges, 0, 30, 3);
 imshow("edges", edges);
 if(waitKey(30) >= 0) break;
 }
 return 0;
}

I.at<uchar>(y, x) = saturate_cast<uchar>(r);

Mat mtx(3, 3, CV_32F); // make a 3x3 floating-point matrix
Mat cmtx(10, 1, CV_64FC2); // make a 10x1 2-channel floating-point
 // matrix (10-element complex vector)
Mat img(Size(1920, 1080), CV_8UC3); // make a 3-channel (color) image
 // of 1920 columns and 1080 rows.
Mat grayscale(img.size(), CV_MAKETYPE(img.depth(), 1)); // make a 1-channel image of
 // the same size and same
 // channel type as img
 
 