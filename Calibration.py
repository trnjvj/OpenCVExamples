 // Create charuco board object and CharucoDetector
 aruco::CharucoBoard board(Size(squaresX, squaresY), squareLength, markerLength, dictionary);
 aruco::CharucoDetector detector(board, charucoParams, detectorParams);
 
 // Collect data from each frame
 vector<Mat> allCharucoCorners, allCharucoIds;
 
 vector<vector<Point2f>> allImagePoints;
 vector<vector<Point3f>> allObjectPoints;
 
 vector<Mat> allImages;
 Size imageSize;
 
 while(inputVideo.grab()) {
 Mat image, imageCopy;
 inputVideo.retrieve(image);
 
 vector<int> markerIds;
 vector<vector<Point2f>> markerCorners;
 Mat currentCharucoCorners, currentCharucoIds;
 vector<Point3f> currentObjectPoints;
 vector<Point2f> currentImagePoints;
 
 // Detect ChArUco board
 detector.detectBoard(image, currentCharucoCorners, currentCharucoIds);
 if(key == 'c' && currentCharucoCorners.total() > 3) {
 // Match image points
 board.matchImagePoints(currentCharucoCorners, currentCharucoIds, currentObjectPoints, currentImagePoints);
 
 if(currentImagePoints.empty() || currentObjectPoints.empty()) {
 cout << "Point matching failed, try again." << endl;
 continue;
 }
 
 cout << "Frame captured" << endl;
 
 allCharucoCorners.push_back(currentCharucoCorners);
 allCharucoIds.push_back(currentCharucoIds);
 allImagePoints.push_back(currentImagePoints);
 allObjectPoints.push_back(currentObjectPoints);
 allImages.push_back(image);
 
 imageSize = image.size();
 }
 }
 Mat cameraMatrix, distCoeffs;
 
 if(calibrationFlags & CALIB_FIX_ASPECT_RATIO) {
 cameraMatrix = Mat::eye(3, 3, CV_64F);
 cameraMatrix.at<double>(0, 0) = aspectRatio;
 }
 
 // Calibrate camera using ChArUco
 double repError = calibrateCamera(allObjectPoints, allImagePoints, imageSize, cameraMatrix, distCoeffs,
 noArray(), noArray(), noArray(), noArray(), noArray(), calibrationFlags);
 
 
 
 
 "camera_calib.txt" -w=5 -h=7 -sl=0.04 -ml=0.02 -d=10
-v=path/img_%02d.jpg




 // Create board object and ArucoDetector
 aruco::GridBoard gridboard(Size(markersX, markersY), markerLength, markerSeparation, dictionary);
 aruco::ArucoDetector detector(dictionary, detectorParams);
 
 // Collected frames for calibration
 vector<vector<vector<Point2f>>> allMarkerCorners;
 vector<vector<int>> allMarkerIds;
 Size imageSize;
 
 while(inputVideo.grab()) {
 Mat image, imageCopy;
 inputVideo.retrieve(image);
 
 vector<int> markerIds;
 vector<vector<Point2f>> markerCorners, rejectedMarkers;
 
 // Detect markers
 detector.detectMarkers(image, markerCorners, markerIds, rejectedMarkers);
 
 // Refind strategy to detect more markers
 if(refindStrategy) {
 detector.refineDetectedMarkers(image, gridboard, markerCorners, markerIds, rejectedMarkers);
 }
 if(key == 'c' && !markerIds.empty()) {
 cout << "Frame captured" << endl;
 allMarkerCorners.push_back(markerCorners);
 allMarkerIds.push_back(markerIds);
 imageSize = image.size();
 }
 }
 Mat cameraMatrix, distCoeffs;
 
 if(calibrationFlags & CALIB_FIX_ASPECT_RATIO) {
 cameraMatrix = Mat::eye(3, 3, CV_64F);
 cameraMatrix.at<double>(0, 0) = aspectRatio;
 }
 
 // Prepare data for calibration
 vector<Point3f> objectPoints;
 vector<Point2f> imagePoints;
 vector<Mat> processedObjectPoints, processedImagePoints;
 size_t nFrames = allMarkerCorners.size();
 
 for(size_t frame = 0; frame < nFrames; frame++) {
 Mat currentImgPoints, currentObjPoints;
 
 gridboard.matchImagePoints(allMarkerCorners[frame], allMarkerIds[frame], currentObjPoints, currentImgPoints);
 
 if(currentImgPoints.total() > 0 && currentObjPoints.total() > 0) {
 processedImagePoints.push_back(currentImgPoints);
 processedObjectPoints.push_back(currentObjPoints);
 }
 }
 
 // Calibrate camera
 double repError = calibrateCamera(processedObjectPoints, processedImagePoints, imageSize, cameraMatrix, distCoeffs,
 noArray(), noArray(), noArray(), noArray(), noArray(), calibrationFlags);





