

class DictBuilder:
    def __init__(self):
        self._prod = None
        self._qty = None

    # Genera un diccionario
    def to_dict(self) -> dict:
        """
        Convertimos a diccionario (inventario)
        """

        inventory = {
            "prod_name": self._prod,
            "quantity": self._qty
        }

        return inventory
