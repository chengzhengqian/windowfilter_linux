'''this module is used to send key to other windows'''

import subprocess

def send_key(host_id, target_id='0x6000012', keystroke="Down"):
    subprocess.run(["wmctrl","-i","-r",host_id,"-b","add,above"])
    subprocess.run(["xdotool", "windowactivate", target_id])
    subprocess.run(["xdotool", "key", keystroke])
    subprocess.run(["xdotool", "windowactivate", host_id])
    subprocess.run(["wmctrl","-i","-r",host_id,"-b","remove,above"])


if __name__=="__main__" :
    send_key()
