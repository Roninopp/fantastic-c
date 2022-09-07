
import asyncio 

import sys 

from motor import motor_asyncio 

from pymongo import MongoClient 

from pymongo.errors import ServerSelectionTimeoutError 

from SuzuneHorikita.confing import get_int_key, get_str_key 

from SuzuneHorikita import LOGGER 

  
      
client = MongoClient("mongodb://Shoto:abhinav123@#@ac-0nui3uu-shard-00-00.xdb8kfi.mongodb.net:27017,ac-0nui3uu-shard-00-01.xdb8kfi.mongodb.net:27017,ac-0nui3uu-shard-00-02.xdb8kfi.mongodb.net:27017/?ssl=true&replicaSet=atlas-3b648r-shard-0&authSource=admin&retryWrites=true&w=majority") 

client = MongoClient("mongodb://Shoto:abhinav123@#@ac-0nui3uu-shard-00-00.xdb8kfi.mongodb.net:27017,ac-0nui3uu-shard-00-01.xdb8kfi.mongodb.net:27017,ac-0nui3uu-shard-00-02.xdb8kfi.mongodb.net:27017/?ssl=true&replicaSet=atlas-3b648r-shard-0&authSource=admin&retryWrites=true&w=majority", 27017)["SuzuneHorikita"] 

motor = motor_asyncio.AsyncIOMotorClient("mongodb://Shoto:abhinav123@#@ac-0nui3uu-shard-00-00.xdb8kfi.mongodb.net:27017,ac-0nui3uu-shard-00-01.xdb8kfi.mongodb.net:27017,ac-0nui3uu-shard-00-02.xdb8kfi.mongodb.net:27017/?ssl=true&replicaSet=atlas-3b648r-shard-0&authSource=admin&retryWrites=true&w=majority", 27017) 

db = motor["SuzuneHorikita"] 

db = client["SuzuneHorikita"] 

 
try: 
 asyncio.get_event_loop().run_until_complete(motor.server_info()) 
except ServerSelectionTimeoutError: 
 sys.exit(LOGGER.critical("ERROR"))


