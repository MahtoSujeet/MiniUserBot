import os
from importlib import util

from ..core.logger import logging

LOGS = logging.getLogger(__name__)


class PluginManager:

    @staticmethod
    def install_plugin(shortname: str, plugin_path="userbot/plugins"):
        """Installs plugins.

        :param shrotname: Name of the plugin file without extension.
        """

        if shortname.startswith("__"):
            return
        path = os.path.join(plugin_path, (shortname + ".py"))
        name = path.replace("/", ".")

        spec = util.spec_from_file_location(name=name, location=path)
        spec.loader.load_module(name)

        LOGS.info(f"{shortname} installed!")
