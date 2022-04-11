from .core.session import miniub
from .core.logger import logging
from .utils import plugin_manager as pm

LOGS = logging.getLogger("MiniUserBot")

LOGS.info("Preparing to Install Plugins....")

# type is specified to let module loader know where to put this module
# TODO Remove this type shit.
pm.load_plugins_from_folder("assistant", type="assistant")
pm.load_plugins_from_folder("plugins")

miniub.start()
LOGS.info("Bot started successfully!")

miniub.run_until_disconnected()
