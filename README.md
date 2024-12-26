# MiniBot

[![Last commit](https://img.shields.io/github/last-commit/MahtoSujeet/miniuserbot?&logo=github)](https://github.com/MahtoSujeet/miniuserbot)
[![Size](https://img.shields.io/github/repo-size/MahtoSujeet/miniuserbot?color=green)](https://github.com/MahtoSujeet/miniuserbot)

## A Mininal yet Powerful Telegram Userbot.

This telegram userbot only has the minimal features that you need,
making it **the fasttest** userbot out there.

![Demo GIF](./assets/demo.gif)

Although it does come with many feature out of the box, one can still install plugins
to get more features.


### To contribute, follow below instruction.

* Clone the repo.
* Create virtual env and Install requirements using `python3 -m pip install -r --no-cache-dir requirements.txt`
* Make pull request on GitHub.

## Current file structure

```
├── config.py
├── downloads
├── minitgbot.session
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
├── sample_config.py
├── string_session.py
└── userbot
    ├── assistant
    │   ├── chat_assist.py
    │   └── chat_info.py
    ├── core
    │   ├── client.py
    │   ├── constants.py
    │   ├── __init__.py
    │   ├── logger.py
    │   ├── session.py
    │   └── tg_manager.py
    ├── __init__.py
    ├── __main__.py
    ├── plugins
    │   ├── alive.py
    │   ├── evaluators.py
    │   ├── greetings.py
    │   ├── images.py
    │   ├── __init__.py
    │   ├── install.py
    │   ├── ping.py
    │   ├── plus.py
    │   ├── psave.py
    │   ├── stripe_chk_handler.py
    │   └── stripe_chk.py
    └── utils
        ├── google_img_dl.py
        ├── __init__.py
        └── plugin_manager.py

7 directories, 32 files
```

# Command List 
### Chat Helper
* `id` - Get User/Chat id.
* `del` - Delete replied message.
* `purge` - Delete all messages till replied message.
* `psave` - Saves the replied message (Video) to a specified group.

* `alive` - Get bot's running status.
* `ping` - Check server's ping.
* `install` - Installs plugin by sending custom file.

* `eval` - To Execute python script/statements in a subprocess.
* `exec` - To Execute shell commands in a subprocess.

## Greeting commands
* `hbd` - Happy birthday.
* `thanks` - Thanks message.
* `hi` - HI message made with flower emoji.
* `gm` - Good Morning message.
* `gm2` - Good Morning message 2.
* `gm3` - Good Morning message 3.
* `gn` - Good Night message.
* `gn2` - Good Night message 2.
* `gn3` - Good Night message 3.
* `getwell` , `luck` , `cheer`, `sprinkle`



# Contact Me
Telegram: `@SujeetMahto`
Instagram: `sujeetvibes`
