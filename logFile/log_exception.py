import logging

logging.basicConfig(filename="error sample.log", level=logging.INFO)
log = logging.getLogger("ex")

try:
    raise RuntimeError
except Exception:
    log.exception("Error!")
