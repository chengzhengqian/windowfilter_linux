'''module for capture the screen of a given windows id'''

import subprocess
from subprocess import Popen, PIPE
from skimage import io
from skimage.filters import try_all_threshold
import matplotlib.pyplot as plt
import configure 
import re

def get_wininfo(id):
    p=subprocess.Popen(["xwininfo","-id",id],stdout=PIPE)
    output,err=p.communicate(b"")
    result= (output.decode()).split("\n")[1]
    m=re.search("\"(.*)\"",result)
    if(m):
        return m.group(1)
    return "none"

def search_id(name="WindowsFilter"):
    p=subprocess.Popen(["xdotool","search","--name",name],stdout=PIPE)
    output,err=p.communicate(b"")
    return (output.decode()).split("\n")

    
def xwd_id(id):
    '''capture the screen of given windows, use xwininfo to find id'''
    p = subprocess.run(["xwd", "-id", id, "-out", configure.temp_file_name])


def convert_image():
    p = subprocess.run(["convert", configure.temp_file_name, configure.convert_file_name])


def process_image():
    global img, img_process
    img = io.imread(configure.convert_file_name)
    '''
    add image process code here, also, one can think about store them
    '''
    img_process=img
    io.imsave(configure .processed_file_name, img_process)


def caputure_window(id='0x6000012'):
    configure.update_patterns()
    xwd_id(id)
    convert_image()
    process_image()


if __name__=="__main__" :
    print(search_id())
    print(get_wininfo("0x6000012"))
