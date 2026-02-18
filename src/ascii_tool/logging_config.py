# logging_config.py

import logging
import os
from datetime import datetime
from rich.logging import RichHandler

LOG_DIR = "logs"

def setup_logging():
    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Clear handlers (prevents duplicates)
    if logger.hasHandlers():
        logger.handlers.clear()

    # ---------- Generate unique session filename ----------
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    logfile = os.path.join(LOG_DIR, f"session_{timestamp}.log")

    # ---------- Console handler (pretty) ----------
    console_handler = RichHandler(
        rich_tracebacks=True,
        markup=True
    )
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter("%(message)s"))

    # ---------- File handler (detailed) ----------
    file_handler = logging.FileHandler(
        logfile,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)

    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)-8s | "
        "%(filename)s:%(lineno)d | %(message)s"
    ))

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    # Optional: log where the file is
    logger.info(f"Logging to {logfile}")
