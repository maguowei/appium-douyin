from pymongo import MongoClient

client = MongoClient('mongodb://root:example@127.0.0.1:27017/')
db = client['douyin']


# def query_uids():
#     db['nearby'].distinct('uuid')