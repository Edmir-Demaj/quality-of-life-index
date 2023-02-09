"""
Import libraries needed for the application to function,
aswell to style the output on terminal for better UX.
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
AFRICA = SHEET.worksheet("Africa")
ASIA = SHEET.worksheet("Asia")
EUROPE = SHEET.worksheet("Europe")
AMERICA = SHEET.worksheet("America")
OCEANIA = SHEET.worksheet("Oceania")


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
        time.sleep(0.06)


def clean_screen():
    """
    This function clean terminal from content when
    is called, it refers to the operating system OS.
    """
    os.system("cls" if os.name == "nt" else "clear")


def logo():
    """
    Shows a welcome message and a logo to users
    when the application starts/run.
    """
    print(" ")
    print_slowly("Welcome to Quality of Life Index !")
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
    Provide info about the app so users can understand what is QLI.
    """
    print(ts.W + "Quality of Life Index (higher is better)\n")
    print("is an estimation of overall quality of life,\n")
    print("using an empirical formula which consider:\n")
    time.sleep(2)
    print("--------------------------------------------")
    print(ts.G + "Purchasing power Index (higher is better)\n")
    time.sleep(1)
    print(ts.Y + "Pollution Index (lower is better)\n")
    time.sleep(1)
    print(ts.Y + "House price to Income ratio (lower is better)\n")
    time.sleep(1)
    print(ts.Y + "Cost of living Index (lower is better)\n")
    time.sleep(1)
    print(ts.G + "Safety Index (higher is better)\n")
    time.sleep(1)
    print(ts.G + "Health care Index (higher is better)\n")
    time.sleep(1)
    print(ts.Y + "Traffic commute time Index (lower is better)\n")
    time.sleep(1)
    print(ts.G + "Climate Index (higher is better)\n")
    time.sleep(4)
    clean_screen()


def get_user_name():
    """
    Get users name from an input() method.
    """
    print(" ")
    print_slowly("Let's start...\n")
    time.sleep(1.5)
    print(" ")
    print("First insert your name with letters between\n")
    print("2 and 13 characters long and no numbers.\n")

    while True:
        username = input(ts.Y + "Please enter your name: \n")
        print(" ")
        print("Validating your input value...\n")
        time.sleep(1.5)
        print(ts.W + "--------------------------------------------")

        if validate_username(username):
            print(ts.G + "Input value entered is valid. Processing...\n")
            time.sleep(1.5)
            clean_screen()
            break

    return username


def validate_username(username):
    """
    Validate users input name inside a try block
    and raise error if data is incorrect.
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
        if len(username) > 13 or len(username) < 2:
            raise ValueError(
                f"You entered wrong number of characters: '{len(username)}'"
            )
    except ValueError as error:
        print(f"{ts.R}Invalid data:\n{error}.\nPlease enter correct value.\n")
        time.sleep(3)
        clean_screen()
        return False

    return True


def select_continent(*name):
    """
    This function will provide alternatives for user to
    choose from which Continent they want data.
    """
    if name:
        user = name[0].capitalize()
        print(f"{ts.W}Great {ts.Y}{user} !\n")
        time.sleep(1.5)
    print(ts.W + "Now please select one of the Continents to get data:\n")

    while True:
        print(ts.Y + "Type one of the letters [a, b, c, d, e]\n")
        print(ts.B + "a) Africa\n")
        print(ts.B + "b) Asia\n")
        print(ts.B + "c) Europe\n")
        print(ts.B + "d) America\n")
        print(ts.B + "e) Oceania\n")
        choice = input(ts.Y + "Please select one of the options: \n")
        user_choice = choice.lower()
        print(" ")
        print("Validating your input value...\n")
        time.sleep(1.5)
        print(ts.W + "--------------------------------------------")

        if validate_cont_choice(user_choice):
            print(f"{ts.G}Input valid. Proceessing...\n")
            time.sleep(1.5)
            clean_screen()
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
            raise ValueError(f"You entered wrong value: '{user_choice}'")
    except ValueError as error:
        print(f"{ts.R}Invalid selection:\n{error}. Please try again !\n ")
        time.sleep(3)
        clean_screen()
        return False

    return True


def access_sheet(user_cont):
    """
    Based on user continent selection will
    access and open Google sheet (quality_of_life_index)
    so can get data for different countries.
    """
    # cont it's a short form of continent,used to reduce code lines
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


def select_country(cont_name):
    """
    This function provides user with info how to select
    the Country they want data from, get users Country name
    and provide data for that Country.
    """
    user_cont_name = cont_name[1]
    print(f"{ts.W} Now choose a Country from {ts.Y}{user_cont_name}\n")
    print(f"{ts.W} to get the {ts.Y}Quality of Life Index.\n")
    time.sleep(1)
    print(f"{ts.R} *** Important ! ***\n")
    print(f"{ts.W} In order to receive data, the name of the\n")
    print(f"{ts.W} Country should be typed as the example:\n")
    time.sleep(1)
    print_slowly(f"{ts.B} Ireland or\n")
    print_slowly(f"{ts.B} Czech Republic or\n")
    print_slowly(f"{ts.B} New Zealand etc.\n")
    while True:
        print(" ")
        user_country = input(ts.Y + "Please enter the name of Country: \n")
        country_name = user_country.capitalize()
        time.sleep(1)

        if validate_country(country_name, cont_name):
            # Find the cell where Country belongs on worksheet
            cell = cont_name[0].find(country_name, in_column=2)
            # Based on cell get row number to access all data for that Country
            row = cell.row
            # Get data from the specifi row
            country_index = cont_name[0].row_values(row)
            print(f"Showing data for {country_name}: \n")
            time.sleep(1)
            print(f"Quality of Life Index: {country_index[2]}\n")
            print(f"Rank in {cont_name[1]} is: {country_index[0]}\n")
            time.sleep(1)
            print(ts.W + "--------------------------------------------")
            print(ts.G + "If Q.L.I bigger than 160 (High Quality of Life)")
            print(" ")
            print(ts.Y + "If Q.L.I between 100-160 (Medium Quality of Life)")
            print(" ")
            print(ts.R + "If Q.L.I smaller than 100 (Low Quality of Life)")
            print(ts.W + "--------------------------------------------")
            time.sleep(5)
            clean_screen()
            break

    return country_name, cont_name, country_index


def validate_country(country_name, cont_name):
    """
    Validate if Country choosed from user is
    valid on database of QLI sheet.
    """
    country_column = cont_name[0].col_values(2)

    if country_name in country_column:
        print(" ")
        print(f"Getting data for {ts.B}{country_name}...\n")
        print(ts.W + "--------------------------------------------")
        time.sleep(1.5)
        clean_screen()
        return True
    else:
        print(ts.W + "--------------------------------------------")
        print(ts.R + "Sorry but we don't have any data for:\n")
        print(f"{ts.B}'{country_name}' in '{cont_name[1]}'.\n")
        print(ts.R + "Make sure your Country name is correct!\n")
        print("Please try again different Country!\n")
        time.sleep(3)
        clean_screen()
        return False


def specific_data(index):
    """
    Function to provide more specific data if user wants
    to get more details about Country.
    """
    while True:
        print_slowly("Would you like to get more specific data?\n")
        answer = input("Enter yes/no:\n")

        if validate_answer(answer):
            print(ts.G + "Higher is better 0-100")
            print(f"Purchasing Power Index is: {index[2][3]}\n")
            time.sleep(1.2)
            print(ts.R + "Lower is better 0-100")
            print(f"Pollution Index: {index[2][9]}\n")
            time.sleep(1.2)
            print(ts.R + "Lower is better 0-100")
            print(f"House Price to Income Ratio: {index[2][7]}\n")
            time.sleep(1.2)
            print(ts.R + "Lower is better 0-100")
            print(f"Cost of Living Index: {index[2][6]}\n")
            time.sleep(1.2)
            print(ts.G + "Higher is better 0-100")
            print(f"Safety Index is: {index[2][4]}\n")
            time.sleep(1.2)
            print(ts.G + "Higher is better 0-100")
            print(f"Health Care Index: {index[2][5]}\n")
            time.sleep(1.2)
            print(ts.R + "Lower is better 0-100")
            print(f"Traffic Commute Time Index: {index[2][8]}\n")
            time.sleep(1.2)
            print(ts.G + "Higher is better 0-100")
            print(f"Climate Index: {index[2][10]}\n")
            time.sleep(7)
            clean_screen()
            other_country()
            break

    return answer


def validate_answer(answer):
    """
    Will validate users answer if yes/no and
    will provide more data or error message.
    """
    if answer == "yes":
        print(" ")
        print("Getting specific data...\n")
        time.sleep(1.5)
        clean_screen()
        return True
    elif answer == "no":
        print(" ")
        other_country()
        print(" ")
        return False
    else:
        print("wrong answer")


def other_country():
    """
    Ask user if they want data for another country.
    Validate the answer from user.
    """
    print_slowly("Would you like to get QLI for another Country?\n")
    other_count_answer = input("Enter yes/no: \n")

    if other_count_answer == "yes":
        clean_screen()
        user_cont = select_continent()
        worksheet = access_sheet(user_cont)
        data = select_country(worksheet)
        specific_data(data)
    elif other_count_answer == "no":
        print(" ")
        print_slowly("Thank you for using Quality of Life Index application.")
        print(" (c) Edmir Demaj 2023")
        print(" ")
        time.sleep(2)
        clean_screen()


def main():
    """
    Here on this main function will call the other
    functions inside it.
    """
    # logo()
    # app_info()
    name = get_user_name()
    user_cont = select_continent(name)
    worksheet = access_sheet(user_cont)
    data = select_country(worksheet)
    # specific_data(data)


main()
