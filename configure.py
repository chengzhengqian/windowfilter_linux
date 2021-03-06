import os

temp_file_index=0
"it seems that we have a strange behavior here, the kivy will store the image with a given file name"
file_directory="/home/chengzhengqian/.windowsfilter/"
temp_file_name_pattern="/home/chengzhengqian/.windowsfilter/temp_%s_%d.xwd"
convert_file_name_pattern="/home/chengzhengqian/.windowsfilter/temp_%s_%d.png"
processed_file_name_pattern="/home/chengzhengqian/.windowsfilter/processed_%s_%d.png"

class  conf:
    '''a class to hold a temperature configuration, necessary in multithread'''
    def __init__(self,index,book_name):
        self.temp_file_index=index
        self.temp_file_name=temp_file_name_pattern%(book_name,self.temp_file_index)
        self.convert_file_name=convert_file_name_pattern%(book_name,self.temp_file_index)
        self.processed_file_name=processed_file_name_pattern%(book_name,self.temp_file_index)
        print(self.processed_file_name)

def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

        
ensure_directory(file_directory)        


