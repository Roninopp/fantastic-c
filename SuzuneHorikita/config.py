# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open('{}/SuzuneHorikita/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]

class Config(object):
    #dont change
    LOGGER=True
    ALLOW_CHATS=True
    ALLOW_EXCL=False
    TEMP_DOWNLOAD_DIRECTORY="./"
    DEL_CMDS=False
    BAN_STICKER="kans"
    CERT_PATH=""
    PORT=8443
    WORKERS=8
    LOAD=""
    NO_LOAD="translation"
    MONGO_DB="Shoto"
    WEBHOOK=False
    BOT_API_URL="https://api.telegram.org/bot"
    
    #change
    WOLVES=[549, 530666]
    BOT_ID=
    DB_URL=
    JOIN_LOGGER=
    API_HASH=
    ARQ_API_URL="arq.hamker.dev"
    GENIUS_API_TOKEN=
    INFOPIC=True
    TIGERS=[1]
    API_ID=44
    BL_CHATS=[1]
    DB_URL2=
    TOKEN="5475gege59Odo"
    APP_HASH="45aabfaca993a6d"
    DEV_USERS=[5306]
    DRAGONS=[9763]
    APP_ID=6781
    SPAMWATCH_API="J968E_20LgxrKj0sIDBG~YqN2NRTbU"
    WALL_API="6950f559377140a4e1594c564cdca6a3" #gift from meow
    DEMONS=[1939576]
    SUPPORT_CHAT="IgniteTechDivision"
    OWNER_USERNAME="h"
    DONATION_LINK="https://www.paypal.me/PaulSonOfLars"
    EVENT_LOGS=
    OWNER_ID=5
    TIME_API_KEY="QLLLDV7SWFD3" #gift from meow
    ERROR_LOGS=
    BOT_NAME="Shoto"
    STRICT_GBAN=True
    REDIS_URL="redis://15446/-db"
    ARQ_API_KEY="SLSFXS-BKJCMT-"
    UPDATES_CHANNEL="IgniteTechUpdates"
    MONGO_DB_URL="mongodb+srv.net/?retrrity"
    BOT_USERNAME="jj"
    REM_BG_API_KEY="K2Rc"


class Production(Config):
    LOGGER=True


class Development(Config):
    LOGGER=True
