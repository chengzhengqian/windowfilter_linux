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


def xwd_id(id, config):
    '''capture the screen of given windows, use xwininfo to find id'''
    p = subprocess.run(
        ["xwd", "-silent", "-id", id, "-out", config.temp_file_name])


def clear_xwd(config=0):
    p = subprocess.run(["rm",  config.temp_file_name])


def convert_image(config=0):
    p = subprocess.run(
        ["convert", config.temp_file_name, config.convert_file_name])





def process_image(config):
    global img, img_process
    img = io.imread(config.convert_file_name)
    '''
    add image process code here, also, one can think about store them
    python is way to slow in doing this job
    '''
    imageProcess.defaulProcess.processBitmap(img)
    io.imsave(config .processed_file_name, img)


def caputure_window(id='0x6000012', config=0):
    xwd_id(id, config)
    convert_image(config)
    process_image(config)
    clear_xwd(config)


def update_processed_image(config):
    process_image(config)


class CaptureThread (threading.Thread):

    '''caputure the background pages, use page down as default
    forward_number=0 indicates that we just processing the Bitmap
    '''

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

    def send_key_stroke_and_capture(self, config):
        if(self.next_page_command != ""):
            print("send ", self.next_page_command)
            send_key.send_key(
                self.host_id, self.target_id, keystroke=self.next_page_command)
            time.sleep(0.1)
        else:
            print("only capture content")
        caputure_window(self.target_id, config)

    def run(self):
        current_configure = configure.conf(self.init_index)
        if(self.forward_number == 0):
            print("update processed image only")
            '''creat configure from index'''
            update_processed_image(current_configure)
        else:
            for i in range(self.forward_number):
                print(self.init_index, " is captured")
                self.send_key_stroke_and_capture(current_configure)
                self.init_index += 1
                current_configure = configure.conf(self.init_index)


if __name__ == "__main__":
    print(search_id())
    print(get_wininfo("0x6000012"))
