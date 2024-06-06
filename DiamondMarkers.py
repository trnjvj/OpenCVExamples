 vector<int> diamondIds = {ids[0], ids[1], ids[2], ids[3]};
 aruco::CharucoBoard charucoBoard(Size(3, 3), (float)squareLength, (float)markerLength, dictionary, diamondIds);
 Mat markerImg;
 charucoBoard.generateImage(Size(3*squareLength + 2*margins, 3*squareLength + 2*margins), markerImg, margins, borderBits);




 // estimate diamond pose
 size_t N = diamondIds.size();
 if(estimatePose && N > 0) {
 cv::Mat objPoints(4, 1, CV_32FC3);
 rvecs.resize(N);
 tvecs.resize(N);
 if(!autoScale) {
 // set coordinate system
 objPoints.ptr<Vec3f>(0)[0] = Vec3f(-squareLength/2.f, squareLength/2.f, 0);
 objPoints.ptr<Vec3f>(0)[1] = Vec3f(squareLength/2.f, squareLength/2.f, 0);
 objPoints.ptr<Vec3f>(0)[2] = Vec3f(squareLength/2.f, -squareLength/2.f, 0);
 objPoints.ptr<Vec3f>(0)[3] = Vec3f(-squareLength/2.f, -squareLength/2.f, 0);
 // Calculate pose for each marker
 for (size_t i = 0ull; i < N; i++)
 solvePnP(objPoints, diamondCorners.at(i), camMatrix, distCoeffs, rvecs.at(i), tvecs.at(i));
 if(estimatePose) {
 for(size_t i = 0u; i < diamondIds.size(); i++)
 cv::drawFrameAxes(imageCopy, camMatrix, distCoeffs, rvecs[i], tvecs[i], squareLength*1.1f);
 }
 
 
 
 for (size_t i = 0ull; i < N; i++) { // estimate diamond pose as Charuco board
Mat objPoints_b, imgPoints;
// The coordinate system of the diamond is placed in the board plane centered in the bottom left corner
vector<int> charucoIds = {0, 1, 3, 2}; // if CCW order, Z axis pointing in the plane
// vector<int> charucoIds = {0, 2, 3, 1}; // if CW order, Z axis pointing out the plane
charucoBoard.matchImagePoints(diamondCorners[i], charucoIds, objPoints_b, imgPoints);
solvePnP(objPoints_b, imgPoints, camMatrix, distCoeffs, rvecs[i], tvecs[i]);
}




dp=path_to_opencv/opencv/samples/cpp/tutorial_code/objectDetection/detector_params.yml -sl=0.4 -ml=0.25 -refine=3
-v=path_to_opencv/opencv/doc/tutorials/objdetect/charuco_diamond_detection/images/diamondmarkers.jpg
-cd=path_to_opencv/opencv/samples/cpp/tutorial_code/objectDetection/tutorial_dict.yml
-c=path_to_opencv/opencv/samples/cpp/tutorial_code/objectDetection/tutorial_camera_params.yml



