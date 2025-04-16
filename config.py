import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8107410246:AAHg6qoPkmyAyA-Ne9yrjv6ovZwE97Y1vXs")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "27975779"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "378062eb0a32d8d6b1bbbe97cb63a75a")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002506142464"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "srkassistant")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1416841137"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Wrio:TWmfbZA0vF5YvdaN@cluster0.cockran.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Wrio")

#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "600"))


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1002003576723"))
#put 0 to disable
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002007663918"))#put 0 to disable
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1002047546753"))#put 0 to disable
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))#put 0 to disable

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "50"))

START_PIC = os.environ.get("START_PIC", "https://i.ibb.co/YzFqHky/photo-2025-04-15-09-14-30-7493465832589099024.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://i.ibb.co/hxqp9gQk/photo-2025-04-03-11-00-42-7489040182323183640.jpg")

# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
TOKEN = True if os.environ.get('TOKEN', "False") == "True" else False  #For Enable Token 

#TOKEN = False if os.environ.get('TOKEN', "FALSE") == 'FALSE' else False # For disable Token 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "modijiurl.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "b579e0c5eaa8014f26564fc534c3c6014df5e050")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 600)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "False")
TUT_VID = os.environ.get("TUT_VID","https://t.me/how_to_download_tamil/6")


HELP_TXT = "<b><blockquote>Tʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @Anime_Fusion_Tamil\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n Dᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/srkassistant>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></blockquote></b>"

ABOUT_TXT = "<b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/srkassistant>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/+gE8Utdmvn4kzZjE1>sʀᴋ ɴᴇᴛᴡᴏʀᴋ</a>\n◈ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/anime_fusion_tamil>ᴀɴɪᴍᴇ ғᴜsɪᴏɴ</a>\n◈ sᴇʀɪᴇs ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/webseries_flix>ᴡᴇʙsᴇʀɪᴇs ғʟɪx</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/srkassistant>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></blockquote></b>"


START_MSG = os.environ.get("START_MESSAGE", "<b><blockquote>Hᴇʟʟᴏ {first} ⚡</blockquote>\n<blockquote> ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</blockquote></b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "1416841137").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

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
   
