import gspread
from google.oauth2.service_account import Credentials

# Code taken from Code Institute's "Love Sandwiches" project
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
    
# Code taken from Code Institute's "Love Sandwiches" project
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('small_business_books')


def record_income_data(year):
    """
    Get income data input from the user.
    """
    headings_string = ''
    headings_list = SHEET.worksheet(f'income_{year}').row_values(1)

    for heading in headings_list[0:-3]:
        headings_string += heading + ', '
    headings_string += headings_list[-3]

    print('Enter the date and income data, separated by commas.')
    print('Data should be in the corresponding order:\n')
    print(headings_string)
    print('Example: DD/MM/YYYY,500,600,700,800,500,400\n')

    data_str = input('Enter your data here:\n')

    income_data = data_str.split(',')

    return income_data
    
record_income_data(2023)