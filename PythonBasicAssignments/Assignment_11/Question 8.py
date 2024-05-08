import logging

# Create a logger with a custom name
logger = logging.getLogger('my_application')

# Set the logger's level
logger.setLevel(logging.DEBUG)

# Create a file handler and set its level
file_handler = logging.FileHandler('my_application.log')
file_handler.setLevel(logging.DEBUG)

# Create a console handler and set its level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter for the log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set the formatter for the handlers
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Example usage in a module or class
class MyClass:
    def __init__(self):
        # Log a message at the INFO level
        logger.info('Initializing MyClass')

    def do_something(self):
        # Log a message at the DEBUG level
        logger.debug('Doing something')

# Example usage in another module
def main():
    # Log a message at the INFO level
    logger.info('Starting application')

    # Create an instance of MyClass
    obj = MyClass()

    # Call a method of MyClass
    obj.do_something()

if __name__ == '__main__':
    main()
