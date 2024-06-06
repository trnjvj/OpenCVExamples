// g++ main.cpp -o a.out -I /usr/local/include/opencv4 -lopencv_core -lopencv_highgui -lopencv_imgcodecs
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgcodecs.hpp>
#include <iostream>
#include <string>
 
int main(void)
{
 std::cout << "cv::currentUIFramework() returns " << cv::currentUIFramework() << std::endl;
 
 cv::Mat src;
 src = cv::imread("opencv-logo.png");
 
 cv::namedWindow("src");
 
 int key = 0;
 do
 {
 cv::imshow("src", src );
 key = cv::waitKey(50);
 } while( key != 'q' );
 return 0;
}
