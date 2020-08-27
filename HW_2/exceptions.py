class NegativeValError(ValueError):

    def __init__(self, value, *args):
        self.value = value
    def __str__(self):
        return f"The value can't be below 0. You entered {self.value}"

class TypeValError(TypeError):

    def __init__(self, value, *args):
        self.value = value
    def __str__(self):
        return f"A type of numeric values must be integer or float. You entered {self.value}"