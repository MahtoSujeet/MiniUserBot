from importlib import util
from glob import glob
import os
from pathlib import Path

from ..core.logger import logging

LOGS = logging.getLogger(__name__)


def load_module(shortname: str, plugin_path="", type=None):
    """Installs plugins.

    :param shrotname: Name of the plugin file without extension.
    :param plugin_path (optional): PathLike : directory path of the module file. default: root directory
    :param type (optional): "assistant" or default(plugins)
    """
    if shortname.startswith("__"):
        return

    # path is used for path reference eg. "package/module.py"
    path = (f"{plugin_path}/{shortname}.py") if plugin_path else (f"{shortname}.py")
    # name is used to module referece eg. "packeage.module"

    # Specifying module name, using match statement to that it would be easy to add more types of plugins
    match type:
        case "":
            name = f"userbot.plugins.{shortname}"
        case "assistant":
            name = f"userbot.assistant.{shortname}"
        case _:
            raise ImportError("Unknown plugin type: {type}")

    spec = util.spec_from_file_location(name=name, location=path)
    mod = util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    LOGS.info(f"{shortname} installed!")


def load_plugins_from_folder(folder, type=""):
    """Load all plugins of a folder."""
    modules = glob(f"userbot/{folder}/*.py")
    modules.sort()

    for module in modules:
        path = os.path.dirname(module)
        shortname = Path(module).stem

        try:
            load_module(shortname, path, type=type)

        except ImportError as e:
            LOGS.error(f"{shortname} install failed! {e}")
