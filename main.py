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
        ui.help = help
        input("press key to set main window id (ui.MWID) and windows")
        ui.MWID = capture.search_id()[0]
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

list_window_names = []


def ls():
    '''API list target'''
    global list_window_names
    list_window_names = []
    name = input("windows key word:")
    list_ids = capture.search_id(name)
    id_pattern = "\d+"
    ui.list_ids = [id for id in list_ids if re.match(id_pattern, id)]
    for index, id in enumerate(ui.list_ids):
        list_window_names.append(str(capture.get_wininfo(id)))
        print(index, capture.get_wininfo(id))


def set():
    index = input("windows index:")
    try:
        ui.list_index = int(index)
        ui.current_book_name = list_window_names[ui.list_index]
        bookinfo= {
            "current_index": -1,
            "cached_index": -1,
            "list_index": ui.list_index,
            "list_ids": list(ui.list_ids),
            "is_finished_circle": False
        }
        set_bookinfo(bookinfo)
        ui.book_list[ui.current_book_name]=bookinfo
    except Exception as e:
        print(e)


def l():
    '''list and set  windows and add to books'''
    ls()
    set()


def store_bookinfo(book_info):
    book_info["current_index"] = ui.current_index
    book_info["cached_index"] = ui.cached_index
    book_info["list_index"] = ui.list_index
    book_info["list_ids"] = ui.list_ids
    book_info["is_finished_circle"] = ui.is_finished_circle


def set_bookinfo(book_info):
    ui.current_index = book_info["current_index"]
    ui.cached_index = book_info["cached_index"]
    ui.list_index = book_info["list_index"]
    ui.list_ids = book_info["list_ids"]
    ui.is_finished_circle = book_info["is_finished_circle"]


def lb():
    "list book and choose one"
    books = []
    index = 0
    for i in ui.book_list:
        if(i == ui.current_book_name):
            print("*", index, i)
            book_info = ui.book_list[i]
            store_bookinfo(book_info)
        else:
            print(index, i)
        books.append(i)
        index += 1

    try:
        a = input("select book")
        index_ = int(a)
        if(index_ >= 0 and index_ < index):
            ui.current_book_name = books[index_]
            book_info = ui.book_list[ui.current_book_name]
            set_bookinfo(book_info)
    except Exception as e:
        print(e)


def help():
    '''help hint if user does not set window yet'''
    print("use ls() to list, set() to set index")

if __name__ == "__main__":
    console = ConsoleThread()
    console.start()
    ui.WindowsFilter().run()
