use("tp5")
// db.sportifs.find()

// 1
// db.sportifs.aggregate([
//     {
//         $match: {
//             Age: {$gte:20, $lte:30}
//         }
//     },
//     {
//        $project: {
//             _id: 1,
//             nom: "$Nom",
//             prenom: "$Prenom"
//     }
//     }
// ])

// 2
// db.gymnase.find()
// db.gymnase.aggregate([
//     {
//         $match: {
//             Ville: { $in: ["VILLETANEUSE", "SARCELLES"] },
//             Surface: {$gte: 400}
//         }
//     }
// ])

// 3
// db.sportifs.find()
// db.sportifs.aggregate([
//     {
//         $match: {
//             "Sports.Jouer" : "Hand ball"
//         }
//     },
//     {
//         $project:{
//             _id: 1,
//             Nom:1
//         }
//     }
// ])

// 4 
// db.sportifs.find()
// db.sportifs.aggregate([
//     {
//         $match: {
//             "Sports.Jouer" : {$exists:false}
//         }
//     },
//     {
//         $project:{
//             _id: 1,
//             Nom:1
//         }
//     }
// ])

// 5
// db.gymnase.find()
// db.gymnase.aggregate([
//     {
//         $match: {
//             "Seances.Jour" : {$nin: ["dimanche", "Dimanche"]}
//         }
//     }
// ])

// 6
// db.gymnase.find()
// db.gymnase.aggregate([
//     {
//         $match: {
//             "Seances.Libelle" : {$nin :['Handball', 'Hockey']}
//         }
//     }
// ])

// 7 

// db.gymnase.find()
// db.sportifs.find()

// db.sportifs.aggregate({
//     $lookup: {
//         from: "gymnase", 
//         localField: "IdSportif", 
//         foreignField: "Seances.IdSportifEntraineur", 
//         as: "sportif"
// }});

// 8 

// db.sportifs.aggregate(
//     { $match:
//         {
//             Nom: "KERVADEC"
//         }
// })

// db.sportifs.aggregate(
//     { $match:
//         {
//             IdSportif: 1
//         }
// })


// 9 

// db.sportifs.aggregate([
//     {
//         $match: {
//             "Sports.Jouer" : "Basket ball"
//         }
//     },
//     {
//         $group: {
//           _id: "Age",
//           moyenne_age: {$avg: "$Age"}
//         }
//     }
// ])


// 10
// db.sportifs.find()

// db.sportifs.aggregate([
//   {
//     $match: {
//       "Sports.Entrainer": { $in: ["Hand ball", "Basket ball"] }
//     }
//   },
//   {
//     $match: {
//       "Sports.Entrainer": { $nin: ["Hockey", "Volley ball","Ping pong","Boxe"] } 
//     }
//   },
//   {
//     $project: {
//         _id: 1,
//         Sports: 1
//     }
//   }
// ])

