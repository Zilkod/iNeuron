import logging

# Configure logging to write to the file "app.log"
logging.basicConfig(filename='app.log', level=logging.INFO, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

# Log the message "Hello, World!" at the INFO level
logging.info("Hello, World!")
