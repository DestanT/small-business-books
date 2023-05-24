import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

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

    # Ignores last 2 columns: cash, total.
    for heading in headings_list[0:-3]:
        headings_string += heading + ', '
    headings_string += headings_list[-3] # Adds string without the ","

    while True:
        print('Enter the date and income data, separated by commas.')
        print('Data should be in the corresponding order:\n')
        print(headings_string)
        print('Example: DD/MM/YYYY,500,600,700,800,500,400\n')

        data_str = input('Enter your data here:\n')

        income_data = data_str.split(',')

        if validate_data(income_data, headings_list[0:-2]):
            print('Data is valid!')
            break

    return income_data


def validate_data(data, headings):
    """
    Checks the date is in the right format,
    Checks if data[1:] can be converted to int,
    Checks if len(data) matches len(headings),
    Raises Errors accordingly.
    """
    # CREDIT - datetime method:
    # https://paperbun.org/validate-date-string-format-in-python/
    try:
        datetime.strptime(data[0], '%d/%m/%Y') # Checks date only
        [int(value) for value in data[1:]] # Skips date index
        if len(data) != len(headings):
            raise ValueError(
                f'Exactly {len(headings)-1} values needed, you entered {len(data)-1}'
            )
    except ValueError as e:
        print(f'Invalid date string: {e}, please try again.\n')
        return False
    except TypeError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False
    
    return True

    
    
    
record_income_data(2023)