class CustomError(Exception):
    """Custom exception class"""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

try:
    raise CustomError("This is a custom error message.")
except CustomError as e:
    print("Custom error occurred:", e.message)
