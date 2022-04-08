from ..utils.plugin_manager import PluginManager as pm
from ..core.logger import logging
import os

LOGS = logging.getLogger("PluginManager")

# file = filename, eg. alive.py
for file in os.listdir(os.path.dirname(__file__)):

    if os.path.isdir(file):
        continue

    # without extension (.py)
    module_name = os.path.splitext(file)[0]
    try:
        pm.install_plugin(module_name)
    except Exception as e:
        LOGS.error(f"{module_name} plugin failed to install with exception {e}")
