 try
 {
 app.bardet = makePtr<barcode::BarcodeDetector>(sr_prototxt, sr_model);
 }
 catch (const std::exception& e)
 {
 cout <<
 "\n---------------------------------------------------------------\n"
 "Failed to initialize super resolution.\n"
 "Please, download 'sr.*' from\n"
 "https://github.com/WeChatCV/opencv_3rdparty/tree/wechat_qrcode\n"
 "and put them into the current directory.\n"
 "Or you can leave sr_prototxt and sr_model unspecified.\n"
 "---------------------------------------------------------------\n";
 cout << e.what() << endl;
 return -1;
 }





 for (size_t i = 0; i < corners.size(); i += 4)
 {
 const size_t idx = i / 4;
 const bool isDecodable = idx < decode_info.size()
 && idx < decode_type.size()
 && !decode_type[idx].empty();
 const Scalar lineColor = isDecodable ? greenColor : redColor;
 // draw barcode rectangle
 vector<Point> contour(corners.begin() + i, corners.begin() + i + 4);
 const vector< vector<Point> > contours {contour};
 drawContours(frame, contours, 0, lineColor, 1);
 // draw vertices
 for (size_t j = 0; j < 4; j++)
 circle(frame, contour[j], 2, randColor(), -1);
 // write decoded text
 if (isDecodable)
 {
 ostringstream buf;
 buf << "[" << decode_type[idx] << "] " << decode_info[idx];
 putText(frame, buf.str(), contour[1], FONT_HERSHEY_COMPLEX, 0.8, yellowColor, 1);
 }
 }





