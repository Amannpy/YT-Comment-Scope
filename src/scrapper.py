import os
import re
import csv
from googleapiclient.discovery import build
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs
import time
from tqdm import tqdm  # For progress bars
from pathlib import Path  # For better path handling

def get_video_id(url):
    """
    Extracts the video ID from a YouTube URL using urllib.parse.
    Supports various YouTube URL formats.
    """
    parsed_url = urlparse(url)
    
    # Handle different YouTube URL formats
    if parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
        if parsed_url.path == '/watch':
            query = parse_qs(parsed_url.query)
            return query.get('v', [None])[0]
        elif parsed_url.path.startswith('/embed/'):
            return parsed_url.path.split('/')[2]
        elif parsed_url.path.startswith('/v/'):
            return parsed_url.path.split('/')[2]
    elif parsed_url.hostname == 'youtu.be':
        return parsed_url.path.lstrip('/')
    
    print("Invalid YouTube URL.")
    return None

def get_comments(api_key, video_id, max_comments=1000):
    """
    Retrieves comments from a YouTube video using the YouTube Data API.
    Fetches up to 'max_comments' comments.
    """
    youtube = build('youtube', 'v3', developerKey=api_key)

    comments = []
    try:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,  # Maximum allowed per request
            textFormat="plainText",
            order="relevance"  # You can change to "time" if desired
        )
        response = request.execute()

        pbar = tqdm(total=max_comments, desc="Fetching comments", unit="comment")

        while response and len(comments) < max_comments:
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append(comment)
                pbar.update(1)
                if len(comments) >= max_comments:
                    break  # Exit if we've reached the desired number of comments

            if 'nextPageToken' in response and len(comments) < max_comments:
                request = youtube.commentThreads().list(
                    part="snippet",
                    videoId=video_id,
                    pageToken=response['nextPageToken'],
                    maxResults=100,
                    textFormat="plainText",
                    order="relevance"
                )
                response = request.execute()
                time.sleep(1)  # Optional: Delay to respect API rate limits
            else:
                break  # No more pages to fetch

        pbar.close()

    except Exception as e:
        print(f"An error occurred while fetching comments: {e}")

    return comments

def save_comments_to_csv(comments, directory, filename='comments.csv'):
    """
    Saves the list of comments to a CSV file with serial numbers.
    
    Parameters:
    - comments (list): List of comment strings.
    - directory (Path): Directory where the CSV file will be saved.
    - filename (str): Name of the CSV file to save comments.
    """
    try:
        # Ensure the directory exists
        directory.mkdir(parents=True, exist_ok=True)
        print(f"Directory '{directory}' is ready.")

        csv_path = directory / filename

        with csv_path.open('w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Serial Number', 'Comment'])  # Write header
            for idx, comment in enumerate(comments, start=1):
                writer.writerow([idx, comment])
        print(f"Comments have been saved to {csv_path.resolve()}")
    except Exception as e:
        print(f"Failed to save comments to CSV: {e}")

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Retrieve the API key from the environment variable
    api_key = os.getenv('YOUTUBE_API_KEY')
    
    if not api_key:
        print("Error: The environment variable 'YOUTUBE_API_KEY' is not set.")
        return
    else:
        print("API Key loaded successfully.")

    video_url = input("Enter the YouTube video URL: ").strip()
    video_id = get_video_id(video_url)

    if video_id:
        print("Fetching comments...")
        comments = get_comments(api_key, video_id, max_comments=1000)
        print(f"Total comments fetched: {len(comments)}")
        if comments:
            # Define the base directory using pathlib
            base_dir = Path('D:/YouTube Analysis')
            data_dir = base_dir / 'data'
            
            # Optionally, get and print the current working directory
            cwd = Path.cwd()
            print(f"Current Working Directory: {cwd.resolve()}")
            
            # Save comments to CSV inside the data directory
            save_comments_to_csv(comments, directory=data_dir, filename='comments.csv')
        else:
            print("No comments were fetched.")
    else:
        print("Failed to extract video ID from the provided URL.")

if __name__ == "__main__":
    main()
