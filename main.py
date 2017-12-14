import threading
import ui
import rlcompleter
import readline
import capture
import re

class ConsoleThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        ui.help=help
        input("press key to set main window id (ui.MWID) and windows")
        ui.MWID=capture.search_id()[0]
        print("find {0}".format(ui.MWID))
        l()
        while True:
            readline.parse_and_bind("tab: complete")
            command = input(">>>")
            try:
                exec(command)
            except Exception as e:
                print(e)
            except KeyboardInterrupt:
                exit()

def ls():
    '''API list target'''
    name=input("windows key word:")
    list_ids=capture.search_id(name)
    id_pattern="\d+"
    ui.list_ids=[id for id in list_ids if re.match(id_pattern,id)]
    for index, id in enumerate(ui.list_ids):
        print(index, capture.get_wininfo(id))

def set():
    index=input("windows index:")
    ui.list_index=int(index)

def l():
    ls()
    set()
    
def help():
    print("use ls() to list, set() to set index")
    
if __name__ == "__main__":
    console=ConsoleThread()
    console.start()
    ui.WindowsFilter().run()
