import get_video_info
import get_pic
import generate_pic

# https://www.youtube.com/watch?v=QdwHn-QiMwk&list=RDQdwHn-QiMwk&start_radio=1
# video_url = input("YouTubeの動画URLを入力してください: ")
video_url = "https://www.youtube.com/watch?v=QdwHn-QiMwk&list=PL2JAJdZbZxxBGn9Cr4L8O2M2u9a_qqtB4&index=59"
video_id = get_video_info.get_video_id(video_url)
video_info = get_video_info.get_video_info(video_id, get_video_info.API_KEY)

if "items" in video_info and len(video_info["items"]) > 0:
    title = video_info["items"][0]["snippet"]["title"]
    thumbnail_url = video_info["items"][0]["snippet"]["thumbnails"]["high"]["url"]
    channel_name = video_info["items"][0]["snippet"]["channelTitle"]
    get_pic.get_pic(thumbnail_url)
    generate_pic.generate_pic("downloaded_image.jpg", title, channel_name)
else:
    print("動画情報が見つかりませんでした")
# https://www.instagram.com/api/v1/web/create/configure_to_story/
