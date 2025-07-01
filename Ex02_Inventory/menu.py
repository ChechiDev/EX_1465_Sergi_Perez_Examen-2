import os
from lib import utils

class BaseMenu:
    def __init__(self):
        # Instancia
        self.ut = utils.Utils()

        # Attr
        self._pattern = "="
        self._width = 80
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

    def footer(self):
        """ Show the footer of the menu """

        print("\n" * 4)
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



if __name__ == "__main__":
    menu = ExitMenu()
    menu.exit()