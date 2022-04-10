from .core.session import miniub
from .core.logger import logging
from .utils import plugin_manager as pm

LOGS = logging.getLogger("MiniUserBot")

LOGS.info("Preparing to Install Plugins....")
pm.load_plugins_from_folder("plugins")

miniub.start()
LOGS.info("Bot started successfully!")

miniub.run_until_disconnected()
