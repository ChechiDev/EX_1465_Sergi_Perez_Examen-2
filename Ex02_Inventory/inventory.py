from lib.dict_builder import DictBuilder
from lib import utils


class InventoryManagement:
    def __init__(self, prod, qty):
        self.inventory = {}
        self.ut = utils.Utils()
        self.dict_builder = DictBuilder()

        # Attr:
        self._prod = prod
        self._qty = qty


    def add_product(self, prod: str, qty: int) -> dict:
        """
        Add a new product using DictBuilder class
        """
        self.dict_builder._prod = prod
        inventory = self.dict_builder.to_dict()

        # Verificamos si existe el prod, si existe lo incrementamos, sinó lo creamos:
        check_prod = self.inventory.get(prod)

        # Si existe suma la nueva qty:
        if check_prod is not None and check_prod > 0:
            self.inventory[prod] = check_prod + qty

        # Si no existe lo crea con la qty especificada por user:
        else:
            self.inventory[prod] = qty

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
                for prod, qty in self.inventory.inventory.items():
                    print(f"{prod}: {qty}")

        else:
            print("Inventory is empty...")


if __name__ == "__main__":
    tienda = InventoryManagement("inicial", 0)


    print("Añado producto nuevo:")
    print(tienda.add_product("Manzanas", 10))
    print(tienda.add_product("Peras", 8))
    print(tienda.inventory)