temp_file_index=0
history_size=10
temp_file_name_pattern="/home/chengzhengqian/.windowsfilter/temp%d.xwd"
convert_file_name_pattern="/home/chengzhengqian/.windowsfilter/temp%d.png"
processed_file_name_pattern="/home/chengzhengqian/.windowsfilter/processed%d.png"

def update_patterns():
    global temp_file_index, temp_file_name, convert_file_name,processed_file_name
    temp_file_index+=1
    temp_file_index=temp_file_index%history_size
    temp_file_name=temp_file_name_pattern%temp_file_index
    convert_file_name=convert_file_name_pattern%temp_file_index
    processed_file_name=processed_file_name_pattern%temp_file_index


update_patterns()

