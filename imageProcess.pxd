##****IMAGEPROCESS_PXD****##
cdef extern from "imageProcess.h" namespace "ImageProcess":

    cdef cppclass FilterProcess:
        void print_info()
        void processBitmap(unsigned char* img, int width, int height, int channel) nogil
        void setfilter(int a, int b, int c)
# ++++class:FilterProcess++++namespace:ImageProcess++++ #



# ####namespace:ImageProcess#### #
