from pymongo import MongoClient
import urllib.parse
username = urllib.parse.quote_plus('rushi')
password = urllib.parse.quote_plus('Rushi_1192')
client = MongoClient('mongodb://%s:%s@127.0.0.1'%(username, password))

db = client['firstDatabase']

collection = db['firstCollection']

data = collection.find_one({'name':'Rushi123'})

print(data)

client.close()