import logging
import traceback
import datetime

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('errors.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logging.getLogger().addHandler(file_handler)

try:
    raise ValueError("Example error occurred")
except Exception as e:
    logging.error(f"Exception: {type(e).__name__} - {e} - Timestamp: {datetime.datetime.now()}")
    traceback.print_exc()
