import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import plotext as plt

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


def update_worksheet(worksheet, data):
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


def calculate_totals(worksheet, data):
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
    for num in data[1:-1]: # ignores date[1] and card[-1] payments
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


def input_time_period():
    """
    Get start and end dates from the user.
    Validates each input for correct format,
    and checks if end date is later than start date.
    Returns [start_date, end_date] list.
    """
    while True:
        print('Input the desired START date (DD/MM/YYYY):\n')
        start_date = input()

        if validate_data([start_date], [1]):
            break
        else:
            continue

    while True:
        print(f'Input the desired END date (Later than {start_date}):\n')
        end_date = input()

        try:
            first_date = datetime.strptime(start_date, '%d/%m/%Y')
            second_date = datetime.strptime(end_date, '%d/%m/%Y')

            if second_date < first_date or second_date == first_date:
                print('Please try again...')
                continue
        except:
            pass

        if validate_data([end_date], [1]):
            return [start_date, end_date]
        else:
            continue


def get_data_dict(worksheet, dates):
    """
    Takes the worksheet and start/end dates as arguments,
    compiles a data_dict for all data within dates.
    Returns time_period_data as a list of dicts.
    """
    # Start date
    start_date = dates[0]
    temp_list = start_date.split('/')
    start_year = temp_list[2]
    
    # End date
    end_date = dates[1]
    temp_list = end_date.split('/')
    end_year = temp_list[2]

    if start_year == end_year:
        desired_worksheet = SHEET.worksheet(f'{worksheet}_{start_year}')
        list_of_dicts = desired_worksheet.get_all_records()

        start_date_row = desired_worksheet.find(start_date).row
        end_date_row = desired_worksheet.find(end_date).row

        # -2 and -1 indices due to google sheets numbering convention
        time_period_data = list_of_dicts[start_date_row-2 : end_date_row-1]
        return time_period_data
    else:
        time_period_data = []

        # Start date
        desired_worksheet = SHEET.worksheet(f'{worksheet}_{start_year}')
        start_date_dicts = desired_worksheet.get_all_records()
        start_date_row = desired_worksheet.find(start_date).row

        # last day of that year
        last_row = desired_worksheet.find(start_date_dicts[-1]['Date']).row

        # data dict: start_date - 31st December
        start_date_data = start_date_dicts[start_date_row-2 : last_row-1]

        # extends list
        time_period_data.extend(start_date_data)


        # List of all the years inbetween start and end year, if any
        years = [year for year in range(int(start_year)+1, int(end_year))]

        # For loop only runs if 'years' variable has values in list 
        for year in years:
            desired_worksheet = SHEET.worksheet(f'{worksheet}_{year}')
            data_dicts = desired_worksheet.get_all_records()
            
            first_row = desired_worksheet.find(data_dicts[0]['Date']).row
            last_row = desired_worksheet.find(data_dicts[-1]['Date']).row

            date_data = data_dicts[first_row-2 : last_row-1]
            
            # extends list
            time_period_data.extend(date_data)


        # End date
        desired_worksheet = SHEET.worksheet(f'{worksheet}_{end_year}')
        end_date_dicts = desired_worksheet.get_all_records()
        end_date_row = desired_worksheet.find(end_date).row

        # first day of the year
        first_row = desired_worksheet.find(end_date_dicts[0]['Date']).row

        # data dict: 1st January - end_date
        end_date_data = end_date_dicts[first_row-2 : end_date_row-1]

        # extends list
        time_period_data.extend(end_date_data)
        return time_period_data


def input_key_values(list_of_dicts):
    """
    Takes key values from the first dict, [0], in argument,
    asks the user to input choices from those keys only.
    Returns list of labels.
    """
    # Get list of keys
    keys = [key for key in list_of_dicts[0]]

    # Ignores [0], date
    choice_headings = ''
    for heading in keys[1:-1]:
        choice_headings += heading + ','
    choice_headings += keys[-1] # Adds string without the ","

    # Change key names to lowercase, for later use
    temp = [key.lower() for key in keys]
    keys = temp
    
    while True:
        print('From the list below, select the data you want to display,')
        print('in the order in which you want to display it:')
        print('(separated by commas)\n')
        print(f'{choice_headings}\n')
        
        choices = input()

        # List of choices
        input_list = choices.split(',')
        # Change choice strings to lowercase
        temp = [choice.lower() for choice in input_list]
        input_list = temp

        labels_list = []
        try:
            for x in range(len(input_list)):
                # Ignores [0], date - checks if input is in keys list,
                # otherwise returns ValueError
                keys[1:].index(input_list[x])

                # Re-capitalize and append to list
                labels_list.append(input_list[x].capitalize())
        except ValueError as e:
            print(f'{e}, please try again...\n')
            continue
        
        break
    
    return labels_list


def concatenate_data(labels, data_dict):
    """
    Takes the chosen labels and loops through data_dict,
    groups the data from the key-value pairs (of label) into a list of lists.
    Also makes a list of all dates from the data_dict.
    Returns tuple of (dates as [] and data as [[x], [y], [z], ...])
    """
    # Puts dates in a list
    dates_list = []

    for x in range(len(data_dict)):
        dates_list.append(data_dict[x]['Date'])

    # Puts data in a list of lists: [[data1], [data2], [data3]] etc.
    data_list = []

    for item in labels:
        new_list = []
        for x in range(len(data_dict)):
            new_list.append(data_dict[x][item])
        data_list.append(new_list)
        
    return dates_list, data_list


def print_bar_chart(labels, data_tuple):
    """
    Prints a bar chart to the terminal using the plotext library.
    """
    dates_list = data_tuple[0]
    data_lists = data_tuple[1]
    
    plt.multiple_bar(dates_list, data_lists, label = labels)
    plt.title("Bar Chart")
    plt.theme('dark')
    plt.yticks([200 * i for i in range(7)])
    plt.show()
    
    
def main():
    income_data = record_data('income', 2023)
    update_worksheet('income', income_data)
    calculate_totals('income', income_data)

    expense_data = record_data('expense', 2023)
    update_worksheet('expense', expense_data)
    calculate_totals('expense', expense_data)

    time_period = input_time_period()
    time_period_data = get_data_dict('income', time_period)
    
    key_values = input_key_values(time_period_data)
    data_tuple = concatenate_data(key_values, time_period_data)
    
    print_bar_chart(key_values, data_tuple)
    # print_bar_chart(['John', 'Susan', 'Carol', 'Mario', 'Retail'], (['01/01/2022', '02/01/2022', '03/01/2022', '04/01/2022', '05/01/2022', '06/01/2022', '07/01/2022', '08/01/2022', '09/01/2022', '10/01/2022', '11/01/2022', '12/01/2022', '13/01/2022', '14/01/2022', '15/01/2022', '16/01/2022', '17/01/2022', '18/01/2022', '19/01/2022', '20/01/2022', '21/01/2022', '22/01/2022', '23/01/2022', '24/01/2022', '25/01/2022', '26/01/2022', '27/01/2022', '28/01/2022', '29/01/2022', '30/01/2022', '31/01/2022'], [[470, 664, 604, 995, 775, 927, 512, 531, 751, 609, 456, 1061, 821, 954, 1011, 396, 952, 768, 437, 354, 557, 761, 491, 570, 359, 1161, 846, 1056, 452, 883, 693], [704, 960, 626, 748, 814, 900, 852, 362, 1154, 707, 1012, 753, 822, 1018, 584, 1166, 762, 470, 1135, 638, 860, 1077, 828, 1018, 836, 598, 462, 1198, 693, 431, 393], [1042, 1000, 722, 1050, 581, 736, 461, 927, 724, 506, 369, 1075, 1193, 767, 379, 553, 1002, 438, 1001, 1173, 861, 1180, 1060, 649, 1093, 845, 1019, 678, 1184, 790, 985], [694, 1151, 439, 1070, 638, 475, 849, 778, 1057, 907, 1014, 1016, 1198, 474, 789, 602, 780, 620, 549, 899, 826, 485, 1149, 992, 812, 688, 1099, 453, 1030, 455, 523], [441, 294, 115, 137, 230, 475, 354, 206, 312, 334, 480, 362, 165, 179, 459, 167, 309, 449, 416, 497, 138, 137, 351, 415, 490, 511, 157, 365, 231, 147, 128]]))


main()