from ..core import minibot
from importlib import util
import os
from ..core.logger import logging

LOGS = logging.getLogger("PluginManager")


class PluginManager:

    @staticmethod
    def install_plugin(shortname: str, plugin_path="userbot/plugins"):
        """Installs plugins.

        :param shrotname: Name of the plugin file without extension.
        """

        if shortname.startswith("__"):
            return

        path = os.path.join(plugin_path, (shortname + ".py"))
        name = path.replace("/", ".")[1:]

        spec = util.spec_from_file_location(name=name, location=path)
        spec.loader.load_module(name)

        LOGS.info(f"{shortname} has installed successfully!")
