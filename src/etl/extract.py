import re
from youtool import YouTube

def extract_video_id(input_str: str) -> str:
    """
    Extracts the video ID from a YouTube URL or returns the input if it's already an ID.
    """
    video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", input_str)
    if video_id_match:
        return video_id_match.group(1)
    elif len(input_str) == 11:
        return input_str

    raise Exception("Invalid YouTube URL or video ID.")

def fetch_comments(video_id: str, api_key: str) -> list:
    """
    Fetches comments for a given YouTube video ID using provided API keys.
    """
    yt = YouTube([api_key])
    comments_data = yt.video_comments(video_id)
    return comments_data
