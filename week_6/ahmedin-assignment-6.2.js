/*
============================================
; Title:  house.js
; Author: Professor Krasso
; Date:   22 April 2023
; Modified By: Yakut Ahmedin
; Description:  These queries are based on the house.js script provided in week six of the WEB 335 course GitHub repository.
;===========================================
*/

//1. Load the house.js script from the GitHub repository
load("Downloads/house.js");

//2. list of documents in the houses collection
db.houses.find();

//3. list of documents in the students collection
db.students.find();

//4. Insert the new student’s  document
db.students.insertOne({ firstName: "Weyne", lastName: "Adem", studentId: "s1019", houseId: "h1011"});

// check  if the student is added
db.students.find({ firstName: "Weyne" });

//5. delete the student
db.students.deleteOne({ firstName: "Weyne" });

// check the document was deleted from the student's collection:
db.students.find({ firstName: "Weyne" });

//6. show a list of students by house 
db.houses.aggregate([{ $lookup: { from: "students", localField: "houseId", foreignField: "houseId", as: "students"}}]);

//7.show a list of students for house Gryffindor 
db.houses.aggregate([{ $match: {houseId: "h1007"}},{ $lookup: { from: "students", localField: "houseId", foreignField: "houseId", as: "students" }}])

//8. show a list of students for the Eagle mascot
db.houses.aggregate([{$match: {mascot: "Eagle"}},{$lookup: {from: "students", localField: "houseId", foreignField: "houseId", as: "students"}}])
  
