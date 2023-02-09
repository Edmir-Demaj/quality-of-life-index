"""
Import library to style text with colors for user on terminal.
"""
from colorama import init, Fore
# initialize colorama before using it on script.
init()


class TextStyle:
    """
    This class contains attributes for colors
    assigned to variables to reduce code repetion.
    """
    R = Fore.RED
    G = Fore.GREEN
    B = Fore.BLUE
    C = Fore.CYAN
    Y = Fore.YELLOW
    W = Fore.WHITE
