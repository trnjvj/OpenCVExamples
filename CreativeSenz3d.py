VideoCapture capture( CAP_REALSENSE );
for(;;)
{
 Mat depthMap;
 capture >> depthMap;
 
 if( waitKey( 30 ) >= 0 )
 break;
}





VideoCapture capture(CAP_REALSENSE);
for(;;)
{
 Mat depthMap;
 Mat image;
 Mat irImage;
 
 capture.grab();
 
 capture.retrieve( depthMap, CAP_INTELPERC_DEPTH_MAP );
 capture.retrieve( image, CAP_INTELPERC_IMAGE );
 capture.retrieve( irImage, CAP_INTELPERC_IR_MAP);
 
 if( waitKey( 30 ) >= 0 )
 break;
}





VideoCapture capture(CAP_REALSENSE);
capture.set( CAP_INTELPERC_DEPTH_GENERATOR | CAP_PROP_INTELPERC_PROFILE_IDX, 0 );
cout << "FPS " << capture.get( CAP_INTELPERC_DEPTH_GENERATOR+CAP_PROP_FPS ) << endl;





