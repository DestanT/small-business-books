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


def record_data(worksheet, year):
    """
    Get the date and data from the user,
    returns data given as a list.
    """
    headings_string = ''
    headings_list = SHEET.worksheet(f'{worksheet}_{year}').row_values(1)

    # Ignores last 2 columns: cash and total columns in "income" worksheets,
    # Or the "empty" and total columns in "expense" worksheets.
    for heading in headings_list[0:-3]:
        headings_string += heading + ', '
    headings_string += headings_list[-3] # Adds string without the ","

    # Gives user correctly lengthed example of input.
    example_print = ''
    for i in range(len(headings_list[0:-3])): # -3 because date index not considered.
        example_print += ',305'

    while True:
        print(f'Enter the date and {worksheet} data, separated by commas.')
        print('Data should be in the corresponding order:\n')
        print(headings_string)
        print(f'Example: DD/MM/YYYY{example_print}\n')

        data_str = input('Enter your data here:\n')

        data_list = data_str.split(',')

        if validate_data(data_list, headings_list[0:-2]):
            print('Data is valid!\n')
            break

    return data_list


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
        datetime.strptime(data[0], '%d/%m/%Y') # Checks date; index 0
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


def update_worksheet(data, worksheet):
    """
    Receives a data list, finds the date associated with data,
    and updates specified worksheet.
    """
    date = data[0]
    date_list = date.split('/')
    year = date_list[2]
    
    print(f'Updating "{worksheet}_{year}" worksheet...\n')
    worksheet_to_update = SHEET.worksheet(f'{worksheet}_{year}')
    row_to_update = worksheet_to_update.find(date).row
         
    income_data = [value for value in data]
    for i in range(len(income_data)):
        worksheet_to_update.update_cell(row_to_update, i + 1, income_data[i])

    print(f'"{worksheet}_{year}" worksheet updated successfully.\n')


def calculate_totals(data, worksheet):
    """
    Calculates total sums and updates specified worksheet.
    If worksheet == 'income'; calculates cash value for the day.
    """
    date = data[0]
    date_list = date.split('/')
    year = date_list[2]

    worksheet_to_update = SHEET.worksheet(f'{worksheet}_{year}')
    row_to_update = worksheet_to_update.find(date).row
    total_column = worksheet_to_update.find('Total').col

    total = 0
    for num in data[1:]:
        total += int(num)
    # Update "Total" column in specified worksheet
    worksheet_to_update.update_cell(row_to_update, total_column, total)
    
    if worksheet == 'income':
        card_column = worksheet_to_update.find('Card').col
        card_value = worksheet_to_update.cell(row_to_update, card_column).value
        cash_column = worksheet_to_update.find('Cash').col

        cash = total - int(card_value)
        # Update "Cash" column in specified worksheet
        worksheet_to_update.update_cell(row_to_update, cash_column, cash)
        
        print('Cash and')

    print('Total sum calculated.\n')
    

def main():
    income_data = record_data('income', 2023)
    update_worksheet(income_data, 'income')
    calculate_totals(income_data, 'income')

    expense_data = record_data('expense', 2023)
    update_worksheet(expense_data, 'expense')
    calculate_totals(expense_data, 'expense')


main()