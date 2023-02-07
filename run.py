"""
Import libraries needed for the application to function,
aswell to style the output for user for better UX.
"""
import sys
import os
import time
import gspread
from google.oauth2.service_account import Credentials
from style import TextStyle as ts

# Code below was taken from love_sandwiches walkthrough project
# with Code Institute. Refered to Credits on README.md file.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('quality_of_life_index')

# Create const variable to open each worksheet
# so can use later on code easily following the 'DRY' rule.
AFRICA = SHEET.worksheet('Africa').get_all_values()
ASIA = SHEET.worksheet('Asia').get_all_values()
EUROPE = SHEET.worksheet('Europe').get_all_values()
AMERICA = SHEET.worksheet('America').get_all_values()
OCEANIA = SHEET.worksheet('Oceania').get_all_values()


# Code below was taken from Stack Owerflow.
# Refered to Credits on README.md file.
def print_slowly(text):
    """
    Types text with animation slowing typing
    time for print statment on terminal.
    """
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.08)


def clean_screen():
    """
    This function clean terminal from content when
    is called, it refers to the operating system OS.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def logo():
    """
    This function shows a welcome message and a
    logo to users when the application starts/run.
    """
    print(' ')
    print_slowly('WELCOME TO QUALITY OF LIFE INDEX !')
    time.sleep(1.5)
    print(' ')
    print(ts.B + "        ____    _        _____   ")
    print(ts.B + "       / __ \  | |      |_   _|  ")
    print(ts.B + "      | |  | | | |        | |    ")
    print(ts.C + "      | |  | | | |        | |    ")
    print(ts.C + "      | |  | | | |        | |    ")
    print(ts.C + "      | |__| | | |____   _| |_   ")
    print(ts.C + "       \___\_\ |______| |_____|  ")
    print(' ')
    time.sleep(3)
    clean_screen()


def main():
    """
    Here on this main function will call the other
    functions inside it. This way is more easy to call
    functions and control flow of app.
    """
    logo()
