#!/usr/bin/env python3
from pypresence import Presence # The simple rich presence client in pypresence
import time
import sys

client_id = "963136145691140097"  # Put your Client ID in here
RPC = Presence(client_id)  # Initialize the Presence client
RPC.connect() # Start the handshake loop
IMAGE="https://e7.pngegg.com/pngimages/994/418/png-clipart-lain-iwakura-anime-television-show-manga-anime-face-black-hair.png"
ACTIVITY=sys.argv[1]+" "+sys.argv[2]

while True:  # The presence will stay on as long as the program is running
    RPC.update(
        details="Watching anime",
        state=ACTIVITY,
        large_image=IMAGE,
        start=int(time.time()),
    )
    time.sleep(60) #Wait a wee bit
