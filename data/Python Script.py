from googleapiclient.discovery import build
import pandas as pd
from isodate import parse_duration

API_KEY = "xyz_321"
CHANNEL_ID = "UCODHrzPMGbNv67e84WDZhQQ"

youtube = build("youtube", "v3", developerKey=API_KEY)


# ---------- 1. CHANNEL INFO ----------
def get_channel_info():
    res = youtube.channels().list(
        part="snippet,statistics,contentDetails",
        id=CHANNEL_ID
    ).execute()["items"][0]

    return {
        "Channel ID": res["id"],
        "Channel Title": res["snippet"]["title"],
        "Description": res["snippet"]["description"],
        "Published At": res["snippet"]["publishedAt"],
        "Subscriber Count": res["statistics"].get("subscriberCount"),
        "View Count": res["statistics"].get("viewCount"),
        "Video Count": res["statistics"].get("videoCount"),
        "Uploads Playlist": res["contentDetails"]["relatedPlaylists"]["uploads"]
    }


# ---------- 2. GET ALL VIDEO IDS ----------
def get_video_ids(playlist_id):
    video_ids = []
    token = None

    while True:
        res = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=token
        ).execute()

        video_ids += [
            item["contentDetails"]["videoId"]
            for item in res["items"]
        ]

        token = res.get("nextPageToken")
        if not token:
            break

    return video_ids


# ---------- 3. GET VIDEO DETAILS ----------
def get_video_data(video_ids):
    data = []

    for i in range(0, len(video_ids), 50):
        res = youtube.videos().list(
            part="snippet,contentDetails,statistics,status",
            id=",".join(video_ids[i:i+50])
        ).execute()

        for v in res["items"]:
            data.append({
                "Video ID": v["id"],
                "Title": v["snippet"]["title"],
                "Published At": v["snippet"]["publishedAt"],
                "Duration": str(parse_duration(v["contentDetails"]["duration"])),
                "Views": v["statistics"].get("viewCount"),
                "Likes": v["statistics"].get("likeCount"),
                "Comments": v["statistics"].get("commentCount"),
                "Privacy": v["status"]["privacyStatus"]
            })

    return data


# ---------- 4. SAVE ----------
def save_to_excel(channel_data, video_data):
    with pd.ExcelWriter("data.xlsx", engine="openpyxl") as writer:
        pd.DataFrame([channel_data]).to_excel(writer, sheet_name="Channel", index=False)
        pd.DataFrame(video_data).to_excel(writer, sheet_name="Videos", index=False)


# ---------- MAIN FLOW ----------
channel_data = get_channel_info()
video_ids = get_video_ids(channel_data["Uploads Playlist"])
video_data = get_video_data(video_ids)

import os

print("\nData saved successfully")
print("Saved at:", os.path.abspath("youtube_data.xlsx"))

print("Done, Data saved successfully.")