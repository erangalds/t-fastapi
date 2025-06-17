from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def connect_to_mongodb():
    # MongoDB connection URI.
    # By default, our docker-compose setup does not enable auth on MongoDB.
    mongo_uri = "mongodb://localhost:27017/"

    # If you uncommented and set MONGO_INITDB_ROOT_USERNAME and MONGO_INITDB_ROOT_PASSWORD
    # in docker-compose.yml (e.g., myuser/mypassword), your URI would be:
    # mongo_uri = "mongodb://myuser:mypassword@localhost:27017/"

    try:
        # Create a new client and connect to the server
        client = MongoClient(mongo_uri)

        # Send a ping to confirm a successful connection
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")

        # Example: List databases
        print("Databases:", client.list_database_names())

        # Example: Access a database (it will be created if it doesn't exist)
        db = client['mydemodb'] # or client.mydemodb
        collection = db['mycollection'] # or db.mycollection

        # Example: Insert a document
        doc_to_insert = {"name": "Gemini User", "project": "Docker Mongo Test"}
        insert_result = collection.insert_one(doc_to_insert)
        print(f"Inserted document with id: {insert_result.inserted_id}")

        # Example: Find the document
        found_doc = collection.find_one({"_id": insert_result.inserted_id})
        print(f"Found document: {found_doc}")

    except ConnectionFailure:
        print("Failed to connect to MongoDB. Check if the MongoDB container is running and accessible.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'client' in locals() and client:
            client.close()
            print("MongoDB connection closed.")

if __name__ == "__main__":
    connect_to_mongodb()