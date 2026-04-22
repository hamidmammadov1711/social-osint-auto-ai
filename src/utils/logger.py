import logging
import sys
import io
from rich.logging import RichHandler
from rich.console import Console

# Force UTF-8 encoding for Windows console
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

console = Console(force_terminal=True)

def setup_logger(name="OSINT-AUTO"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Rich handler for beautiful console output
    rich_handler = RichHandler(rich_tracebacks=True, console=console)
    logger.addHandler(rich_handler)
    
    return logger

logger = setup_logger()
