import pymongo
import certifi


con_str = "mongodb+srv://weeraphot:Test1234@cluster0.lubtx7z.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database('organic')