def transform_comment(comment, video_id):
    """
    Transforms a single comment or reply into a MongoDB document.
    """

    import logging
    logger = logging.getLogger(__name__)
    logger.info(f"the morderforker comment is: {comment}")

    return {
        "comment_id": comment.get("id"),
        "video_id": video_id,
        "text": comment.get("text"),
        "author": {
            "name": comment.get("author"),
            "channel_url": f"https://youtube.com/{comment.get("author")}",
            "profile_image_url": comment.get("author_profile_image_url"),
        },
        "published_at": comment.get("published_at"),
        "likes": comment.get("likes"),
        "is_hearted": comment.get("is_hearted"),
        "parent_id": comment.get("parent_id"),
    }

def transform_comments(comments_data, video_id):
    """
    Transforms a list of comments into MongoDB documents.
    """
    documents = []
    for comment in comments_data:
        main_doc = transform_comment(comment, video_id)
        documents.append(main_doc)
    return documents
