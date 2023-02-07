"""
Import libraries to style text and make
typing with animation for users on mok terminal.
"""
from colorama import init, Fore

init()

class TextStyle:
    """
    This class contains attributes for colors and
    a method to type slowly the text on terminal
    """
    R = Fore.RED
    G = Fore.GREEN
    B = Fore.BLUE
    C = Fore.CYAN
    Y = Fore.YELLOW
    W = Fore.WHITE

