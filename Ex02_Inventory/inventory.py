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
        return self._name.strip().title()

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
    def __init__(self):
        self.inventory = {}
        self.ut = utils.Utils()
        self.dict_builder = DictBuilder()


    def add_product(self, prod: str, qty: int) -> dict:
        """ Add a new product using DictBuilder class """
        try:
            product = Product(prod, qty)

            # Verificamos si el producto existe:
            if product.name in self.inventory:
                # Si existe incrementamos cantidad:
                self.inventory[product.name] += product.quantity

            else:
                # Sinó creamos el dict
                self.dict_builder._prod = product.name
                self.dict_builder._qty = product.quantity

                new_entry = self.dict_builder.to_dict()

                # Agregar al inventario principal
                self.inventory[product.name] = new_entry["quantity"]

        except ValueError as e:
            print(f"Error: {e}")

        return self.inventory


    def delete_product(self, prod: str) -> bool:
        """ Delete a product from inventory """

        try:
           # Usamos la clase Product para validar:
           product = Product(prod, 0)
           product_name = product.name

           # Checkeamos:
           if product_name in self.inventory:
               # Si está borramos:
               self.inventory.pop(product_name)
               return True

           # Si no está:
           else:
               return False

        except ValueError as e:
            print(f"Error: {e}")
            return False


    def consult_product(self, prod: str) -> dict:
        """
        Consult a product in inventory
        Returns:
            Quantity using .get() if exists
        """
        try:
            # Usamos la clase Product para validar:
            product = Product(prod, 0)
            product_name = product.name

            # Buscamos la cantidad del producto:
            quantity = self.inventory.get(product_name)

            # Si existe devolvemos cantidaD:
            if quantity is not None:
                return {
                    "product": product_name,
                    "quantity": quantity
                }

            else:
                return None

        except ValueError as e:
            print(f"Error: {e}")
            return False


    def mod_quantity(self, prod: str, new_qty: int) -> bool:
        """ Modify the quantity of an existing product in the inventory """
        try:
            # Usamos la clase Product para validar:
            product = Product(prod, new_qty)
            product_name = product.name

            new_qty = product.quantity

            # existe?
            if product_name in self.inventory:
                self.inventory[product_name] = new_qty
                return True

            else:
                # No existe:
                print(f"Product '{product_name}' not found in inventory.")
                return False


        except ValueError as e:
            print(f"Error: {e}")
            return False



    def find_product(self, txt: str) -> str:
        pass



    def view_inventory(self, sort = False, show_qty=True) -> None:
        """ Display the current inventory with optional sorting and quantity visibility """

        if not self.inventory:
            print("Inventory is empty...")
            return

        if show_qty == True:
            title = "Current inventory:"

        else:
            title = "Available products:"

        print(f"{title}\n")

        if sort == True:
            items = sorted(self.inventory.items())

        else:
            items = self.inventory.items()

        for product, quantity in items:
            if show_qty == True:
                print(f"{product}: {quantity}")

            else:
                print(f"{product}")


if __name__ == "__main__":
    inventory_mgr = InventoryManagement()

    inventory_mgr.add_product("manzanas", 10)
    inventory_mgr.add_product("peras", 5)
    inventory_mgr.add_product("kiwi", 3)


    inventory_mgr.view_inventory()

    result1 = inventory_mgr.mod_quantity("manzanas", 25)
    inventory_mgr.view_inventory()
