#ifndef IMAGEPROCESS_H
#define IMAGEPROCESS_H
namespace ImageProcess{
  class FilterProcess{
  public:
    FilterProcess();//i
    void print_info();//w//d//i
    unsigned char filters[3]={220,220,220};
    void processBitmap(unsigned char* img, int width, int height, int channel);//w//d//i
    void setfilter(int a, int b, int c);//w//d//i
/* ++++class:FilterProcess++++namespace:ImageProcess++++ */
  };

  
/* ####namespace:ImageProcess#### */
}


#endif

