from .core import minibot
from .core.logger import logging
from . import plugins

LOGS = logging.getLogger("MiniBot")

minibot.start()
LOGS.info("Bot started successfully!")
minibot.run_until_disconnected()
