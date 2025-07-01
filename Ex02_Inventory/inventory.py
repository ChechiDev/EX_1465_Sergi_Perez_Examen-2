import os
from lib.dict_builder import DictBuilder


class InventoryManagement:
    def __init__(self, prod):
        self.inventory = {}
        self.dict_builder = DictBuilder()

        # Attr:
        self._prod = prod


    def add_product(self, prod: str) -> dict:
        """
        Add a new product using DictBuilder class
        """
        self.dict_builder._prod = prod
        inventory = self.dict_builder.to_dict()

        # Verificamos si existe el prod, si existe lo incrementamos, sinó lo creamos:
        check_prod = self.inventory.get(prod)

        if check_prod is not None and check_prod > 0:
            self.inventory[prod] = check_prod + 1

        else:
            self.inventory[prod] = 1

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
        pass

if __name__ == "__main__":
    os.system("cls")
    tienda = InventoryManagement("inicial")


    print("Añado producto nuevo:")
    print(tienda.add_product("Manzanas"))
    print(tienda.add_product("Peras"))
    print(tienda.inventor)