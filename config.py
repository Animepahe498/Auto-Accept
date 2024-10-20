import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "20860620")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "25d2343b36fc5aea3604c6c50a8e2b59")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7941846162:AAERg_hUoaS7qA5o7LoqOfNc4PlmEnUvYoY")  # ⚠️ Required

    # database config
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://madara:madara@cluster0.tjfuu1g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required
    DB_NAME = os.environ.get("DB_NAME", "AutoAccept69")

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://envs.sh/pqi.jpg")
    ADMIN = int(os.environ.get('ADMIN', '6199677027'))  # ⚠️ Required
    DEFAULT_WELCOME_MSG = os.environ.get("WELCOME_MSG", "Hey {user},\nYour Request Approved ✅,\n\nWelcome to **{title}**\n\nCreated By - @Anime_Bloodline")
    DEFAULT_LEAVE_MSG = os.environ.get("LEAVE_MSG", "Bye Dude🥺 {user},\nSee You Again 👋\n\nFrom **{title}**")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002197851838"))  # ⚠️ Required

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8030"))


class TxT(object):

    HELP_MSG = """
<b> ADMIN Available commands:- </b>

➜ /set_welcome - To set custom welcome message (support photo & video & animation or gif or audio)
➜ /set_leave - To set custom leave message (support photo & video & animation or gif or audio)
➜ /option - To toggle your welcome & leave message also auto accept (whether it'll show to user or not and will auto accept or not)
➜ /auto_approves - To toggle your auto approve channel or group
➜ /status - To see status about bot
➜ /restart - To restart the bot
➜ /broadcast - To brodcast the users (only those user who has started your bot)
➜ /acceptall - To accept all the pending join requests
➜ /declineall - To decline all the pending join requests
➜ /add_userbot - To add user bot for to accept or reject pending join requests

⚠️ <b> Support HTML & Markdown formating in welcome or leave message for more info <a href=https://core.telegram.org/api/entities#:~:text=%2C%20MadelineProto.-,Allowed%20entities,-For%20example%20the> Link </a>. </b>


<b>⦿ Developer:</b> <a href=https://t.me/ShadowKakashi>ઝꪋઝꪋઽꫝꪱ</a>
"""

class temp(object):
    PENDING_REQUESTS = []
