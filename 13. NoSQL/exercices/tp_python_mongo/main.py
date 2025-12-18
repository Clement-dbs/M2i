from pymongo import MongoClient
from datetime import datetime



if __name__ == "__main__":

      
    print("=== Configuration ===")
    uri = "mongodb://admin:password@localhost:27017/?authSource=admin"
    client = MongoClient(uri)

    db = client["tp_python"]
    collection = db["students"]

    # 1
    # print(f"Premier document : {collection.find()[0]}")

    # # 2
    # print(f"Total d'étudiants : {collection.count_documents({})}")
    # # 3
    # print(f"Aurelia Menendez : {collection.find_one({"name": "Aurelia Menendez"})}")
    # # 4
    # print(f"Étudiant 50 : {collection.find_one({"_id": 50})}")
    # 5
    # students = list(collection.find({"name": ""}))

    # for student in students:
    #     print(student)

    # 6 
    # students = list(collection.find().limit(10))
    # for student in students:
    #     print(student)
    
    # 7
    # students = list(collection.find().limit(5).sort("name",1))
    # for student in students:
    #     print(student)

    # 8 
    # results = list(collection.aggregate([
    # {
    #     "$match": {
    #         "_id":0
    #     }
    # },
    # {
    #     "$project": {
    #         "scores": 1,
    #         "_id": 0
    #     }
    # }
    
    # ]))
    # print(results)

    # 9
    results = list(collection.aggregate([
    {
        "$unwind": "$scores"
    },
    {
        "$match": {
            "_id":1
        }
    },
    {
        "$project": {
            "moyenne": {"$avg" : "score"}
        }
    }
    
    ]))
    print(results)


    # print("=== LECTURE ===")
    # for user in collection.find():
    #     print(user)

    # print()

    # print("Utilisateurs de moins de 30 ans : ")
    # for user in collection.find({"age": {"$lt": 30}}):
    #     print(user["prenom"], user["nom"], "-", user["age"], "ans")

    # print()

    # print("=== MISE À JOUR ===")
 
    # result = collection.update_one(

    #     {"nom": "Dupont", "prenom": "Jean"},

    #     {"$set": {"age": 31}}

    # )

    # print("Documents modifiés:", result.modified_count)

    # print("Après mise à jour:")

    # print(collection.find_one({"nom": "Dupont"}))

    # print()


    # print("=== SUPPRESSION ===")

    # print()

    # result = collection.delete_many({"age": {"$gt": 35}})

    # print("Documents modifiés:", result.deleted_count)

    # print()
    # print("=== LECTURE ===")
    # for user in collection.find():
    #     print(user)

    # print()

    client.close()
