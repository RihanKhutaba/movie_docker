from pymongo import MongoClient
import gridfs

connection = MongoClient("localhost", 27017)

database = connection['DB_NAME']

def writefile():

    fs = gridfs.GridFS(database)
    file = "poster_1.jpeg"
    with open(file, 'rb') as f:
         contents = f.read()
    fs.put(contents, filename="file")

def delfile():

    db = MongoClient().DB_NAME
    fs = gridfs.GridFS(db)
    fileid = fs.get_last_version(filename="file").id
    fs.delete(fileid)

