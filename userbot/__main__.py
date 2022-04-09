import asyncio

from .core.session import miniub
from .core.logger import logging
from . import plugins

LOGS = logging.getLogger("MiniUserBot")

miniub.start()

LOGS.info("Bot started successfully!")
print(miniub.list_event_handlers())
miniub.run_until_disconnected()
