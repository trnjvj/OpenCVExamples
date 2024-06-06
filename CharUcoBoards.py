 int squaresX = parser.get<int>("w");
 int squaresY = parser.get<int>("h");
 float squareLength = parser.get<float>("sl");
 float markerLength = parser.get<float>("ml");
 bool refine = parser.has("rs");
 int camId = parser.get<int>("ci");
 
 string video;
 if(parser.has("v")) {
 video = parser.get<string>("v");
 }
 
 Mat camMatrix, distCoeffs;
 readCameraParamsFromCommandLine(parser, camMatrix, distCoeffs);
 aruco::DetectorParameters detectorParams = readDetectorParamsFromCommandLine(parser);
 aruco::Dictionary dictionary = readDictionatyFromCommandLine(parser);
 
 if(!parser.check()) {
 parser.printErrors();
 return 0;
 }
 
 VideoCapture inputVideo;
 int waitTime = 0;
 if(!video.empty()) {
 inputVideo.open(video);
 } else {
 inputVideo.open(camId);
 waitTime = 10;
 }
 
 float axisLength = 0.5f * ((float)min(squaresX, squaresY) * (squareLength));
 
 // create charuco board object
 aruco::CharucoBoard charucoBoard(Size(squaresX, squaresY), squareLength, markerLength, dictionary);
 
 // create charuco detector
 aruco::CharucoParameters charucoParams;
 charucoParams.tryRefineMarkers = refine; // if tryRefineMarkers, refineDetectedMarkers() will be used in detectBoard()
 charucoParams.cameraMatrix = camMatrix; // cameraMatrix can be used in detectBoard()
 charucoParams.distCoeffs = distCoeffs; // distCoeffs can be used in detectBoard()
 aruco::CharucoDetector charucoDetector(charucoBoard, charucoParams, detectorParams);
 
 double totalTime = 0;
 int totalIterations = 0;
 
 while(inputVideo.grab()) {
 Mat image, imageCopy;
 inputVideo.retrieve(image);
 
 double tick = (double)getTickCount();
 
 vector<int> markerIds, charucoIds;
 vector<vector<Point2f> > markerCorners;
 vector<Point2f> charucoCorners;
 Vec3d rvec, tvec;
 
 // detect markers and charuco corners
 charucoDetector.detectBoard(image, charucoCorners, charucoIds, markerCorners, markerIds);
 
 // estimate charuco board pose
 bool validPose = false;
 if(camMatrix.total() != 0 && distCoeffs.total() != 0 && charucoIds.size() >= 4) {
 Mat objPoints, imgPoints;
 charucoBoard.matchImagePoints(charucoCorners, charucoIds, objPoints, imgPoints);
 validPose = solvePnP(objPoints, imgPoints, camMatrix, distCoeffs, rvec, tvec);
 }
 
 double currentTime = ((double)getTickCount() - tick) / getTickFrequency();
 totalTime += currentTime;
 totalIterations++;
 if(totalIterations % 30 == 0) {
 cout << "Detection Time = " << currentTime * 1000 << " ms "
 << "(Mean = " << 1000 * totalTime / double(totalIterations) << " ms)" << endl;
 }
 
 // draw results
 image.copyTo(imageCopy);
 if(markerIds.size() > 0) {
 aruco::drawDetectedMarkers(imageCopy, markerCorners);
 }
 
 if(charucoIds.size() > 0) {
 aruco::drawDetectedCornersCharuco(imageCopy, charucoCorners, charucoIds, cv::Scalar(255, 0, 0));
 }
 
 if(validPose)
 cv::drawFrameAxes(imageCopy, camMatrix, distCoeffs, rvec, tvec, axisLength);
 
 imshow("out", imageCopy);
 if(waitKey(waitTime) == 27) break;
 }
 
 
 
 
 #include <opencv2/objdetect/charuco_detector.hpp>
 
 
 
 
 Mat image, imageCopy;
inputVideo.retrieve(image);




 if(parser.has("c")) {
 bool readOk = readCameraParameters(parser.get<std::string>("c"), camMatrix, distCoeffs);
 if(!readOk) {
 throw std::runtime_error("Invalid camera file\n");
 }
 }




 // detect markers and charuco corners
 charucoDetector.detectBoard(image, charucoCorners, charucoIds, markerCorners, markerIds);




 // estimate charuco board pose
 bool validPose = false;
 if(camMatrix.total() != 0 && distCoeffs.total() != 0 && charucoIds.size() >= 4) {
 Mat objPoints, imgPoints;
 charucoBoard.matchImagePoints(charucoCorners, charucoIds, objPoints, imgPoints);
 validPose = solvePnP(objPoints, imgPoints, camMatrix, distCoeffs, rvec, tvec);
 }




