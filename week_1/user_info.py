""" 
    Title: user_info.py
    Author: Professor Krasso
    Date: 19 March 2023
    Modified By: Yakut Ahmedin
    Description: Assignment 1.4 Business Rules.
"""

users = {
    1: {
        'roles': ['Manager', 'Developer'],
        'dependents': ['John', 'Jane'],
        'birth_date': '1999-01-01'
    },
    2: {
        'roles': ['QA Engineer'],
        'dependents': ['David'],
        'birth_date': '1998-05-15'
    }
}

# retrieve roles and dependents for a user
def get_user_roles(user_id):
    return users[user_id]['roles']

def get_user_dependents(user_id):
    return users[user_id]['dependents']

# retrieve birth date for a user
def get_user_birth_date(user_id):
    return users[user_id]['birth_date']


user_id = 1
roles = get_user_roles(user_id)
dependents = get_user_dependents(user_id)
birth_date = get_user_birth_date(user_id)

print(f"User {user_id} has the following roles: {', '.join(roles)}")
print(f"User {user_id} has the following dependents: {', '.join(dependents)}")
print(f"User {user_id} birth date is: {(birth_date)}")
