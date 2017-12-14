import os

temp_file_index=0
"it seems that we have a strange behavior here, the kivy will store the image with a given file name"
file_directory="/home/chengzhengqian/.windowsfilter/"
temp_file_name_pattern="/home/chengzhengqian/.windowsfilter/temp%d.xwd"
convert_file_name_pattern="/home/chengzhengqian/.windowsfilter/temp%d.png"
processed_file_name_pattern="/home/chengzhengqian/.windowsfilter/processed%d.png"

def update_index(index):
    global temp_file_index, temp_file_name, convert_file_name,processed_file_name
    temp_file_index=index
    temp_file_name=temp_file_name_pattern%temp_file_index
    convert_file_name=convert_file_name_pattern%temp_file_index
    processed_file_name=processed_file_name_pattern%temp_file_index

def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

        
ensure_directory(file_directory)        
update_index(0)

