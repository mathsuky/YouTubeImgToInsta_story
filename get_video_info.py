import requests
import re
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('YOUTUBE_API_KEY')  # ここにあなたのAPIキーを入力してください


def get_video_id(url):
    video_id_match = re.search(r'v=([a-zA-Z0-9_-]+)', url)
    if video_id_match:
        return video_id_match.group(1)
    else:
        raise ValueError('Invalid YouTube URL')


def get_video_info(video_id, api_key):
    url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


def print_video_info(video_info):
    if 'items' in video_info and len(video_info['items']) > 0:
        snippet = video_info['items'][0]['snippet']
        print(f"タイトル: {snippet['title']}")
        print(f"サムネイルURL: {snippet['thumbnails']['high']['url']}")
    else:
        print("動画情報が見つかりませんでした")


if __name__ == "__main__":
    video_url = input("YouTubeの動画URLを入力してください: ")
    try:
        video_id = get_video_id(video_url)
        video_info = get_video_info(video_id, API_KEY)
        # print(video_info)
        print_video_info(video_info)
    except Exception as e:
        print(f"エラーが発生しました: {e}")
