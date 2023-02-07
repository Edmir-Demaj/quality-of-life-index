"""
Import libraries needed for the application to function,
aswell to style the output for user for better UX.
"""
import gspread
from google.oauth2.service_account import Credentials

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

print(EUROPE)
