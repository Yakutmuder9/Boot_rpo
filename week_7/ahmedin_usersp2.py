""" 
    Title: ahmedin_myworld.py
    Author: Professor Krasso
    Date: 26 April 2023
    Modified By: Yakut Ahmedin
    Description: Exercise 7.3 – Python with MongoDB, Part 2.
"""

import pymongo
from pymongo import MongoClient

# Set up a connection to the MongoDB server
client = MongoClient('mongodb+srv://web420_user:1234@cluster0.pbxmoid.mongodb.net/web420DB?retryWrites=true&w=majority')

# Get a reference to the users collection in the web335DB database
db = client.web335DB
users = db.users

# Create a new user document
new_user = {"name": "John Doe", "email": "johndoe@example.com", "age": 30}
result = users.insert_one(new_user)
print("New user created with id:", result.inserted_id)

# Display the newly created document
print("New user document:")
print(users.find_one({"_id": result.inserted_id}))

# Update the email address of the document
users.update_one({"_id": result.inserted_id}, {"$set": {"email": "johndoe12@example.com"}})

# Display the updated document
print("Updated user document:")
print(users.find_one({"_id": result.inserted_id}))

# Store the id in a variable before deletion
document_id = result.inserted_id

# Delete the document
result = users.delete_one({"_id": document_id})
print(result.deleted_count, "document deleted.")

# Prove the document was deleted
print("User document after deletion:")
print(users.find_one({"_id": document_id}))

