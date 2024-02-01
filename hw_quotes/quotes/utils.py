from pymongo import MongoClient

connection_string = 'mongodb+srv://the10or:ZFhToxXpJj2Wu9j3@cluster0.9va9jbs.mongodb.net/authors_quotes?retryWrites=true&w=majority'
client = MongoClient(connection_string)
db = client['authors_quotes']


# def get_db_handle(db_name, host, port, username, password):
#     client = MongoClient(
#         host=host, username=username, password=password
#     )
#     db_handle = client['db_name']
#     return db_handle, client
