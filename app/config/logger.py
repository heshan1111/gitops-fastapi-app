"""
Application Logger Configuration

This file creates a centralized logger for the application.

Instead of using print(), every module will use this logger.
"""

import logging

# Create a logger instance for the application
logger = logging.getLogger("gitops-api")

# Set the minimum log level
# INFO means INFO, WARNING, ERROR and CRITICAL logs will be shown.
logger.setLevel(logging.INFO)

# Create a console output handler
console_handler = logging.StreamHandler()

# Define the log message format
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

# Apply the formatter to the console handler
console_handler.setFormatter(formatter)

# Avoid adding duplicate handlers when reloading
if not logger.handlers:
    logger.addHandler(console_handler)