#!/usr/bin/env python3
from pypresence import Presence
import time
import sys
import subprocess

client_id = "963136145691140097"
RPC = Presence(client_id)
RPC.connect()
IMAGE = "https://img.youtube.com/vi/V2lXQ2iTr0A/0.jpg"
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
