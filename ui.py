import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
import configure
import capture
import send_key
import time
'''
ID for main window and target windows
'''
MWID = 0
list_ids = []
list_index = -1
current_index = -1
cached_index = -1
is_ready_cached = False
'''store the file in a ring'''
MAX_NUMBER = 500
is_finished_circle = False


class MainWindow(Image):

    def __init__(self, **kwargs):
        global is_ready_cached
        super(MainWindow, self).__init__(**kwargs)
        Window.bind(on_key_down=self.on_key_down)
        self.source = "readme.png"
        self.is_ready_cached = True
        self.nocache = True

    def check_MWID(self):
        if(MWID == 0):
            print("set MWD first, ")
            help()
            return False
        return True

    def check_INDEX(self):
        if(list_index < 0 or list_index >= len(list_ids)):
            print("set target index ")
            help()
            return False
        return True

    # self.source= (configure.processed_file_name)

    def on_key_down(self, object, keycode, scancode, name, modifiers):
        '''handles the key input'''
        global cached_index, current_index, is_ready_cached, is_finished_circle
        print("key pressed:", keycode, scancode, name, modifiers)
        if(name == 'q'):
            exit()
        if(not self.check_MWID()):
            return
        if(not self.check_INDEX()):
            return
        try:
            if(cached_index < 0):
                p = capture.CaptureThread(
                    MWID, list_ids[list_index], init_index=0,
                                          next_page_command="", forward_number=1)
                cached_index = 0
                current_index = -1
                is_ready_cached = False
                p.start()

            '''
            show original form
            '''
            if(name == "o"):
                print("nocache:", self.nocache)
                self.source = configure.convert_file_name_pattern % (
                    current_index)
            '''
            show processed form
            '''
            if(name == "u"):
                print("update processing")
                '''forward_number=0 ensure it only updates from cached image'''
                self.source = configure.convert_file_name_pattern % (
                    current_index)
                p = capture.CaptureThread(
                    MWID, list_ids[list_index], current_index,
                                          next_page_command="", forward_number=0)
                p.start()
            if(name == "c"):
                '''just recapture the end of cached images'''
                print("just recapture ", cached_index)
                # cached_index = cached_index+1
                p = capture.CaptureThread(
                    MWID, list_ids[list_index], cached_index,
                                          next_page_command="", forward_number=1)
                p.start()

            if(name == "i"):
                print("nocache:", self.nocache)
                self.source = configure.processed_file_name_pattern % (
                    current_index)
            if(name == "p"):
                can_go_back=False
                if(is_finished_circle):
                    if(current_index !=(cached_index+1)%MAX_NUMBER):
                        can_go_back=True
                else:
                    if(current_index!=0):
                        can_go_back=True

                if(can_go_back):
                        current_index -= 1
                        current_index=current_index%MAX_NUMBER
                        self.source = configure.processed_file_name_pattern % (
                            current_index)                                    
                else:
                    print("begining of history!")
            if((name == "n" or name=="m") and is_ready_cached):
                '''advance the cached_index further if current_index=cached_index-1'''
                if(((current_index + 1) % MAX_NUMBER) == cached_index):
                    cached_index = cached_index + 1
                    if(cached_index==MAX_NUMBER):
                        is_finished_circle=True
                    cached_index = cached_index % MAX_NUMBER
                    if(name=="n"):
                        command="Page_Down"
                    else:
                        command="Page_Up"
                    p = capture.CaptureThread(
                        MWID, list_ids[list_index], cached_index,
                                          next_page_command=command, forward_number=1)
                    is_ready_cached = False
                    p.start()
                current_index += 1
                current_index = current_index % MAX_NUMBER
                self.source = configure.processed_file_name_pattern % (
                    current_index)
            if(name == "e"):
                print("end of cached images")
                current_index = cached_index
                cached_index = cached_index + 1
                cached_index = cached_index % MAX_NUMBER
                p = capture.CaptureThread(
                    MWID, list_ids[list_index], cached_index,
                                          next_page_command="Page_Down", forward_number=1)
                p.start()
                self.source = configure.processed_file_name_pattern % (
                    current_index)

        except Exception as e:
            print(e)

    def on_touch_down(self, touch):
        print(touch)


class MainLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.add_widget(MainWindow())


class WindowsFilter(App):

    def build(self):
        return MainLayout()
