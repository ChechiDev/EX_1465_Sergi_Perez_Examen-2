import re

class Validation:
    """ Regex validation class """

    @staticmethod
    def normalize_str_space(value: str) -> str:
        """ Normalizes str spacing by removing extra spaces"""

        value = value.strip()
        return re.sub(r"\s+", " ", value) # Con sub igualamos a replace


    @staticmethod
    def val_string(value: str) -> bool:
        """ Only accepts words and spaces """

        pattern = r"^[a-zA-Z\s]+$"
        value = value.strip()

        return re.match(pattern, value) is not None