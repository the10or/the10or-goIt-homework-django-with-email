from pymongo import MongoClient

connection_string = "mongodb+srv://the10or:ZFhToxXpJj2Wu9j3@cluster0.9va9jbs.mongodb.net/authors_quotes?retryWrites=true&w=majority"
client = MongoClient(connection_string)
db = client["authors_quotes"]
