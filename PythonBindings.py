CV_EXPORTS_W void equalizeHist( InputArray src, OutputArray dst );


CV_EXPORTS_W void minEnclosingCircle( InputArray points,
 CV_OUT Point2f& center, CV_OUT float& radius );



class CV_EXPORTS_W CLAHE : public Algorithm
{
public:
 CV_WRAP virtual void apply(InputArray src, OutputArray dst) = 0;
 
 CV_WRAP virtual void setClipLimit(double clipLimit) = 0;
 CV_WRAP virtual double getClipLimit() const = 0;
}
    
    
    
     
CV_EXPORTS_W void integral( InputArray src, OutputArray sum, int sdepth = -1 );
 
CV_EXPORTS_AS(integral2) void integral( InputArray src, OutputArray sum,
 OutputArray sqsum, int sdepth = -1, int sqdepth = -1 );
 
CV_EXPORTS_AS(integral3) void integral( InputArray src, OutputArray sum,
 OutputArray sqsum, OutputArray tilted,
 int sdepth = -1, int sqdepth = -1 );



class CV_EXPORTS_W_SIMPLE DMatch
{
public:
 CV_WRAP DMatch();
 CV_WRAP DMatch(int _queryIdx, int _trainIdx, float _distance);
 CV_WRAP DMatch(int _queryIdx, int _trainIdx, int _imgIdx, float _distance);
 
 CV_PROP_RW int queryIdx; // query descriptor index
 CV_PROP_RW int trainIdx; // train descriptor index
 CV_PROP_RW int imgIdx; // train image index
 
 CV_PROP_RW float distance;
};
    
    
    
    class CV_EXPORTS_W_MAP Moments
{
public:
 CV_PROP_RW double m00, m10, m01, m20, m11, m02, m30, m21, m12, m03;
 CV_PROP_RW double mu20, mu11, mu02, mu30, mu21, mu12, mu03;
 CV_PROP_RW double nu20, nu11, nu02, nu30, nu21, nu12, nu03;
};
    
    
    
    class CV_EXPORTS_W UMat
{
public:
 // You would need to provide `static bool cv_mappable_to(const Ptr<Mat>& src, Ptr<UMat>& dst)`
 CV_WRAP_MAPPABLE(Ptr<Mat>);
 
 /! returns the OpenCL queue used by OpenCV UMat.
 // You would need to provide the method body in the binder code
 CV_WRAP_PHANTOM(static void* queue());
 
 // You would need to provide the method body in the binder code
 CV_WRAP_PHANTOM(static void* context());
 
 CV_WRAP_AS(get) Mat getMat(int flags CV_WRAP_DEFAULT(ACCESS_RW)) const;
};
    
    
    
    