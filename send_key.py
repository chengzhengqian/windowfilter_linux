'''this module is used to send key to other windows'''

import subprocess

def send_key(host_id, target_id='0x6000012', keystroke="Down"):
    subprocess.run(["xdotool", "windowactivate", target_id])
    subprocess.run(["xdotool", "key", keystroke])
    subprocess.run(["xdotool", "windowactivate", host_id])


if __name__=="__main__" :
    send_key()
