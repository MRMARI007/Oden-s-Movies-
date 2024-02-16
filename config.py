#(©)CodeXBotz




import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("6467531922:AAEQoD3p0kQB9YTKZTHBkNU1m2NtHhgId9s", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("27494774", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("65f2c43c01f4757dcc875de35249829b", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("-1001649343645", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("2136908929", ""))

#Port
PORT = os.environ.get("PORT", "8030")

#Database
DB_URI = os.environ.get("mongodb+srv://SaturuGojo:SaturuGojo@cluster0.ikrb9xv.mongodb.net/?retryWrites=true&w=majority", "")
DB_NAME = os.environ.get("SaturuGojo", "filesharexbot")
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DB_URI)


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002058531177"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002058531177"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first}\n\nI am a file store bot Powered by @Animes_xyz ⚡</b>.")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "6680981259").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Sorry Dude ned MChann</b>\n\n<b>So Please Joinhaning Your Favourite Animes ⚡</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫 Please Avoid Direct Messages. I'm Here merely for file sharing!"

ADMINS.append(OWNER_ID)
ADMINS.append(6208886200)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
