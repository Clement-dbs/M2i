use("users")

// db.users.insertOne({
//     name: "Chuck Norris", 
//     age: 77, 
//     hobbies : ["Karate", "Kung-fu", "Ruling the world"]
// })


// db.users.find({name: "Chuck Norris"})
// db.users.find({$and: [ {age: { $gt: 20 }},{age: { $lt:25 }}]})
db.users.find({$and: [{age: { $gt: 30 }},{age: { $lt:40 }}]}, {$and{gender: "male"}})



