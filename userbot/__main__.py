from .core import client
from .core.logger import logging
from . import plugins


LOGS = logging.getLogger("MiniBot")

client.run_until_disconnected()
