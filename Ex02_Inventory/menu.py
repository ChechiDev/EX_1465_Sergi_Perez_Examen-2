from time import sleep
from lib import utils
from lib import validation
from inventory import InventoryManagement, Product

class BaseMenu:
    def __init__(self):
        # Instancia
        self.ut = utils.Utils()
        self.validation = validation.Validation()

        # Attr
        self._pattern = "="
        self._width = 100
        self._header_title = "Inventory Management"

    def separator(self):
        """ Shows separation barr """

        print(self._pattern * self._width)

    def header(self):
        """ Shows the menu header """

        self.ut.clear_terminal()
        self.separator()
        print(self.ut.center_txt(self._header_title, self._width))
        self.separator()

    def footer(self, space=1):
        """ Show the footer of the menu """

        print("\n" * space)
        self.separator()


class ExitMenu(BaseMenu):
    def __init__(self):
        super().__init__()

    def exit(self):
        """ Shows the exit menu """

        self.ut.clear_terminal()
        self.header()
        print(f"Thank you for visiting us!")
        self.footer()


class AddProdMenu(BaseMenu):
    def __init__(self, inventory):
        super().__init__()
        self._header_title = "Add New Product"
        self.inventory = inventory


    def show_add_product(self):
        while True:
            self.header()
            self.inventory.view_inventory()
            self.footer()

            # Solicitamos al user por el nombre del producto nuevo:
            prod_name = input("Enter a product name: ").strip()

            # Verificamos que no esté vacío:
            if prod_name:
                break

            else:
                print("Product name cannot be empty")
                sleep(2)
                continue

        # Solicitamos la cantidad
        while True:
            self.header()
            self.inventory.view_inventory()

            try:
                self.footer(2)
                qty = int(input("Enter quantity: "))
                break

            except ValueError:
                print("Please enter a valid number")
                sleep(2)
                continue

        # Obtenemos el nombre validado
        product = Product(prod_name, qty)

        # Agregamos el product validado:
        self.inventory.add_product(prod_name, qty)

        # Mostramos:
        while True:
            self.header()
            print(f"Product '{product.name}' added successfully!")
            self.footer(3)

            # Preguntamos si se quiere seguir añadiendo productos o no:
            continue_adding = input("Do you want to add another product? (y/n): ").strip().lower()

            if continue_adding in ["s", "si", "yes", "y"]:
                self.show_add_product()
                break # Seguims agregando

            elif continue_adding in ["n", "no"]:
                break # Salimos a landing menu

            else:
                print("Please enter 'y' to continue adding or 'n' to exit")
                sleep(1)


class DeleteProdMenu(BaseMenu):
    def __init__(self, inventory):
        super().__init__()
        self._header_title = "Delete product"
        self.inventory = inventory


    def show_delete_product(self):
        pass


class LandingMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        # Instancia:
        self.inventory = InventoryManagement()
        self.add_menu = AddProdMenu(self.inventory)
        self.delete_menu = DeleteProdMenu(self.inventory)
        self.exit_menu = ExitMenu()

        self.menu_opt = [
            "Add new product",
            "Delete product",
            "Consult a product",
            "Modify a product quantity",
            "Find a product",
            "View inventory"
        ]


    def show_user_options(self):
        """ Display user menu options """

        self.header()
        for idx, opt in enumerate(self.menu_opt):
            print(f"\n{idx + 1}. {opt}")

        print("\n0. Exit\n")
        self.separator()


    def run(self):
        """ Main menu options loop """

        while True:
            self.show_user_options()

            try:
                user_opt = input("Select an option: ").strip()

                if user_opt == "1":
                    self.add_menu.show_add_product()

                elif user_opt == "2":
                    self.delete_menu.show_delete_product()

                elif user_opt == "0":
                    self.exit_menu.exit()
                    break

                else:
                    print("Invalid option...")
                    sleep(1)
                    continue

            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    menu = LandingMenu()
    menu.run()