// Open depth stream
 VideoCapture depthStream(CAP_OPENNI2_ASTRA);
 // Open color stream
 VideoCapture colorStream(0, CAP_V4L2);
 
 
 
 
 
 // Set color and depth stream parameters
 colorStream.set(CAP_PROP_FRAME_WIDTH, 640);
 colorStream.set(CAP_PROP_FRAME_HEIGHT, 480);
 depthStream.set(CAP_PROP_FRAME_WIDTH, 640);
 depthStream.set(CAP_PROP_FRAME_HEIGHT, 480);
 depthStream.set(CAP_PROP_OPENNI2_MIRROR, 0);
 
 
 
 
 // Print depth stream parameters
 cout << "Depth stream: "
 << depthStream.get(CAP_PROP_FRAME_WIDTH) << "x" << depthStream.get(CAP_PROP_FRAME_HEIGHT)
 << " @" << depthStream.get(CAP_PROP_FPS) << " fps" << endl;
 
 
 
 
 // Create two lists to store frames
 std::list<Frame> depthFrames, colorFrames;
 const std::size_t maxFrames = 64;
 
 // Synchronization objects
 std::mutex mtx;
 std::condition_variable dataReady;
 std::atomic<bool> isFinish;
 
 isFinish = false;
 
 // Start depth reading thread
 std::thread depthReader([&]
 {
 while (!isFinish)
 {
 // Grab and decode new frame
 if (depthStream.grab())
 {
 Frame f;
 f.timestamp = cv::getTickCount();
 depthStream.retrieve(f.frame, CAP_OPENNI_DEPTH_MAP);
 if (f.frame.empty())
 {
 cerr << "ERROR: Failed to decode frame from depth stream" << endl;
 break;
 }
 
 {
 std::lock_guard<std::mutex> lk(mtx);
 if (depthFrames.size() >= maxFrames)
 depthFrames.pop_front();
 depthFrames.push_back(f);
 }
 dataReady.notify_one();
 }
 }
 });
 
 // Start color reading thread
 std::thread colorReader([&]
 {
 while (!isFinish)
 {
 // Grab and decode new frame
 if (colorStream.grab())
 {
 Frame f;
 f.timestamp = cv::getTickCount();
 colorStream.retrieve(f.frame);
 if (f.frame.empty())
 {
 cerr << "ERROR: Failed to decode frame from color stream" << endl;
 break;
 }
 
 {
 std::lock_guard<std::mutex> lk(mtx);
 if (colorFrames.size() >= maxFrames)
 colorFrames.pop_front();
 colorFrames.push_back(f);
 }
 dataReady.notify_one();
 }
 }
 });
 
 
 
 
 
 
 // Pair depth and color frames
 while (!isFinish)
 {
 std::unique_lock<std::mutex> lk(mtx);
 while (!isFinish && (depthFrames.empty() || colorFrames.empty()))
 dataReady.wait(lk);
 
 while (!depthFrames.empty() && !colorFrames.empty())
 {
 if (!lk.owns_lock())
 lk.lock();
 
 // Get a frame from the list
 Frame depthFrame = depthFrames.front();
 int64 depthT = depthFrame.timestamp;
 
 // Get a frame from the list
 Frame colorFrame = colorFrames.front();
 int64 colorT = colorFrame.timestamp;
 
 // Half of frame period is a maximum time diff between frames
 const int64 maxTdiff = int64(1000000000 / (2 * colorStream.get(CAP_PROP_FPS)));
 if (depthT + maxTdiff < colorT)
 {
 depthFrames.pop_front();
 continue;
 }
 else if (colorT + maxTdiff < depthT)
 {
 colorFrames.pop_front();
 continue;
 }
 depthFrames.pop_front();
 colorFrames.pop_front();
 lk.unlock();
 
 // Show depth frame
 Mat d8, dColor;
 depthFrame.frame.convertTo(d8, CV_8U, 255.0 / 2500);
 applyColorMap(d8, dColor, COLORMAP_OCEAN);
 imshow("Depth (colored)", dColor);
 
 // Show color frame
 imshow("Color", colorFrame.frame);
 
 // Exit on Esc key press
 int key = waitKey(1);
 if (key == 27) // ESC
 {
 isFinish = true;
 break;
 }
 }
 }
 
 
 
 
 
 
 