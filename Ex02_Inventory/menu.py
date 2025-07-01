from time import sleep
from lib import utils
from lib import validation
from inventory import InventoryManagement

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
            prod_name = input("Enter a product name: ")

            # Validamos que no tenga números ni carácteres raros:
            prod_valid = self.validation.val_string(prod_name)
            if not prod_valid:
                print("Error: Product name must contain only alphabetic characters without accents")
                sleep(2)
                continue

            break

        # Solicitamos la cantidad
        while True:
            self.header()
            self.inventory.view_inventory()
            # self.footer()

            try:
                self.footer(2)
                qty = int(input("Enter quantity: "))
                if qty <= 0:
                    print("Quantity must be positive")
                    continue

                break

            except ValueError:
                print("Please enter a valid number")
                continue


        # Agregamos el producto al dict con el método add_product de inventory:
        add = self.inventory.add_product(prod_name, qty)
        self.header()
        print(f"Product '{prod_name}' added successfully!")
        self.footer(2)
        sleep(2)



class LandingMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        # Instancia:
        self.inventory = InventoryManagement("inicial", 0)
        self.add_menu = AddProdMenu(self.inventory)
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