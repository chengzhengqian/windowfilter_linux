##****IMAGEPROCESS_PYX****##
from imageProcess cimport *
import numpy as np
cimport numpy as np

cdef class FilterProcess_p:
    cdef FilterProcess* c_FilterProcess

    def __cinit__(self):
        self.c_FilterProcess = new FilterProcess()

    def __dealloc__(self):
        del self.c_FilterProcess

    def print_info(self,):
        return self.c_FilterProcess.print_info()

    def processBitmap(self,img):
        cdef int width, height, channel
        cdef np.ndarray[unsigned char, ndim=3, mode="c"] img_c
        width,height,channel=img.shape
        img_c=img
        with nogil:
            self.c_FilterProcess.processBitmap(&img_c[0,0,0], width, height, channel)


    def setfilter(self,int a, int b, int c):
        '''set threshold for rgb'''
        return self.c_FilterProcess.setfilter(a, b, c)


# ++++class:FilterProcess++++namespace:ImageProcess++++ #

defaulProcess=FilterProcess_p()
