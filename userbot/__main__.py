from .core.session import miniub
from .core.logger import logging
from .plugins import install_plugins

LOGS = logging.getLogger("MiniUserBot")

LOGS.info("Preparing to Install Plugins....")
install_plugins()

miniub.start()
LOGS.info("Bot started successfully!")

miniub.run_until_disconnected()
