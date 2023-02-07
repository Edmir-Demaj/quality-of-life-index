"""
Import library to style text for users on terminal.
"""
from colorama import init, Fore

init()


class TextStyle:
    """
    This class contains attributes for colors
    assigned to variables to reduce code.
    """
    R = Fore.RED
    G = Fore.GREEN
    B = Fore.BLUE
    C = Fore.CYAN
    Y = Fore.YELLOW
    W = Fore.WHITE
