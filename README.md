![image](https://github.com/justchokingaround/ani-cli/assets/44473782/2c761436-d5e1-4392-853b-e6eec7ea9d5a)


Install ani-cli from this fork:
```sh
sudo rm -f /usr/local/bin/ani-cli &&
sudo curl -sL github.com/justchokingaround/ani-cli/raw/presence/ani-cli -o /usr/local/bin/ani-cli &&
sudo chmod +x /usr/local/bin/ani-cli
```

Install the presence script:
(You will also need the following python dependencies: `httpx`, `pypresence`)
```sh
sudo curl -sL github.com/justchokingaround/ani-cli/raw/presence/ani-cli-presence.py -o /usr/local/bin/ani-cli-presence.py &&
sudo chmod +x /usr/local/bin/ani-cli-presence.py
```
