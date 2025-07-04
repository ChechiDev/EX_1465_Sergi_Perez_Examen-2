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

    def footer(self, space=11):
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
        self._header_title = "Add New Product Menu"
        self.inventory = inventory


    def show_add_product(self):
        while True:
            self.header()
            self.inventory.view_inventory(sort=True, show_qty=False)
            self.footer()

            # Solicitamos al user por el nombre del producto nuevo:
            prod_name = input("Enter a product name: ").strip()

            # Verificamos que no esté vacío:
            if not prod_name:
                print("Product name cannot be empty")
                sleep(2)
                continue

            try:
                # validamos
                product_name = Product(prod_name, 0)
                break

            except ValueError as e:
                print(f"Error: {e}")
                sleep(2)
                continue


        # Solicitamos la cantidad
        while True:
            self.header()
            self.inventory.view_inventory(sort=True, show_qty=False)

            try:
                self.footer()
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
            self.footer(13)

            # Preguntamos si se quiere seguir añadiendo productos o no:
            continue_adding = input("Do you want to add another product? (y/n): ").strip().lower()

            if continue_adding in ["s", "si", "yes", "y"]:
                self.show_add_product()
                break # Seguims agregando

            elif continue_adding in ["n", "no"]:
                break # Salimos a landing menu

            else:
                print("Please enter 'y' to continue adding or 'n' to exit")
                sleep(2)


class DeleteProdMenu(BaseMenu):
    def __init__(self, inventory):
        super().__init__()
        self._header_title = "Delete product Menu"
        self.inventory = inventory


    def show_delete_product(self):
        # Primero checkeamos que el inventario no esté vacío
        if not self.inventory.inventory:
            self.header()
            print("No products available to delete.")
            self.footer(13)
            input("Press Enter to return to main menu...")
            return

        while True:
            self.header()
            self.inventory.view_inventory(sort=True, show_qty=False)
            self.footer()

            # Solicitamos al user por el nombre del producto nuevo:
            prod_name = input("Enter a product name to delete: ").strip()

            if not prod_name:
                print("Product name cannot be empty")
                sleep(2)
                continue

            try:
                # validamos
                product = Product(prod_name, 0)
                product_name = product.name
                break


            except ValueError as e:
                print(f"Error: {e}")
                sleep(2)
                continue


        # Traemos el nombre del producto desde la clase Product:
        product = Product(prod_name, 0)
        prod_name = product.name

        # Eliminamos el producto con el método del inventairo:
        del_prod = self.inventory.delete_product(prod_name)

        # Mostramos result:
        while True:
            self.header()
            if del_prod:
                print(f"Product: '{prod_name}' deleted from inventory succesfully!")

            else:
                print(f"Product: '{prod_name}' not found in inventory.")


            # Preguntamos si se quiere seguir borrando:
            self.footer(13)
            continue_deleting = input("Do you want to delete another product? (y/n): ").strip().lower()

            if continue_deleting in ["s", "si", "yes", "y"]:
                self.show_delete_product()
                break # Seguimos borrando

            elif continue_deleting in ["n", "no"]:
                break # Salimos a landing menu

            else:
                print("Please enter 'y' to continue adding or 'n' to exit")
                sleep(2)


class ConsultProdMenu(BaseMenu):
    def __init__(self, inventory):
        super().__init__()
        self._header_title = "Consult Product Stock Menu"
        self.inventory = inventory


    def show_consult_product(self):
        # Inventario está vacío:
        if not self.inventory.inventory:
            self.header()
            print("No products available to consult.")
            self.footer(13)
            input("Press Enter to return to main menu...")
            return


        while True:
            self.header()
            self.inventory.view_inventory(sort=True, show_qty=False)
            self.footer()

            # Solicitamos el nombre del producto:
            prod_name = input("Enter a product name to consult: ").strip()

            if not prod_name:
                print("Product name cannot be empty")
                sleep(2)
                continue

            # Validamos el nombre:
            try:
                product = Product(prod_name, 0)
                prod_name = product.name
                break

            except ValueError as e:
                print(f"Error: {e}")
                sleep(2)
                continue

        consult_prod = self.inventory.consult_product(prod_name)

        # Mostramos:
        while True:
            self.header()

            if consult_prod:
                print("Product found in inventory\n")
                print(f"Product: {consult_prod['product']}")
                print(f"Quantity: {consult_prod['quantity']} units")

            else:
                print("Product not found...")

            self.footer(13)

            continue_consulting = input("Do you want to consult another product? (y/n): ").strip().lower()

            if continue_consulting in ["s", "si", "yes", "y"]:
                self.show_consult_product()
                break

            elif continue_consulting in ["n", "no"]:
                break

            else:
                print("Please enter 'y' to continue or 'n' to exit")
                sleep(1)


class ModifProdQtyMenu(BaseMenu):
    def __init__(self, inventory):
        super().__init__()
        self._header_title = "Modify Product Quantity Menu"
        self.inventory = inventory

    def show_modify_quantity(self):
        # Verificar si el inventario está vacío
        if not self.inventory.inventory:
            self.header()
            print("No products available to modify.")
            self.footer(13)
            input("Press Enter to return to main menu...")
            return

        # Bucle para solicitar el nombre del producto
        while True:
            self.header()
            self.inventory.view_inventory(sort=True, show_qty=True)
            self.footer()

            # Solicitar el nombre del producto
            prod_name = input("Enter a product name to modify: ").strip()

            if not prod_name:
                print("Product name cannot be empty")
                sleep(2)
                continue

            # Validar el nombre del producto
            try:
                product = Product(prod_name, 0)
                prod_name = product.name
                break

            except ValueError as e:
                print(f"Error: {e}")
                sleep(2)
                continue

        # Solicitamos a user la nueva qty
        while True:
            self.header()
            self.inventory.view_inventory(sort=True, show_qty=False)

            try:
                self.footer()
                new_qty = int(input("Enter new quantity: "))
                break

            except ValueError:
                print("Please enter a valid number")
                sleep(2)
                continue

        # Modificamos
        modify_result = self.inventory.mod_quantity(prod_name, new_qty)

        # Mostramos:
        while True:
            self.header()

            if modify_result:
                print(f"Product '{prod_name}' quantity updated successfully!")
                print(f"New quantity: {new_qty} units")

            else:
                print(f"Failed to update product '{prod_name}'.")
                print("Product not found in inventory.")

            self.footer(13)

            # Preguntamos si quiere modificar más:
            continue_modifying = input("Do you want to modify another product quantity? (y/n): ").strip().lower()

            if continue_modifying in ["s", "si", "yes", "y"]:
                self.show_modify_quantity()
                break

            elif continue_modifying in ["n", "no"]:
                break

            else:
                print("Please enter 'y' to continue or 'n' to exit")
                sleep(2)


class FindProdMenu(BaseMenu):
    def __init__(self, inventory):
        super().__init__()
        self._header_title = "Find Product Menu"
        self.inventory = inventory

    def show_find_product(self):
        # Lo de siempre... vacio?
        if not self.inventory.inventory:
            self.header()
            print("No products available to search.")
            self.footer(13)
            input("Press Enter to return to main menu...")
            return


        while True:
            self.header()
            self.inventory.view_inventory(sort=True, show_qty=False)
            self.footer()

            search_text = input("Enter text to search for products: ").strip()

            if not search_text:
                print("Search text cannot be empty")
                sleep(2)
                continue

            break

        # Buscamos los productos con el método de inventory:
        found_products = self.inventory.find_product(search_text)

        # Mostrar resultados
        while True:
            self.header()

            if found_products:
                print(f"Search results for '{search_text}':\n")
                print(f"Found {len(found_products)} product(s):\n")

                for product in found_products:
                    print(f"{product['product']}: {product['quantity']} units")

            else:
                print(f"No products found containing '{search_text}'")

            self.footer(13)

            # Preguntar si quiere buscar más productos
            continue_searching = input("Do you want to search for another product? (y/n): ").strip().lower()

            if continue_searching in ["s", "si", "yes", "y"]:
                self.show_find_product()
                break

            elif continue_searching in ["n", "no"]:
                break

            else:
                print("Please enter 'y' to continue or 'n' to exit")
                sleep(2)


class LandingMenu(BaseMenu):
    def __init__(self):
        super().__init__()
        # Instancia:
        self.inventory = InventoryManagement()
        self.add_menu = AddProdMenu(self.inventory)
        self.delete_menu = DeleteProdMenu(self.inventory)
        self.consult_menu = ConsultProdMenu(self.inventory)
        self.modify_menu = ModifProdQtyMenu(self.inventory)
        self.find_menu = FindProdMenu(self.inventory)
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

                elif user_opt == "3":
                    self.consult_menu.show_consult_product()

                elif user_opt == "4":
                    self.modify_menu.show_modify_quantity()

                elif user_opt == "5":
                    self.find_menu.show_find_product()

                elif user_opt == "6":
                    self.header()
                    self.inventory.view_inventory(sort=True, show_qty=True)
                    self.footer(13)
                    input("Press Enter to return to main menu...")

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