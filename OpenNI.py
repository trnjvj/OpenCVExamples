VideoCapture capture( CAP_OPENNI );
for(;;)
{
 Mat depthMap;
 capture >> depthMap;
 
 if( waitKey( 30 ) >= 0 )
 break;
}




VideoCapture capture(0); // or CAP_OPENNI
for(;;)
{
 Mat depthMap;
 Mat bgrImage;
 
 capture.grab();
 
 capture.retrieve( depthMap, CAP_OPENNI_DEPTH_MAP );
 capture.retrieve( bgrImage, CAP_OPENNI_BGR_IMAGE );
 
 if( waitKey( 30 ) >= 0 )
 break;
}




VideoCapture capture( CAP_OPENNI );
capture.set( CAP_OPENNI_IMAGE_GENERATOR_OUTPUT_MODE, CAP_OPENNI_VGA_30HZ );
cout << "FPS " << capture.get( CAP_OPENNI_IMAGE_GENERATOR+CAP_PROP_FPS ) << endl;




bool isImageGeneratorPresent = capture.get( CAP_PROP_OPENNI_IMAGE_GENERATOR_PRESENT ) != 0; // or == 1





