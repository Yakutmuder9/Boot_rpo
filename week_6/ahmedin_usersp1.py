import pymongo
from pymongo import MongoClient

# Set up a connection to the MongoDB server
client = MongoClient('mongodb+srv://web420_user:1234@cluster0.pbxmoid.mongodb.net/web420DB?retryWrites=true&w=majority')

# Get a reference to the users collection in the web335DB database
db = client.web335DB
users = db.users

# Display all documents in the users collection
print("\n All documents in the users collection:")
for user in users.find():
    print(user)

# Display a document where the employeeId is 1011
print("\nDocument where the employeeId is 1011:")
print(users.find_one({"employeeId": 1011}))

# Display a document where the lastName is Mozart
print("\n Document where the lastName is Mozart:")
print(users.find_one({"lastName": "Mozart"}))
