use("restaurant")

//1
// db.restaurant.aggregate([
//     {
//         $limit:10
//     }
// ])

//2
// db.restaurant.aggregate([
//     {
//         $limit:10
//     },
//     {
//         $sort:{name:-1}
//     }

// ])

//3
// db.restaurant.find({"address line 2" : "Brooklyn"}).limit(10).sort({name: -1})

//4
// db.restaurant.aggregate([
//     {
//         $match : {"address line 2" : "Brooklyn"}
//     },
//     {
//         $sort:{name:-1}
//     },
//     {
//         $limit:10
//     }
// ])

//4
// db.restaurant.find({}, { name: 1, address:1}).limit(10).sort({name: -1})

//5
// db.restaurant.find({}, { address: 0}).limit(10).sort({name: -1})

//7
// db.restaurant.aggregate([
//     {
//         $limit:10 
//     },
//     {
//         $addFields:{
//             nombreAvis: {$size:["$grades"]}
//         }
//     },
//     {
//         $sort:{nombreAvis}
//     }
// ])

// 8
// db.restaurant.aggregate([
//   {
//     $project: {                                     
//       nom: { $toUpper: "$name" },  
//       quartier: "$borough"          
//     }
//   },
//   { $limit: 10 }               
// ])


// 9
//  db.restaurant.aggregate([
//   {
//     $project: {               
//       name: { $toUpper: "$name" },  
//       address : {$substrCP: ["$borough", 0, 3] }   
//     }
//   },
//   { $limit: 10 }               
// ])

// 10
// db.restaurant.aggregate({  
//      $count : "name"   
// })

//11
// db.restaurant.aggregate([
//   {
//     $group: {
//       _id: "$borough", 
//       nombreRestaurant : {$sum: 1}
//     }
//   }
// ])




