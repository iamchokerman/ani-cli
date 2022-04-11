#!/bin/sh
echo "hello world"
VAR="idk"

main () {
python3 - << EOF
from pypresence import Presence # The simple rich presence client in pypresence
import time

client_id = "960166822315962379"  # Put your Client ID in here
RPC = Presence(client_id)  # Initialize the Presence client
RPC.connect() # Start the handshake loop
IMAGE="https://media1.giphy.com/media/VTtANKl0beDFQRLDTh/giphy.gif?cid=ecf05e47sl1ebnscj2p0t3as26q7lmwpr98n7nxwxlly3oda&rid=giphy.gif&ct=g"
# ACTIVITY=''

while True:  # The presence will stay on as long as the program is running
    RPC.update(
        details="Learning...",
        # state=ACTIVITY,
        large_image=IMAGE,
        start=int(time.time()),
    )
    time.sleep(60) #Wait a wee bit
EOF
}
main

echo "bye world"
