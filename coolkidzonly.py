#!/usr/bin/env python3
from pypresence import Presence
import time
import sys
import subprocess
import httpx

client_id = "963136145691140097"
RPC = Presence(client_id)
RPC.connect()
content_title, *gibberish = sys.argv[1].rsplit(" ", 1)
print(content_title)
IMAGE = httpx.get(f"https://kitsu.io/api/edge/anime?filter[text]={content_title}").json()["data"][0]["attributes"]["posterImage"]["medium"]
ACTIVITY = sys.argv[1]+" "+sys.argv[2]
executable = sys.argv[5]
process = subprocess.Popen(args=[executable, sys.argv[3],
                                 "--referrer=" + sys.argv[4],
                                 "--force-media-title=" +
                                 sys.argv[1] + " " + sys.argv[2]])
RPC.update(
        details="Watching anime",
        state=ACTIVITY,
        large_image=IMAGE,
        start=int(time.time()),
)
process.wait()
