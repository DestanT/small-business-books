""" Libraries used """
from datetime import datetime
import math
import os
import time
import plotext as plt
import gspread
from google.oauth2.service_account import Credentials

# Code taken from Code Institute's "Love Sandwiches" project
SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
    ]

# Code taken from Code Institute's "Love Sandwiches" project
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('small_business_books')


def record_data(worksheet, year):
    """
    Get the date and data input from the user.

    Parameters
    ----------
    worksheet (str)
    year (str)

    Returns
    ----------
    data_list (list)
    """
    headings_string = ''
    headings_list = SHEET.worksheet(f'{worksheet}_{year}').row_values(1)

    # Ignores last 2 columns: cash and total columns in "income" worksheets,
    # Or the "empty" and total columns in "expense" worksheets.
    headings_string += ','.join(headings_list[0:-2])

    # Gives user correctly lengthed example of input.
    example_print = ''
    # -3 because date index, also, not considered.
    for _ in range(len(headings_list[0:-3])):
        example_print += ',305'

    while True:
        print(f'Enter the date and {worksheet} data')
        print(f'for the year {year}, separated by commas.')
        print('Data should be in the corresponding order:\n')
        print(headings_string)
        print(f'Example: DD/MM{example_print}\n')

        data_str = input('Enter your data here:\n')

        data_list = data_str.split(',')
        # Re-add the year, previously selected, to the data list for validation
        data_list[0] += f'/{year}'

        if validate_data(data_list, headings_list[0:-2]):
            print('Data is valid!\n')
            break

    return data_list


def validate_data(data, headings):
    """
    Checks the date is in the right format,
    Checks if data entered after the date can be converted to int,
    Checks if len(data) matches len(headings),
    Raises Errors accordingly.

    Parameters
    ----------
    data (list)
    headings (list)

    Returns
    ----------
    bool: True for valid, False for invalid.
    """
    # CREDIT - datetime method:
    # https://paperbun.org/validate-date-string-format-in-python/
    try:
        # Checks date; index 0
        datetime.strptime(data[0], '%d/%m/%Y')

        # Checks if int, skips date index
        int_data = list(map(int, data[1:]))
        is_int = all(isinstance(value, int) for value in int_data)
        if is_int is False:
            raise ValueError(
                'data points must be integers'
            )

        # Compares length of data input to length of headings
        if len(data) != len(headings):
            raise ValueError(
                f'Exactly {len(headings)-1} values needed, you entered {len(data)-1}'
            )

    except ValueError as e:
        print(f'Invalid input: {e}, please try again.\n')
        return False
    except TypeError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False

    return True


def update_worksheet(worksheet, data):
    """
    Finds the date associated with data,
    and updates specified worksheet.

    Parameters
    ----------
    worksheet (str)
    data (list)
    """
    # Clears the terminal
    os.system('clear')

    date = data[0]
    date_list = date.split('/')
    year = date_list[2]

    print(f"Updating '{worksheet}_{year}' worksheet...\n")
    worksheet_to_update = SHEET.worksheet(f'{worksheet}_{year}')
    row_to_update = worksheet_to_update.find(date).row

    income_data = list(data)
    for i in range(len(income_data)):
        worksheet_to_update.update_cell(row_to_update, i + 1, income_data[i])

    print(f"'{worksheet}_{year}' worksheet updated successfully.\n")


def calculate_totals(worksheet, data):
    """
    Calculates total sums and updates specified worksheet.
    If worksheet == "income"; calculates cash value for the day.

    Parameters
    ----------
    worksheet (str)
    data (list)
    """
    date = data[0]
    date_list = date.split('/')
    year = date_list[2]

    worksheet_to_update = SHEET.worksheet(f'{worksheet}_{year}')
    row_to_update = worksheet_to_update.find(date).row
    total_column = worksheet_to_update.find('Total').col

    total = 0
    for num in data[1:-1]:  # ignores date[1] and card[-1] payments
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
    Additionally makes sure the user stays within valid date ranges.

    Returns
    ----------
    [start_date, end_date] list.
    """
    date1 = datetime.strptime('01/01/2021', '%d/%m/%Y')
    date2 = datetime.strptime('30/12/2023', '%d/%m/%Y')

    while True:
        print('Valid date range: 01/01/2021 - 30/12/2023')
        print('Input the desired START date (DD/MM/YYYY):\n')
        start_date = input()

        try:
            # Date must be later than 01/01/2021
            if date1 > datetime.strptime(start_date, '%d/%m/%Y'):
                print('Invalid date selected, please try again')
                continue

            # Date must be before 30/12/2021
            if datetime.strptime(start_date, '%d/%m/%Y') > date2:
                print('Invalid date selected, please try again')
                continue

            if validate_data([start_date], [1]):
                break

            continue

        except ValueError:
            print('Invalid date, please try again')
            continue

    # Update date2 to 31st December 2023 from 30th
    date2 = datetime.strptime('31/12/2023', '%d/%m/%Y')

    while True:
        print(f'Input the desired END date (Later than {start_date}):\n')
        end_date = input()

        try:
            # Date must be no later than 31/12/2021
            if datetime.strptime(end_date, '%d/%m/%Y') > date2:
                print('Data only valid until 31/12/2023, please try again.')
                continue

            first_date = datetime.strptime(start_date, '%d/%m/%Y')
            second_date = datetime.strptime(end_date, '%d/%m/%Y')

            if second_date < first_date or second_date == first_date:
                raise ValueError

        except ValueError:
            print('Please try again')
            continue

        if validate_data([end_date], [1]):
            print(f'From {start_date} to {end_date} selected.')
            return [start_date, end_date]

        continue


def get_data_dict(worksheet, dates):
    """
    Takes the worksheet and start/end dates as arguments,
    compiles a data_dict for all data within dates.

    Parameters
    ----------
    worksheet (str)
    dates (list)

    Returns
    ----------
    time_period_data: list of dicts [{dict}, {dict2}, ...]
    """
    # Clears the terminal
    os.system('clear')

    # Start date
    start_date = dates[0]
    temp_list = start_date.split('/')
    start_year = temp_list[2]

    # End date
    end_date = dates[1]
    temp_list = end_date.split('/')
    end_year = temp_list[2]

    if start_year == end_year:
        print(f"Data between {start_date} and {end_date}")
        print(f"from '{worksheet}_{start_year}' is being compiled...")

        desired_worksheet = SHEET.worksheet(f'{worksheet}_{start_year}')
        list_of_dicts = desired_worksheet.get_all_records()

        start_date_row = desired_worksheet.find(start_date).row
        end_date_row = desired_worksheet.find(end_date).row

        # -2 and -1 indices due to google sheets numbering convention
        time_period_data = list_of_dicts[start_date_row - 2: end_date_row - 1]
        return time_period_data

    # Else:
    time_period_data = []

    # Start date - till the end of the year
    print(f"Data between {start_date} and 31/12/{start_year}")
    print(f"from '{worksheet}_{start_year}' is being compiled...")

    desired_worksheet = SHEET.worksheet(f'{worksheet}_{start_year}')
    start_date_dicts = desired_worksheet.get_all_records()
    start_date_row = desired_worksheet.find(start_date).row

    # last day of that year
    last_row = desired_worksheet.find(start_date_dicts[-1]['Date']).row

    # data dict: start_date - 31st December
    start_date_data = start_date_dicts[start_date_row - 2: last_row - 1]

    # extends list
    time_period_data.extend(start_date_data)

    # List of all the years inbetween start and end year, if any
    years = list(range(int(start_year)+1, int(end_year)))

    # For loop only runs if "years" variable has values in list
    for year in years:
        print(f"Data from '{worksheet}_{year}' is being compiled...")
        desired_worksheet = SHEET.worksheet(f'{worksheet}_{year}')
        data_dicts = desired_worksheet.get_all_records()

        first_row = desired_worksheet.find(data_dicts[0]['Date']).row
        last_row = desired_worksheet.find(data_dicts[-1]['Date']).row

        date_data = data_dicts[first_row - 2: last_row - 1]

        # extends list
        time_period_data.extend(date_data)

    # End date
    print(f"Data between 01/01/{end_year} and {end_date}")
    print(f"from '{worksheet}_{end_year}' is being compiled...")

    desired_worksheet = SHEET.worksheet(f'{worksheet}_{end_year}')
    end_date_dicts = desired_worksheet.get_all_records()
    end_date_row = desired_worksheet.find(end_date).row

    # first day of the year
    first_row = desired_worksheet.find(end_date_dicts[0]['Date']).row

    # data dict: 1st January - end_date
    end_date_data = end_date_dicts[first_row - 2: end_date_row - 1]

    # extends list
    time_period_data.extend(end_date_data)
    return time_period_data


def input_key_values(list_of_dicts):
    """
    Takes key values (headings) from the first dict, [0], in argument,
    asks the user to input choices from those keys only.

    Parameters
    ----------
    list_of_dicts: [{dict}, {dict2}, ...]

    Returns
    ----------
    labels_list (list)
    """
    # Clears the terminal
    os.system('clear')

    # Get list of keys
    keys = list(list_of_dicts[0])

    # Ignores [0], date
    choice_headings = ''
    choice_headings += ','.join(keys[1:])

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
            # Clears the terminal
            os.system('clear')

            print(f'{e}, please try again...\n')
            continue

        break

    return labels_list


def concatenate_data(labels, data_dict):
    """
    Takes the chosen labels and loops through data_dict,
    groups the data from the key-value pairs (of label) into a list of lists.
    Additionally makes a list of all dates from the data_dict.

    Parameters
    ----------
    labels (list)
    data_dict (list)

    Returns
    ----------
    Data Tuple containing:
    [0]dates_list (list)
    [1]data_list (list of lists)
    """
    # Clears the terminal
    os.system('clear')

    print('Sorting data according to parameters chosen...')

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


def print_daily_chart(labels, data_tuple):
    """
    Prints daily plotext bar chart to the terminal
    Return values used in export function.

    Parameters
    ----------
    labels (list)
    data_tuple (tuple)

    Returns
    ----------
    Data Tuple containing:
    [0]labels (list)
    [1]dates_list (list)
    [2]data_list (list of lists)
    """
    dates_list = data_tuple[0]
    data_lists = data_tuple[1]

    # Finds max value from all lists in data_lists
    max_value_list = []
    for i in range(len(data_lists)):
        max_value = max(data_lists[i])
        max_value_list.append(max_value)

    # Calculate yticks in plotext using max_value_list
    yticks_range = math.ceil((max(max_value_list) / 200))

    # Plotext terminal plots
    plt.multiple_bar(dates_list, data_lists, label=labels)
    plt.title('Daily Bar Chart')
    plt.theme('dark')
    plt.yticks([200 * i for i in range(yticks_range)])
    plt.show()

    return labels, dates_list, data_lists


def print_weekly_chart(labels, data_tuple):
    """
    Prints weekly plotext bar chart to the terminal
    Return values used in export function.

    Parameters
    ----------
    labels (list)
    data_tuple (tuple)

    Returns
    ----------
    Data Tuple containing:
    [0]labels (list)
    [1]week_start_date (list)
    [2]totals_data_lists (list of lists)
    """
    dates_list = data_tuple[0]
    data_lists = data_tuple[1]

    # New list of dates, every 7 days
    week_start_date = dates_list[0::7]

    # Number of days divided by 7 to get weeks, rounded up
    weeks = math.ceil(len(data_lists[0]) / 7)

    # This will be the "new" and summed up data_lists used for plotext
    totals_data_lists = []

    # For loop length depending on how many "key" values were chosen
    for x in range(len(data_lists)):
        separated_data_list = data_lists[x]

        weekly_total = []
        for y in range(weeks):
            weekly_total.append(sum(separated_data_list[(y * 7): (y * 7 + 7)]))

        totals_data_lists.append(weekly_total)

    # Finds max value from all lists in data_lists
    max_value_list = []
    for i in range(len(totals_data_lists)):
        max_value = max(totals_data_lists[i])
        max_value_list.append(max_value)

    # Calculate yticks in plotext using max_value_list
    yticks_range = math.ceil((max(max_value_list) / 1000))

    # Plotext terminal plots
    plt.multiple_bar(week_start_date, totals_data_lists, label=labels)
    plt.title('Weekly Bar Chart')
    plt.theme('dark')
    plt.yticks([1000 * i for i in range(yticks_range)])
    plt.show()

    return labels, week_start_date, totals_data_lists


def print_monthly_chart(labels, data_tuple):
    """
    Prints monthly plotext bar chart to the terminal
    Return values used in export function.

    Parameters
    ----------
    labels (list)
    data_tuple (tuple)

    Returns
    ----------
    Data Tuple containing:
    [0]labels (list)
    [1]month_year_list (list)
    [2]totals_data_lists (list of lists)
    """
    dates_list = data_tuple[0]
    data_lists = data_tuple[1]

    temp_list = []
    # Re-format to "datetime"
    for date in dates_list:
        datetime_format = datetime.strptime(date, '%d/%m/%Y')
        # Get month name + year
        month_year = datetime_format.strftime('%b-%y')
        temp_list.append(month_year)

    # Add unique month/years only to list, for use in plotext
    month_year_list = []
    for month_year in temp_list:
        [month_year_list.append(month_year)
        for month_year in temp_list
        if month_year not in month_year_list]

    # This will be the "new" and summed up data_lists used for plotext
    totals_data_lists = []

    # For loop length depending on how many "key" values were chosen
    for i in range(len(data_lists)):
        temp_totals = []

        for item in month_year_list:
            indices = []

            # Find indices in relation to months and data
            for index, month_year in enumerate(temp_list):
                if month_year == item:
                    indices.append(index)

            month_total = sum(data_lists[i][indices[0]: indices[-1]+1])
            temp_totals.append(month_total)

        # Get list of lists, for use in plotext
        totals_data_lists.append(temp_totals)

    # Finds max value from all lists in data_lists
    max_value_list = []
    for i in range(len(totals_data_lists)):
        max_value = max(totals_data_lists[i])
        max_value_list.append(max_value)

    # Calculate yticks in plotext using max_value_list
    yticks_range = math.ceil((max(max_value_list) / 1000))

    # Plotext terminal plots
    plt.multiple_bar(month_year_list, totals_data_lists, label=labels)
    plt.title('Monthly Bar Chart')
    plt.theme('dark')
    plt.yticks([1000 * i for i in range(yticks_range)])
    plt.show()

    return labels, month_year_list, totals_data_lists


def export_data(data_tuple):
    """
    Exports data to Google Sheets

    Parameters
    ----------
    data_tuple (tuple)
    """
    # Clears the terminal
    os.system('clear')

    print('Exporting data...')

    labels_list = data_tuple[0]
    dates_list = data_tuple[1]
    totals_lists = data_tuple[2]

    worksheet_to_update = SHEET.worksheet('exported_data')

    # Places time data in the first available row
    # to keep track of when data was exported
    todays_date = str(datetime.now())
    first_available_row = len(worksheet_to_update.get_all_values()) + 1
    worksheet_to_update.update_cell(first_available_row, 1, todays_date)
    column = 1

    # Exporting rest of the data to Google Sheets
    for x in range(len(dates_list)):
        next_available_row = len(worksheet_to_update.get_all_values()) + 1
        worksheet_to_update.update_cell(next_available_row, column, dates_list[x])

    # Time delay, for API quota limitations
    if len(dates_list) > 30:
        print('Please wait...')
        time.sleep(35)

    for y in range(len(labels_list)):
        worksheet_to_update.update_cell(first_available_row, y + 2, labels_list[y])

        for z in range(len(totals_lists[0])):
            worksheet_to_update.update_cell(first_available_row + 1 + z, y + 2, totals_lists[y][z])

        # Clears the terminal
        os.system('clear')

        # Time delay operations, for API quota limitations
        sleep_time = 15 if len(dates_list) <= 30 else 35

        # sleep_time + 5, to account for writing time on Google Sheets
        time_left = (sleep_time + 5) * (len(labels_list) - y)

        # Shows wait time, roughly
        print('Please wait...')
        print(f'roughly {time_left} seconds left..')

        time.sleep(sleep_time)
        print('Exporting data...')

    print('Complete.')


def print_bar_chart(labels, data_tuple):
    """
    Depending on length of time selected by user,
    chooses to present plotext bar chart in;
    daily, weekly or monthly format.

    Parameters
    ----------
    labels (list)
    data_tuple (tuple)
    """
    # Clears the terminal
    os.system('clear')

    # Clears memory data in plotext - reset
    plt.clear_data()

    dates_list = data_tuple[0]

    # Under 2 weeks; present daily chart
    if len(dates_list) <= 14:
        new_data = print_daily_chart(labels, data_tuple)

    # Under 14 weeks; present weekly chart
    elif len(dates_list) <= 98:
        new_data = print_weekly_chart(labels, data_tuple)

    # Everything else; present monthly chart
    else:
        new_data = print_monthly_chart(labels, data_tuple)

    while True:
        print('Please choose to (E)xport data or go back to the (M)enu')

        choice = input()

        if choice.lower() == 'e':
            export_data(new_data)
            os.system('clear')
            main()

        elif choice.lower() == 'm':
            os.system('clear')
            main()

        else:
            print('Please choose a valid option...')


def main():
    """
    Main function
    """
    print('Welcome to Small Business Books')
    while True:
        print('Please select from one of the following options:')
        print('1. Record Income')
        print('2. Record Expense')
        print('3. View Income Charts')
        print('4. View Expense Charts')

        choice = input()

        if choice == '1':
            os.system('clear')
            print('Select from one of the following years:')
            print('2021, 2022, 2023')

            while True:
                year = input()

                if year in ('2021', '2022', '2023'):
                    income_data = record_data('income', year)
                    update_worksheet('income', income_data)
                    calculate_totals('income', income_data)

                    # Clears the terminal
                    os.system('clear')
                    break

                os.system('clear')
                print('Please enter a valid choice:')
                print('2021, 2022, 2023')
                continue

        elif choice == '2':
            os.system('clear')
            print('Select from one of the following years:')
            print('2021, 2022, 2023')

            while True:
                year = input()

                if year in ('2021', '2022', '2023'):
                    expense_data = record_data('expense', year)
                    update_worksheet('expense', expense_data)
                    calculate_totals('expense', expense_data)

                    # Clears the terminal
                    os.system('clear')
                    break

                os.system('clear')
                print('Please enter a valid choice:')
                print('2021, 2022, 2023')
                continue

        elif choice == '3':
            os.system('clear')
            time_period = input_time_period()
            time_period_data = get_data_dict('income', time_period)
            key_values = input_key_values(time_period_data)
            data_tuple = concatenate_data(key_values, time_period_data)
            print_bar_chart(key_values, data_tuple)
            break

        elif choice == '4':
            os.system('clear')
            time_period = input_time_period()
            time_period_data = get_data_dict('expense', time_period)
            key_values = input_key_values(time_period_data)
            data_tuple = concatenate_data(key_values, time_period_data)
            print_bar_chart(key_values, data_tuple)
            break

        else:
            # Clears the terminal
            os.system('clear')

            print('Invalid choice...')


main()
