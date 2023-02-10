"""
Import libraries needed for application functionality,
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

# Create const variables to open each worksheet
# so can use later on code easily avoiding the 'DRY' rule.
AFRICA = SHEET.worksheet("Africa")
ASIA = SHEET.worksheet("Asia")
EUROPE = SHEET.worksheet("Europe")
AMERICA = SHEET.worksheet("America")
OCEANIA = SHEET.worksheet("Oceania")


# Code below was taken from Stack Owerflow.
# Refered to Credits on README.md file.
def print_slowly(text):
    """
    Types text with animation, slowing typing
    time for print statments on terminal.
    """
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.06)


# Code below was taken from Stack Owerflow.
# Refered to Credits on README.md file.
def clean_screen():
    """
    Clean terminal from content when is called,
    it refers to the operating system OS.
    """
    os.system("cls" if os.name == "nt" else "clear")


def logo():
    """
    Shows a welcome message and a logo to user
    when the application starts.
    """
    print(" ")
    print_slowly(ts.G + ">  Welcome to Quality of Life Index !")
    time.sleep(1.5)
    print(" ")
    print(" ")
    print(ts.C + r"        ____    _        _____   ")
    print(ts.C + r"       / __ \  | |      |_   _|  ")
    print(ts.C + r"      | |  | | | |        | |    ")
    print(ts.C + r"      | |  | | | |        | |    ")
    print(ts.C + r"      | |  | | | |        | |    ")
    print(ts.C + r"      | |__| | | |____   _| |_   ")
    print(ts.C + r"       \___\_\ |______| |_____|  ")
    print(" ")
    print(" ")
    print_slowly(ts.G + ">     Developed by Edmir Demaj.")
    time.sleep(3)
    clean_screen()


def app_info():
    """
    Provide info about the app so user can understand what is QLI
    and how is calculated for Countries.
    """
    print(" ")
    print(ts.W + "Quality of Life Index (higher is better)")
    print("is an estimation of overall quality of life,")
    print("using an empirical formula which consider:")
    time.sleep(3)
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
    print(ts.G + "Climate Index (higher is better)")
    print(ts.W + "--------------------------------------------")
    time.sleep(6)
    clean_screen()


def get_user_name():
    """
    Get user name from an input method. Run a While Loop
    until input is valid.
    """
    print(" ")
    print_slowly(ts.W + "Let's start...\n")
    time.sleep(1.5)
    print(" ")
    print("First insert your name with letters between")
    print("2 and 13 characters long and no numbers.\n")

    while True:
        name = input(ts.Y + "Please enter your name:\n")
        username = name.strip()
        print(" ")
        print("Validating your input value...\n")
        time.sleep(2)
        print(ts.W + "--------------------------------------------")

        if validate_username(username):
            print(ts.G + "Input value entered is valid. Processing...")
            print(ts.W + "--------------------------------------------")
            time.sleep(2)
            clean_screen()
            break

    return username


def validate_username(username):
    """
    Validate user input name inside a try block
    and raise specific error if data is incorrect.
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
        print(f"{ts.R}Invalid data:\n{error}.\nPlease enter correct value.")
        print(ts.W + "--------------------------------------------")
        time.sleep(3)
        clean_screen()
        return False

    return True


def select_continent(*name):
    """
    This function runs a statement with user name. Provide list
    of Continents to get data from and get user selection with input method.
    Has a While Loop which runs until user insert valid input.
    """
    if name:
        user = name[0].capitalize()
        print(" ")
        print(f"{ts.W}Great {ts.Y}{user} !\n")
        time.sleep(1.5)
    print(ts.W + "Now please select one of the Continents to get data:")

    while True:
        print(ts.Y + "Type one of the letters [a, b, c, d, e]\n")
        print(ts.C + "a) Africa\n")
        print(ts.C + "b) Asia\n")
        print(ts.C + "c) Europe\n")
        print(ts.C + "d) America\n")
        print(ts.C + "e) Oceania\n")
        choice = input(ts.Y + "Please select one of the options:\n")
        user_choice = choice.lower().strip()
        print(" ")
        print("Validating your input value...\n")
        time.sleep(2)
        print(ts.W + "--------------------------------------------")

        if validate_cont_choice(user_choice):
            print(f"{ts.G}Input valid. Proceessing...")
            print(ts.W + "--------------------------------------------")
            time.sleep(2)
            clean_screen()
            break

    return user_choice


def validate_cont_choice(user_choice):
    """
    Validates if user input for function above is valid.
    Inside a try block valide input and inside except
    block print the error raised on try block.
    """
    try:
        # check if user_choice value is not inside the list.
        if user_choice not in ["a", "b", "c", "d", "e"]:
            raise ValueError(f"You entered wrong value: '{user_choice}'")
    except ValueError as error:
        print(f"{ts.R}Invalid selection:\n{error}. Please try again ! ")
        print(ts.W + "--------------------------------------------")
        time.sleep(3)
        clean_screen()
        return False

    return True


def access_sheet(user_cont):
    """
    Based on user continent selection this function
    access Google sheet (quality_of_life_index), so can
    get data for different countries in that continent.
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
    Shows info how to select a Country to get data for.
    Get users Country name with input method. Run a While Loop
    until Contry name is valid. Provide data for Country selected.
    """
    user_cont_name = cont_name[1]
    print(" ")
    print(f"{ts.W}Now choose a Country from {ts.Y}{user_cont_name}")
    print(f"{ts.W}to get the {ts.Y}Quality of Life Index.\n")
    time.sleep(1)
    print(f"{ts.R}*** Important ! ***")
    print(f"{ts.W}In order to receive data, the name of the")
    print(f"{ts.W}Country name should be typed as the example:\n")
    time.sleep(1)
    print_slowly(f"{ts.C}Ireland or\n")
    print_slowly(f"{ts.C}Czech Republic or\n")
    print_slowly(f"{ts.C}New Zealand etc.\n")
    while True:
        print(" ")
        user_country = input(ts.Y + "Please enter the name of Country:\n")
        country_name = user_country.title().strip()
        time.sleep(1)

        if validate_country(country_name, cont_name):
            # Find the cell where Country belongs on worksheet
            cell = cont_name[0].find(country_name, in_column=2)
            # Based on cell get row number to access all data for that Country
            row = cell.row
            # Get data from the specific row
            country_index = cont_name[0].row_values(row)
            print(" ")
            print(f"Showing data for {ts.C}{country_name}: \n")
            time.sleep(1.5)
            print(f"{ts.W}Quality of Life Index: {country_index[2]}\n")
            print(f"Rank in {cont_name[1]} is: {country_index[0]}\n")
            time.sleep(2)
            print(ts.W + "--------------------------------------------")
            print(ts.G + "If Q.L.I bigger than 160 (High Quality of Life)")
            time.sleep(1)
            print(" ")
            print(ts.Y + "If Q.L.I between 100-160 (Medium Quality of Life)")
            time.sleep(1)
            print(" ")
            print(ts.R + "If Q.L.I smaller than 100 (Low Quality of Life)")
            print(ts.W + "--------------------------------------------")
            time.sleep(6)
            clean_screen()
            break

    return country_name, cont_name, country_index


def validate_country(country_name, cont_name):
    """
    Validate if Country selected from user is valid on
    database of QLI sheet. If not ask for different Country name.
    """
    country_column = cont_name[0].col_values(2)

    if country_name in country_column:
        print(" ")
        print(ts.W + "--------------------------------------------")
        print(f"{ts.G}Getting data for {ts.C}{country_name}...")
        print(ts.W + "--------------------------------------------")
        time.sleep(1.5)
        clean_screen()
        return True
    else:
        print(" ")
        print(ts.W + "--------------------------------------------")
        print(ts.R + "Sorry but we don't have any data for:")
        print(f"{ts.C}'{country_name}' in '{cont_name[1]}'.")
        print(ts.R + "Make sure your Country name is correct!")
        print(ts.W + "--------------------------------------------\n")
        print(ts.Y + "Please try again different Country!")
        time.sleep(4)
        clean_screen()
        return False


def specific_data(index):
    """
    Provide more specific data if user wants
    to get more details about Country selected.
    Validate the answer from user.
    """
    print(" ")
    print("Would you like to get more specific data?\n")
    answer_choice = input("Enter yes/no:\n")
    answer = answer_choice.lower().strip()

    if answer == "yes":
        time.sleep(1)
        clean_screen()
        print(f"{ts.W}Showing specific data for {index[0]}: ")
        time.sleep(2)
        print(f"{ts.G}Purchasing Power Index: {index[2][3]}")
        print("Higher is better 0-100\n")
        time.sleep(1.5)
        print(f"{ts.R}Pollution Index: {index[2][9]}")
        print("Lower is better 0-100\n")
        time.sleep(1.5)
        print(f"{ts.R}House Price to Income Ratio: {index[2][7]}")
        print("Lower is better 0-100\n")
        time.sleep(1.5)
        print(f"{ts.R}Cost of Living Index: {index[2][6]}")
        print("Lower is better 0-100\n")
        time.sleep(1.5)
        print(f"{ts.G}Safety Index is: {index[2][4]}")
        print("Higher is better 0-100\n")
        time.sleep(1.5)
        print(f"{ts.G}Health Care Index: {index[2][5]}")
        print("Higher is better 0-100\n")
        time.sleep(1.5)
        print(f"{ts.R}Traffic Commute Time Index: {index[2][8]}")
        print("Lower is better 0-100\n")
        time.sleep(1.5)
        print(f"{ts.G}Climate Index: {index[2][10]}")
        print("Higher is better 0-100")
        time.sleep(6)
        clean_screen()
        other_country()
    elif answer == "no":
        time.sleep(1)
        clean_screen()
        other_country()
    else:
        print(" ")
        time.sleep(1)
        print(ts.W + "--------------------------------------------")
        print(ts.R + "Wrong answer! Try again.")
        print(ts.W + "--------------------------------------------")
        time.sleep(2)
        clean_screen()
        specific_data(index)

    return answer


def other_country():
    """
    Ask user if they want data for another country.
    Validate the answer from user.
    """
    print(" ")
    print(ts.Y + "Would you like to get QLI for another Country?\n")
    other_count = input("Enter yes/no:\n")
    other_count_answer = other_count.lower().strip()

    if other_count_answer == "yes":
        time.sleep(1)
        clean_screen()
        user_cont = select_continent()
        worksheet = access_sheet(user_cont)
        data = select_country(worksheet)
        specific_data(data)
    elif other_count_answer == "no":
        time.sleep(1)
        clean_screen()
        print(" ")
        print(ts.W + "Terminating application...\n")
        time.sleep(2)
        print(" ")
        print(ts.W + "--------------------------------------------")
        print_slowly(ts.Y + "Thank you for using Quality of Life Index.\n")
        print(" ")
        print("              **********                   ")
        print(" ")
        print_slowly("     Copyright Edmir Demaj - 2023\n")
        print(ts.W + "--------------------------------------------")
        print(" ")
        time.sleep(4)
        clean_screen()
    else:
        print(" ")
        time.sleep(1)
        print(ts.W + "--------------------------------------------")
        print(ts.R + "Wrong answer! Try again.")
        print(ts.W + "--------------------------------------------")
        time.sleep(2)
        clean_screen()
        other_country()


def main():
    """
    Run all program functions.
    """
    logo()
    app_info()
    name = get_user_name()
    user_cont = select_continent(name)
    worksheet = access_sheet(user_cont)
    data = select_country(worksheet)
    specific_data(data)


main()
