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
        print(self._header_title)
        self.separator()



if __name__ == "__main__":
    menu = BaseMenu()
    menu.header()