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


class MainWindow(Image):

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        Window.bind(on_key_down=self.on_key_down)

    def check_MWID(self):
        if(MWID==0):
            print("set MWD first, ")
            help()
            return False
        return True

    def check_INDEX(self):
        if(list_index<0 or list_index>= len(list_ids)):
            print("set target index ")
            help()
            return False
        return True

    def on_key_down(self, object, keycode, scancode, name, modifiers):
        print(object, keycode, scancode, name, modifiers)
        if(name == 'q'):
            exit()
        if(not self.check_MWID()):
            return
        if(not self.check_INDEX()):
            return 
        if(name == "o"):
            self.source = configure.convert_file_name
        if(name == "i"):
            self.source = configure.processed_file_name
        if(name == "n"):
            send_key.send_key(MWID,target_id=list_ids[list_index],keystroke="Down")
            time.sleep(0.1)
            capture.caputure_window(list_ids[list_index])
            self.source = configure.processed_file_name

    def on_touch_down(self, touch):
        print(touch)


class MainLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.add_widget(MainWindow())


class WindowsFilter(App):

    def build(self):
        return MainLayout()
