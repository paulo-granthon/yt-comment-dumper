import os
import sys
import logging
from dotenv import load_dotenv
from extract import extract_video_id, fetch_comments
from transform import transform_comments
from load import insert_comments
from src.db import get_client

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "")

def main(input_str: str):
    if not YOUTUBE_API_KEY or YOUTUBE_API_KEY == ['']:
        logger.error("No YouTube API keys provided. Please set YOUTUBE_API_KEYS in the .env file.")
        return

    collection = get_client()
    if collection is None:
        return

    video_id = extract_video_id(input_str)
    if not video_id:
        return

    logger.info(f"Fetching comments for video ID: {video_id}")
    comments_data = fetch_comments(video_id, YOUTUBE_API_KEY)

    comment_documents = transform_comments(
        comments_data,
        video_id,
    )

    insert_comments(
        collection,
        comment_documents
    )

    logger.info("Finished fetching and storing comments.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python main.py <video_id_or_url>")
    else:
        main(sys.argv[1])
