<p align=center>
<br>
<a href="http://makeapullrequest.com"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg"></a>
<img src="https://img.shields.io/badge/os-linux-brightgreen">
<img src="https://img.shields.io/badge/os-mac-brightgreen">
<br>
<a href="https://discord.gg/aqu7GpqVmR"><img src="https://invidget.switchblade.xyz/aqu7GpqVmR"></a>
<br>
<a href="https://github.com/iamchokerman"><img src="https://img.shields.io/badge/maintainer-iamchokerman-blue"></a>

</p>

<h3 align="center">
A cli to browse and watch anime. This tool scrapes the site <a href="https://gogoplay4.com">gogoplay.</a>
</h3>
	
<h1 align="center">
	Showcase
</h1>

https://user-images.githubusercontent.com/44473782/160729779-41fe207c-b5aa-4fed-87db-313c83caf6bb.mp4

## Table of Contents

- [Fixing errors](#Fixing-errors)
- [Install](#Installation)
  - [Arch](#Arch)
  - [Linux](#Linux)
  - [Mac](#Mac)
  - [Windows](#Windows)
  - [Android](#Android)
- [Uninstall](#Uninstall)
- [Dependencies](#Dependencies)
- [Contribution Guidelines](./CONTRIBUTING.md)
- [Disclaimer](./disclaimer.md)

## Install

### Linux & Mac OS

Install dependencies [(See below)](#Dependencies)
(Make sure to uninstall ani-cli if you've had it before):
```sh
sudo rm /usr/local/bin/ani-cli
```

```sh
git clone https://github.com/iamchokerman/ani-cli/tree/pypresence && cd ani-cli
sudo cp ani-cli /usr/local/bin/ani-cli && cp coolkidzonly.py /usr/local/bin/coolkidzonly.py
pip install -r requirements.txt
```

*Note that mpv installed through flatpak is not compatible*

## Uninstall

remove from path lul

## Dependencies

- grep
- sed
- curl
- openssl
- mpv - Video Player
- aria2 - Download manager
- ffmpeg - m3u8 Downloader
