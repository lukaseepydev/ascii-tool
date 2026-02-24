# logging_config.py

import logging
import os
from rich.logging import RichHandler


def setup_logging():

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Clear handlers (prevents duplicates)
    if logger.hasHandlers():
        logger.handlers.clear()

    # ---------- Generate unique session filename ----------

    # ---------- Console handler (pretty) ----------
    console_handler = RichHandler(
        rich_tracebacks=True,
        markup=True
    )
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter("%(message)s"))

    # ---------- File handler (detailed) ----------

    logger.addHandler(console_handler)

    logger.propagate = False

    # Optional: log where the file is
