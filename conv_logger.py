import logging
from datetime import datetime

# Set up the logger
logging.basicConfig(filename="conversation_log.txt", 
                    level=logging.INFO, 
                    format="%(asctime)s - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")

def log_conversation(speaker, message):
    """
    Logs the conversation with date, time, speaker, and message.

    Parameters:
    - speaker (str): Who said it (e.g., 'User', 'Robot')
    - message (str): What they said
    """
    log_message = f"{speaker}: {message}"
    logging.info(log_message)
