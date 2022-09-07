
import asyncio 

import sys 

from motor import motor_asyncio 

from pymongo import MongoClient 

from pymongo.errors import ServerSelectionTimeoutError 

from SuzuneHorikita.confing import get_int_key, get_str_key 

from SuzuneHorikita import LOGGER 

  
      
client = MongoClient("mongodb://Abhinav:abhinav123@cluster0-shard-00-00.cjtno.mongodb.net:27017,cluster0-shard-00-01.cjtno.mongodb.net:27017,cluster0-shard-00-02.cjtno.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-8qr3b0-shard-0&authSource=admin&retryWrites=true&w=majority") 

client = MongoClient("mongodb://Abhinav:abhinav123@cluster0-shard-00-00.cjtno.mongodb.net:27017,cluster0-shard-00-01.cjtno.mongodb.net:27017,cluster0-shard-00-02.cjtno.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-8qr3b0-shard-0&authSource=admin&retryWrites=true&w=majority", 27017)["SuzuneHorikita"] 

motor = motor_asyncio.AsyncIOMotorClient("mongodb://Abhinav:abhinav123@cluster0-shard-00-00.cjtno.mongodb.net:27017,cluster0-shard-00-01.cjtno.mongodb.net:27017,cluster0-shard-00-02.cjtno.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-8qr3b0-shard-0&authSource=admin&retryWrites=true&w=majority", 27017) 


db = motor["SuzuneHorikita"] 

db = client["SuzuneHorikita"] 

 
try: 
 asyncio.get_event_loop().run_until_complete(motor.server_info()) 
except ServerSelectionTimeoutError: 
 sys.exit(LOGGER.critical("ERROR"))


