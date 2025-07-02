import os
import platform as plat

class Utils:

    @staticmethod
    def clear_terminal():
        """ Clears the terminal """

        if plat.system() == "Windows":
            os.system("cls")

        else:
            os.system("clear")

    @staticmethod
    def center_txt(txt: str, width: int) -> None:
        """ Centers the given text within the specified width """

        return txt.center(width)