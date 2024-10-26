#Join @dev_gagan

from telethon.errors import FloodWaitError
from datetime import datetime as dt, timedelta
import asyncio
import sys
from pyrogram import Client
import asyncio
import uvloop
from pyrogram.errors import FloodWait
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from decouple import config
import logging, time
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

uvloop.install()

API_ID = "24894984" config("API_ID", default=None, cast=int)
API_HASH = "4956e23833905463efb588eb806f9804" config("API_HASH", default=None)
BOT_TOKEN = "7601293855:AAG0J1lG04wfEnK9J1GnImfOWN7X_2wyaS4" config("BOT_TOKEN", default=None)
SESSION = "BQDNvmIAc2pCfy2TNwMsVQLUU3GjqNuJlYYq_mjlI6P06s6bwaXavLJwzSpREBdv2ckEr8oy-ZAk5FDVLW9EWqpee2b98CWmUDu2xq8kMveTugmPun9Y19IFNTc7d78Tc5NzAtjusgPETXDuUyxP7TIF25HDD6MyzfoRMJMNQNa7jtdMKehOSYdxged-mdYluK7PecGD62AL9NIuaat5H91UAdL8qyNqYjNlkRzi-C0BKBGIIn_MeHiQRK12QKe6Bv8E4DFHxi5wKS2DGYpr1foaVxgHmibV7ly1rZ2e-_6y-5A7COhAUTQvNF0sCCfsei3mS7T1kVgSy2Kun4QfE5xgRAJDQwAAAAA1y9g-AA" config("SESSION", default=None)
FORCESUB = "Targetallcourse" config("FORCESUB", default=None)
AUTH = "902551614" config("AUTH", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "ggnbot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    sys.exit(1)
