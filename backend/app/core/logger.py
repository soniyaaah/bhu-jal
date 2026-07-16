import sys
from loguru import logger

# Remove default handler
logger.remove()

# Add console handler with custom formatting
logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO",
)

# Add file handler for persistent logs (optional, commented out for now since phase 3 doesn't require complex persistence)
# logger.add("logs/app.log", rotation="10 MB", level="DEBUG")

# Export logger
__all__ = ["logger"]
