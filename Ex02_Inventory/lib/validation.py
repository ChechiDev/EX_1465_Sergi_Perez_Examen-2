import re

class Validation:
    """ Regex validation class """

    @staticmethod
    def val_string(value: str) -> bool:
        """ Only accepts words and spaces """

        pattern = r"^[a-zA-Z\s]+$"
        value = value.strip()

        return re.match(pattern, value)