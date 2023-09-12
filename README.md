
Install ani-cli from this fork:
```sh
sudo rm $(command -v ani-cli) &&
sudo curl -sL github.com/justchokingaround/jerry/raw/presence/ani-cli -o /usr/local/bin/ani-cli &&
sudo chmod +x /usr/local/bin/ani-cli
```

Install the presence script:
(You will also need the following python dependencies: `httpx`, `pypresence`)
```sh
sudo curl -sL github.com/justchokingaround/jerry/raw/presence/ani-cli -o /usr/local/bin/ani-cli-presence.py &&
sudo chmod +x /usr/local/bin/ani-cli-presence.py
```
