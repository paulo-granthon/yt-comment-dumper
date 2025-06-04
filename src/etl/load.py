def insert_comment(collection, comment_doc):
    """
    Inserts or updates a comment document in the MongoDB collection.
    """
    try:
        collection.update_one(
            {"comment_id": comment_doc["comment_id"]},
            {"$set": comment_doc},
            upsert=True
        )
    except Exception as e:
        raise Exception(f"Failed to insert comment {comment_doc['comment_id']}") from e


def insert_comments(collection, comment_docs):
    """
    Inserts or updates a list of comment documents in the MongoDB collection.
    """
    for doc in comment_docs:
        insert_comment(collection, doc)
