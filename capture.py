'''module for capture the screen of a given windows id'''

import subprocess
from subprocess import Popen, PIPE
from skimage import io
from skimage.filters import try_all_threshold
import matplotlib.pyplot as plt
import configure
import re
import threading
import send_key
import time
import imageProcess 

def get_wininfo(id):
    p = subprocess.Popen(["xwininfo", "-id", id], stdout=PIPE)
    output, err = p.communicate(b"")
    result = (output.decode()).split("\n")[1]
    m = re.search("\"(.*)\"", result)
    if(m):
        return m.group(1)
    return "none"


def search_id(name="WindowsFilter"):
    p = subprocess.Popen(["xdotool", "search", "--name", name], stdout=PIPE)
    output, err = p.communicate(b"")
    return (output.decode()).split("\n")


def xwd_id(id):
    '''capture the screen of given windows, use xwininfo to find id'''
    p = subprocess.run(["xwd", "-silent","-id", id, "-out", configure.temp_file_name])


def clear_xwd():
    p = subprocess.run(["rm",  configure.temp_file_name])


def convert_image():
    p = subprocess.run(
        ["convert", configure.temp_file_name, configure.convert_file_name])


thread_hold = 170


def process_image():
    global img, img_process
    img = io.imread(configure.convert_file_name)
    '''
    add image process code here, also, one can think about store them
    python is way to slow in doing this job
    '''

    # w, h, c = img.shape
    # for i in range(w):
    #     for j in range(h):
    #         c = sum(img[i, j,:])
    #         if(c < thread_hold*3):
    #             img[i, j,:] = [0, 0, 0]
    imageProcess.defaulProcess.processBitmap(img)
    io.imsave(configure .processed_file_name, img)
    


def caputure_window(id='0x6000012', index=0):
    configure.update_index(index)
    xwd_id(id)
    convert_image()
    process_image()
    clear_xwd()

def update_processed_image(index):
    configure.update_index(index)
    process_image()
    

class CaptureThread (threading.Thread):

    '''caputure the background pages, use page down as default'''

    def __init__(self, host_id, target_id, init_index=0, next_page_command="Page_Down", forward_number=1):
        '''
        init_index is the first index to be written with
        forward_number, the number of pages added to history
        '''
        threading.Thread.__init__(self)
        self.init_index = init_index
        self.next_page_command = next_page_command
        self.host_id = host_id
        self.target_id = target_id
        self.forward_number = forward_number

        
    def send_key_stroke_and_capture(self):
        if(self.next_page_command!=""):
            print("send ", self.next_page_command)
            send_key.send_key(
                self.host_id, self.target_id, keystroke=self.next_page_command)
            time.sleep(0.1)
        else:
            print("only capture content")
        caputure_window(self.target_id, self.init_index)

    def run(self):
        if(self.forward_number==0):
            print("update processed image only")
            update_processed_image(self.init_index)
        else:
            for i in range(self.forward_number):
                print(self.init_index, " is captured")
                self.send_key_stroke_and_capture()
                self.init_index += 1


if __name__ == "__main__":
    print(search_id())
    print(get_wininfo("0x6000012"))
