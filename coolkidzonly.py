#!/usr/bin/env python3
import subprocess
import sys
import time

import httpx
from pypresence import Presence

CLIENT_ID = "963136145691140097"
ENDPONT = "https://kitsu.io/api/"

rpc_client = Presence(CLIENT_ID)
rpc_client.connect()

http_client = httpx.Client(base_url=ENDPONT)


(
    _,
    anime_name,
    episode_count,
    content_stream,
    content_referer,
    mpv_executable,
    *_,
) = sys.argv


anime = http_client.get("edge/anime", params={"filter[text]": anime_name}).json()[
    "data"
]

if not anime:
    raise SystemExit()

media = anime[0]["attributes"]
media_title = "%s %s" % (media["canonicalTitle"], "Episode "+episode_count)

process = subprocess.Popen(
    args=[
        mpv_executable,
        content_stream,
        f"--referrer={content_referer}",
        f"--force-media-title={media_title}",
    ]
)

rpc_client.update(
    details="Watching anime",
    state=media_title,
    large_image=media["posterImage"]["original"],
    start=int(time.time()),
)

process.wait()
