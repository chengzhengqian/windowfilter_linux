all: imageProcess.so

r: all
	python3.6 main.py

cc=g++-4.9
para= -std=c++11
imageProcess.so:imageProcess.o imageProcess_p.o
	$(cc) -shared -pthread -o $@ $^  $(lib) 
imageProcess.o:imageProcess.cpp imageProcess.h
	$(cc) -c -fPIC -O3 $(para) $(inc) -o $@ $<
imageProcess.cc:imageProcess.pyx imageProcess.pxd imageProcess.h
	cython --cplus -o $@ $<
imageProcess_p.o:imageProcess.cc
	$(cc) -c -fPIC -O3 $(para) -I/home/chengzhengqian/anaconda3/include/python3.6m  $(inc) -o $@ $<

