import logging
import pathlib

import pkg_resources

from mopidy import config, ext

__version__ = pkg_resources.get_distribution("Mopidy-SaveStatePeriod").version

# TODO: If you need to log, use loggers named after the current Python module
logger = logging.getLogger(__name__)


class Extension(ext.Extension):

    dist_name = "Mopidy-SaveStatePeriod"
    ext_name = "savestateperiod"
    version = __version__

    def get_default_config(self):
        return config.read(pathlib.Path(__file__).parent / "ext.conf")

    def get_config_schema(self):
        schema = super().get_config_schema()
        schema["period"] = config.Integer(minimum=1)
        return schema

    def setup(self, registry):
        from .frontend import SaveStatePeriodFrontend
        registry.add("frontend", SaveStatePeriodFrontend)
