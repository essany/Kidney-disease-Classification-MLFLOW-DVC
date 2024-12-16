from src.cnnClassifier.utils.common import example_function
from src.cnnClassifier import logger

# Log a test message from the main script
logger.info("Testing logger from main script.")

# Call the example function to log a message from common.py
example_function()
