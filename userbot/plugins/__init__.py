from ..utils.plugin_manager import PluginManager as pm
from ..core.logger import logging
import os

LOGS = logging.getLogger(__name__)

def install_plugins():
    """Installs all plugins in userbot/plugins/"""

    # file = filename, eg. alive.py and not path
    for file in os.listdir(os.path.dirname(__file__)):

        if os.path.isdir(file):
            continue

        module_name = os.path.splitext(file)[0]
        try:
            pm.install_plugin(module_name)
        except Exception as e:
            LOGS.error(f"{module_name} install failed: {e}")
