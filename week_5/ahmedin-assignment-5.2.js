/*
============================================
; Title:  user.js
; Author: Professor Krasso
; Date:   16 April 2023
; Modified By: Yakut Ahmedin
; Description:  These queries are based on the user.js script provided in week four of the WEB 335 course GitHub repository.
;===========================================
*/

// Load the user.js script from the GitHub repository
load("Downloads/user.js");

// Insert the new user document
db.users.insertOne({ firstName: "Antonio", lastName: "Vivaldi", employeeId: "1013", email: "avivaldi@me.com", dateCreated: new Date()});

// Update Mozart's email address
db.users.updateOne({ lastName: "Mozart" }, { $set: { email: "mozart@me.com" }});

// verify the email update
db.users.findOne({ lastName: "Mozart" });

// users collection with firstName, lastName, and email fields
db.users.aggregate([{ $project: { firstName: 1, lastName: 1, email: 1 } }]);
