# Ultralytics YOLO 🚀, AGPL-3.0 license

__version__ = "8.1.34"

from ultralytics_bower.data.explorer.explorer import Explorer
from ultralytics_bower.models import RTDETR, SAM, YOLO, YOLOWorld
from ultralytics_bower.models.fastsam import FastSAM
from ultralytics_bower.models.nas import NAS
from ultralytics_bower.utils import ASSETS, SETTINGS as settings
from ultralytics_bower.utils.checks import check_yolo as checks
from ultralytics_bower.utils.downloads import download

__all__ = (
    "__version__",
    "ASSETS",
    "YOLO",
    "YOLOWorld",
    "NAS",
    "SAM",
    "FastSAM",
    "RTDETR",
    "checks",
    "download",
    "settings",
    "Explorer",
)
