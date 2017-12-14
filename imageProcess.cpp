/****IMAGEPROCESS_CPP****/
#include "imageProcess.h"
#include <iostream>
using namespace std;
namespace ImageProcess {

FilterProcess::FilterProcess() {}

void FilterProcess::print_info() { cout << "FilterProcess:" << endl; }

void FilterProcess::processBitmap(unsigned char *img, int width, int height,
                                  int channel) {
  cout << "precessBitmap: w,h,c"
       << "," << width << "," << height << "," << channel << endl;

  for (int i = 0; i < width; i++)
    for (int j = 0; j < height; j++)
      for (int c = 0; c < channel; c++) {
        int index = i * height * channel + j * channel + c;
        if (img[index] < filters[c]) {
          img[index] = 0;
        } else {
          img[index] = 255;
        }
      }
  cout <<"complete."<<endl;
}

void FilterProcess::setfilter(int a, int b, int c) {
  filters[0] = a;
  filters[1] = b;
  filters[2] = c;
}

/* ++++class:FilterProcess++++namespace:ImageProcess++++ */

/* ####namespace:ImageProcess#### */
}
