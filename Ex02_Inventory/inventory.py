from lib.dict_builder import DictBuilder
from lib.validation import Validation
from lib import utils


class Product:
    """ Class that represents a product """
    def __init__(self, name: str, qty: int = 0):
        # Instancias:
        self.validation = Validation()

        # Attr:
        self._name = self._valid_name(name)
        self._qty = self._valid_quantity(qty)


    def _valid_name(self, name: str) -> str:
        # Normalizamos los espacios para un formato correcto:
        name = Validation.normalize_str_space(name)

        # validación: Nombre sin carácteres raros, ni números:
        if not Validation.val_string(name):
            raise ValueError(
                f"Error: Name -> '{name}' must contain only alphabetic characters without accents..."
            )

        return name

    def _valid_quantity(self, qty: int) -> int:
        if type(qty) != int or qty < 0:

            raise ValueError(
                f"Error: The quantity '{qty}' must be a positive integer"
            )

        return qty


    @property
    def name(self) -> str:
        return self._name

    @property
    def quantity(self):
        return self._qty

    @name.setter
    def name(self, name: str):
        self._name = self._valid_name(name)

    @quantity.setter
    def quantity(self, qty: int):
        self._qty = self._valid_quantity(qty)


class InventoryManagement:
    def __init__(self, prod, qty):
        self.inventory = {}
        self.ut = utils.Utils()
        self.dict_builder = DictBuilder()


    def add_product(self, prod: str, qty: int) -> dict:
        """
        Add a new product using DictBuilder class
        """
        try:
            product = Product(prod)

        except ValueError as e:
            print(f"Error: {e}")
            return self.inventory


    def delete_product(self, prod: str) -> None:
        pass

    def consult_product(self, prod: str) -> dict:
        pass

    def mod_quantity(self, prod: str, new_qty: int) -> int:
        pass

    def find_product(self, txt: str) -> str:
        pass

    def view_inventory(self, sort = False):

        print("Current inventory: \n")
        if self.inventory:
            if sort:
                keys = list(self.inventory.keys())
                keys.sort()

                for prod in keys:
                    print(f"{prod}: {self.inventory[prod]}")

            else:
                for prod, qty in self.inventory.items():
                    print(f"{prod}: {qty}")

        else:
            print("Inventory is empty...")


if __name__ == "__main__":
    p1 = Product("MAnzanas", 10)
    print(p1)