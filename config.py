import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    API_ID = os.getenv("API_ID")

    API_HASH = os.getenv("API_HASH")

    SESSION_STRING = os.getenv("SESSION_STRING")

    LOG_GROUP_ID = os.getenv("LOG_GROUP_ID")

    COMMAND_HANDLER = os.getenv("COMMAND_HANDLER")

    ALIVE_NAME = os.getenv("ALIVE_NAME")

    USERID = os.getenv("USERID")

    BOT_TOKEN = os.getenv("BOT_TOKEN")

    # Optional
    SAVE_GROUP_ID = os.getenv("SAVE_GROUP_ID")
