# (c) JigarVarma2005

import os

class Config(object)
    INFOPIC = bool(os.environ.get("INFOPIC", True))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", @shoto_Xxrobot)
    EVENT_LOGS = os.environ.get("EVENT_LOGS", -1001769989575)
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    URL = os.environ.get("URL", "")  # Does not contain token
    PORT = int(os.environ.get("PORT", 5000))
    CERT_PATH = os.environ.get("CERT_PATH")
    API_ID = os.environ.get("API_ID", 13849191)
    API_HASH = os.environ.get("API_HASH", c1b434defccacad6063758c9a7d76d5d)
    ERROR_LOG = os.environ.get("ERROR_LOG", None)
    DB_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", postgresql://onqxhomv:SeoIutAALq7JqboOKOVkPA7_94iPasjf@drona.db.elephantsql.com/onqxhomv)
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", mongodb://Abhinav:abhinav123@cluster0-shard-00-00.cjtno.mongodb.net:27017,cluster0-shard-00-01.cjtno.mongodb.net:27017,cluster0-shard-00-02.cjtno.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-8qr3b0-shard-0&authSource=admin&retryWrites=true&w=majority)
    ARQ_API = os.environ.get("ARQ_API", None)
    DONATION_LINK = os.environ.get("DONATION_LINK")
    LOAD = os.environ.get("LOAD", "").split()
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", None)
    VIRUS_API_KEY = os.environ.get("VIRUS_API_KEY", None)
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False))
    WORKERS = int(os.environ.get("WORKERS", 8))
    BAN_STICKER = os.environ.get("BAN_STICKER", "CAADAgADOwADPPEcAXkko5EB3YGYAg")
    ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)
    CASH_API_KEY = os.environ.get("CASH_API_KEY", None)
    TIME_API_KEY = os.environ.get("TIME_API_KEY", None)
    WALL_API = os.environ.get("WALL_API", None)
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", @ignitetechdivision)
    SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None)
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    LASTFM_API_KEY = os.environ.get("LASTFM_API_KEY", None)
    CF_API_KEY = os.environ.get("CF_API_KEY", None)
    WELCOME_DELAY_KICK_SEC = os.environ.get("WELCOME_DELAY_KICL_SEC", None)
    BOT_ID = int(os.environ.get("BOT_ID", 5320317765))
    ARQ_API_URL = "https://arq.hamker.in"
    ARQ_API_KEY = ARQ_API
    REDIS_URL = os.environ.get("REDIS_URL", redis://default:HSeBWqLvstwvCF5NItzd@containers-us-west-43.railway.app:5521)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 5320317765:AAEKJ4C0RdJx1qKPuaYN20FNCXpV1ZUVcJE)
