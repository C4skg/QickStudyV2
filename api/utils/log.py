import logging
import colorlog

class LOG_LEVEL:
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

ch = logging.StreamHandler()

formatter = colorlog.ColoredFormatter(
    "\r%(white)s[%(green)s%(asctime)s%(white)s][%(log_color)s%(levelname)-8s%(reset)s%(white)s] %(blue)s%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    reset=True,
    log_colors={
        'DEBUG':    'cyan',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'bold_red',
    },
    secondary_log_colors={},
    style='%'
)

ch.setFormatter(formatter)

LOGGER.addHandler(ch)