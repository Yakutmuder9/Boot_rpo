/*
============================================
; Title:  user.js
; Author: Professor Krasso
; Date:   08 April 2023
; Modified By: Yakut Ahmedin
; Description:  These queries are based on the user.js script provided in week four of the WEB 335 course GitHub repository.
;===========================================
*/

// Load the user.js script from the GitHub repository
load("Downloads/user.js")

// Find all documents in the users collection
db.users.find()

// Find a user with an email address of jbach@me.com
db.users.find({email: "jbach@me.com"})

// Find a user with the last name of Mozart
db.users.find({lastName: "Mozart"})

// Find a user with a first name of Richard
db.users.find({firstName: "Richard"})

// Find a user with an employeeId of 1010
db.users.find({employeeId: "1010"})

