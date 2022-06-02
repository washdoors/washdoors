from pymongo import MongoClient
import urllib.parse
username = urllib.parse.quote_plus('rushi')
password = urllib.parse.quote_plus('Rushi_1192')
client = MongoClient('mongodb://%s:%s@127.0.0.1'%(username, password))

db = client['washdoors']

collections_list = db.list_collection_names()

if 'person' not in collections_list:
    db.create_collection('person')
else:
    print('person collection is already present')

if 'product' not in collections_list:
    db.create_collection('product')
else:
    print('product collection is present')

if 'order' not in collections_list:
    db.create_collection('order')
else:
    print('order collection is created')

client.close()