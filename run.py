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

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("quality_of_life_index")

# Create const variable to open each worksheet
# so can use later on code easily following the 'DRY' rule.
AFRICA = SHEET.worksheet("Africa").get_all_values()
ASIA = SHEET.worksheet("Asia").get_all_values()
EUROPE = SHEET.worksheet("Europe").get_all_values()
AMERICA = SHEET.worksheet("America").get_all_values()
OCEANIA = SHEET.worksheet("Oceania").get_all_values()


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
    os.system("cls" if os.name == "nt" else "clear")


def logo():
    """
    This function shows a welcome message and a
    logo to users when the application starts/run.
    """
    print(" ")
    print_slowly("WELCOME TO QUALITY OF LIFE INDEX !")
    time.sleep(1.5)
    print(" ")
    print(ts.B + "        ____    _        _____   ")
    print(ts.B + "       / __ \  | |      |_   _|  ")
    print(ts.B + "      | |  | | | |        | |    ")
    print(ts.C + "      | |  | | | |        | |    ")
    print(ts.C + "      | |  | | | |        | |    ")
    print(ts.C + "      | |__| | | |____   _| |_   ")
    print(ts.C + "       \___\_\ |______| |_____|  ")
    print(" ")
    time.sleep(3)
    clean_screen()


def app_info():
    """
    On this function will provide info about
    the app so users can understand what is QLI.
    """
    print(ts.W + " ")
    print_slowly("Quality of Life Index (higher is better)\n")
    print_slowly("is an estimation of overall quality of life,\n")
    print_slowly("using an empirical formula which consider:\n")
    print("--------------------------------------------")
    print_slowly(ts.G + "Purchasing power Index (higher is better)\n")
    print_slowly(ts.Y + "Pollution Index (lower is better)\n")
    print_slowly(ts.Y + "House price to Income ratio (lower is better)\n")
    print_slowly(ts.Y + "Cost of living Index (lower is better)\n")
    print_slowly(ts.G + "Safety Index (higher is better)\n")
    print_slowly(ts.G + "Health care Index (higher is better)\n")
    print_slowly(ts.Y + "Traffic commute time Index (lower is better)\n")
    print_slowly(ts.G + "Climate Index (higher is better)\n")
    print(ts.W + "--------------------------------------------")
    time.sleep(4)
    clean_screen()


def get_user_name():
    """
    Get users name from an input() method.
    """
    print(" ")
    print_slowly("Let's start exploring different countries...\n")
    time.sleep(1.5)
    print(" ")
    print_slowly("First insert your name with letters no\n")
    print_slowly("longer than 13 characters and no numbers.\n")
    print(" ")

    while True:
        username = input(ts.Y + "Please enter your name: \n")
        print(ts.W + " ")
        print_slowly(ts.C + "Validating your input value...\n")
        time.sleep(1.5)
        print(ts.W + "--------------------------------------------")

        if validate_username(username):
            print(" ")
            print(ts.G + "Input value entered is valid. Processing...\n")
            print(ts.W + "--------------------------------------------")
            time.sleep(1.5)
            clean_screen()
            break

    return username


def validate_username(username):
    """
    This function will validate users input name
    inside a try block and raise error if data is incorrect.
    Provides a clear error message.
    """
    try:
        # check for empty input value
        if username == "":
            raise ValueError(
                f"You entered empty value: '{username}'"
            )
        # chek for Enter keyword input value
        if username.strip() == "":
            raise ValueError(
                f"You entered empty value: '{username}'"
            )
        # check for numeric input value
        if username.isnumeric():
            raise ValueError(
                f"You entered numeric value: '{username}'"
            )
        # check the length of input value
        if len(username) > 13:
            raise ValueError(
                f"You entered more than 13 characters value: '{username}\n'"
            )
    except ValueError as error:
        print(' ')
        print(f"{ts.R}Invalid data:\n{error}.\nPlease enter correct value.\n")
        print(ts.W + "--------------------------------------------")
        time.sleep(3)
        clean_screen()
        return False

    return True


def select_continent():
    """
    This function will provide alternatives for user to
    choose from which Continent they want data.
    """
    username = get_user_name()
    print_slowly(f"{ts.W}Great {username} !\n")
    print(" ")
    print_slowly("Now please select one of the Continents you want\n")
    print_slowly("to get data from. Make your selection:\n")
    print(" ")
    while True:
        print_slowly(ts.Y + "Type one of the letters [a, b, c, d, e]\n")
        time.sleep(1)
        print(ts.C + "a) Africa\n")
        time.sleep(1)
        print(ts.C + "b) Asia\n")
        time.sleep(1)
        print(ts.C + "c) Europe\n")
        time.sleep(1)
        print(ts.C + "d) America\n")
        time.sleep(1)
        print(ts.C + "e) Oceania\n")
        time.sleep(1)
        # print(" ")
        user_choice = input(ts.W + "Please select one of the options: \n")

        if validate_cont_choice(user_choice):
            print(" ")
            print_slowly(f"{ts.G}Getting data for your selection...\n")
            print(" ")
            time.sleep(2)
            break

    return user_choice


def validate_cont_choice(user_choice):
    """
    This function validates if user has made
    a correct selection for continents above.
    """
    try:
        # check if user_choice value is not inside the list.
        if user_choice not in ["a", "b", "c", "d", "e"]:
            raise ValueError(f"You entered wrong value {user_choice}")
    except ValueError as error:
        print(f"{ts.R}Invalid selection:\n{error}. Please try again !\n ")
        time.sleep(3)
        clean_screen()
        return False

    return True


def access_sheet():
    """
    Based on user continent selection will
    access and open Google sheet (quality_of_life_index)
    so can get data for different countries.
    """
    # cont it's a short form of continent,used to reduce code lines
    user_cont = select_continent()
    if user_cont == "a":
        # cont_data access all data from worksheet named as below
        cont_data = AFRICA
        cont_name = "Africa"
        return cont_data, cont_name
    elif user_cont == "b":
        cont_data = ASIA
        cont_name = "Asia"
        return cont_data, cont_name
    elif user_cont == "c":
        cont_data = EUROPE
        cont_name = "Europe"
        return cont_data, cont_name
    elif user_cont == "d":
        cont_data = AMERICA
        cont_name = "America"
        return cont_data, cont_name
    else:
        cont_data = OCEANIA
        cont_name = "Oceania"
        return cont_data, cont_name


def main():
    """
    Here on this main function will call the other
    functions inside it. This way is more easy to call
    functions and control flow of app.
    """
    # logo()
    # app_info()
    access_sheet()


main()
