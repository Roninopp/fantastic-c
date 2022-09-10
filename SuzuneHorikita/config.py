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
    BOT_ID="5320317765" 
    DB_URL="postgresql://onqxhomv:SeoIutAALq7JqboOKOVkPA7_94iPasjf@drona.db.elephantsql.com/onqxhomv" 
    JOIN_LOGGER="-1001769989575" 
    API_HASH="c1b434defccacad6063758c9a7d76d5d" 
    ARQ_API_URL="arq.hamker.dev"
    GENIUS_API_TOKEN="agjwjspa" 
    INFOPIC=True
    TIGERS=[1]
    API_ID="13849191"
    BL_CHATS=[1]
    DB_URL2="hsjajsjx" 
    TOKEN="5320317765:AAED165KTkdTctvtRN8iWXR8zo8Ms8RLNBc"
    APP_HASH="45aabfaca993a6d"
    DEV_USERS=[1956381927,5205241880, 5259427402, 5109376623, 965613832, 5145883564, 5132406765 ,5231333039, 5011317739 ,5147265129, 1073020871, 5306064258]
    DRAGONS=[5443567678 ,5146000168, 1904998702 ,1946139404, 2093473332, 1633072243]
    APP_ID=6781
    SPAMWATCH_API="J968E_20LgxrKj0sIDBG~YqN2NRTbU"
    WALL_API="6950f559377140a4e1594c564cdca6a3" #gift from meow
    DEMONS=[5555455171 ,2039336161, 5153636966 ,1243568995]
    SUPPORT_CHAT="IgniteTechDivision"
    OWNER_USERNAME="Redeye_Ghoul"
    DONATION_LINK="https://www.paypal.me/PaulSonOfLars"
    EVENT_LOGS="-1001769989575" 
    OWNER_ID="5122071509" 
    TIME_API_KEY="QLLLDV7SWFD3" #gift from meow
    ERROR_LOGS="-1001769989575" 
    BOT_NAME="Shoto"
    STRICT_GBAN=True
    REDIS_URL="redis://default:s3AtIUNofUPQ4zm5Fz8L@containers-us-west-88.railway.app:7458"
    ARQ_API_KEY="SLSFXS-BKJCMT-"
    UPDATES_CHANNEL="IgniteTechUpdates"
    MONGO_DB_URI="mongodb+srv://ub:ub123@horivc.cemtd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    BOT_USERNAME="Shoto_xxrobot"
    REM_BG_API_KEY="K2Rc"


class Production(Config):
    LOGGER=True


class Development(Config):
    LOGGER=True
