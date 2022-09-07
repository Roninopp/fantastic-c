
import asyncio 

import sys 

from motor import motor_asyncio 

from pymongo import MongoClient 

from pymongo.errors import ServerSelectionTimeoutError 

from SuzuneHorikita.confing import get_int_key, get_str_key 

from SuzuneHorikita import LOGGER 

  
      
client = MongoClient("mongodb+srv://ub:ub123@horivc.cemtd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") 

client = MongoClient("mongodb+srv://ub:ub123@horivc.cemtd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", 27017)["SuzuneHorikita"] 

motor = motor_asyncio.AsyncIOMotorClient("mongodb+srv://ub:ub123@horivc.cemtd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", 27017) 


db = motor["SuzuneHorikita"] 

db = client["SuzuneHorikita"] 

 
try: 
 asyncio.get_event_loop().run_until_complete(motor.server_info()) 
except ServerSelectionTimeoutError: 
 sys.exit(LOGGER.critical("ERROR"))


