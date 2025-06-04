import os
import urllib.parse
from pymongo import MongoClient
from dotenv import load_dotenv

def get_client():
    """
    Establishes a connection to the MongoDB collection.
    """

    load_dotenv()

    db_host = os.getenv("DB_HOST", "localhost")
    db_port = int(os.getenv("DB_PORT", "27017"))
    db_name = os.getenv("DB_NAME", "yt_comment_dumper")
    db_collection = os.getenv("DB_COLLECTION", "comments")
    db_username = os.getenv("DB_USERNAME", "mongo")
    db_password = os.getenv("DB_PASSWORD", "secret")

    try:
        username = urllib.parse.quote_plus(db_username)
        password = urllib.parse.quote_plus(db_password)
        mongo_uri = f"mongodb://{username}:{password}@{db_host}:{db_port}/{db_name}?authSource=admin"
        client = MongoClient(mongo_uri)
        db = client[db_name]
        db.command("ping")
        collection = db[db_collection]
        return collection
    except Exception as e:
        raise Exception(f"Failed to connect to MongoDB") from e
