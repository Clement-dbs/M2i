from pymongo import MongoClient
from datetime import datetime



if __name__ == "__main__":

      
    print("=== Configuration ===")
    uri = "mongodb://admin:password@localhost:27017/?authSource=admin"
    client = MongoClient(uri)

    #db = client.get_database("sample_mflix")
    # selection de la db
    db = client["demo_crud"]

    # movies = database.get_collection("movies")
    # selection de la collection
    collection = db["utilisateurs"]

    collection.drop()

    print()

    print("=== Creation ===")
    collection.insert_many([
        {

            "nom": "Dupont",

            "prenom": "Jean",

            "age": 30,

            "ville": "Paris",

            "profession": "Développeur",

            "date_creation": datetime.now()

        },

        {

            "nom": "Martin",

            "prenom": "Marie",

            "age": 25,

            "ville": "Lyon",

            "profession": "Designer",

            "date_creation": datetime.now()

        },

        {

            "nom": "Dubois",

            "prenom": "Pierre",

            "age": 40,

            "ville": "Marseille",

            "profession": "Manager",

            "date_creation": datetime.now()

        }
    ])


    print()
    print("=== LECTURE ===")
    for user in collection.find():
        print(user)

    print()

    print("Utilisateurs de moins de 30 ans : ")
    for user in collection.find({"age": {"$lt": 30}}):
        print(user["prenom"], user["nom"], "-", user["age"], "ans")

    print()

    print("=== MISE À JOUR ===")
 
    result = collection.update_one(

        {"nom": "Dupont", "prenom": "Jean"},

        {"$set": {"age": 31}}

    )

    print("Documents modifiés:", result.modified_count)

    print("Après mise à jour:")

    print(collection.find_one({"nom": "Dupont"}))

    print()


    print("=== SUPPRESSION ===")

    print()

    result = collection.delete_many({"age": {"$gt": 35}})

    print("Documents supprimés:", result.deleted_count)

    print()
    print("=== LECTURE POST SUPPRESSION ===")
    for user in collection.find():
        print(user)

    print()

    client.close()
