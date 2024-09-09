class CustomException:
    def __init__(self, message: str):
        self.message = message

    @property
    def message(self):
        return self.message
    
    @message.setter
    def message(self, value):
        try:
            if value.isinstance(str):
                self.message = value
            else:
                raise ValueError("Custom Exception message must be a string")
        except ValueError as ve:
            print(f"Error when trying to raise Custom Exception")
            return f"Error when trying to raise Custom Exception"
