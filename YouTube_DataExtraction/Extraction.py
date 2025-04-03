'''
import yt_dlp

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

ydl_opts = {"dumpjson": True}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(video_url, download=False)

# print(info)  # Full JSON data

title = info["title"]
publish_date = info["upload_date"]
duration = info["duration"]
print(f"Title: {title}, Published Date: {publish_date}, Duration: {duration} seconds")
'''

import yt_dlp
import json

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

ydl_opts = {"dumpjson": True}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(video_url, download=False)

# Save JSON to a file
json_filename = "video_metadata.json"
with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(info, json_file, indent=4, ensure_ascii=False)

print(f"Metadata saved to {json_filename}")

'''
video_data = {
    "title": info["title"],
    "upload_date": info["upload_date"],
    "duration": info["duration"],
    "uploader": info["uploader"],
    "views": info["view_count"]
}

json_filename = "filtered_video_metadata.json"
with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(video_data, json_file, indent=4, ensure_ascii=False)

print(f"Filtered metadata saved to {json_filename}")
'''