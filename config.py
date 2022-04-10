import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    API_ID = os.getenv("API_ID")

    API_HASH = os.getenv("API_HASH")

    SESSION_STRING = os.getenv("SESSION_STRING")

    LOG_GROUP_ID = os.getenv("LOG_GROUP_ID")

    COMMAND_HANDLER = os.getenv("COMMAND_HANDLER")
