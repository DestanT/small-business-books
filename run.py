import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import plotext as plt
import math

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


def print_daily_chart(labels, data_tuple):
    """
    Prints daily plotext bar chart to the terminal
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
    plt.multiple_bar(dates_list, data_lists, label = labels)
    plt.title("Bar Chart")
    plt.theme('dark')
    plt.yticks([200 * i for i in range(yticks_range)])
    plt.show()


def print_weekly_chart(labels, data_tuple):
    """
    Prints weekly plotext bar chart to the terminal
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
            weekly_total.append(sum(separated_data_list[(y * 7) : (y * 7 + 7)]))
        
        totals_data_lists.append(weekly_total)
    
    # Finds max value from all lists in data_lists
    max_value_list = []
    for i in range(len(totals_data_lists)):
        max_value = max(totals_data_lists[i])
        max_value_list.append(max_value)

    # Calculate yticks in plotext using max_value_list
    yticks_range = math.ceil((max(max_value_list) / 1000))
    
    # Plotext terminal plots
    plt.multiple_bar(week_start_date, totals_data_lists, label = labels)
    plt.title("Bar Chart")
    plt.theme('dark')
    plt.yticks([1000 * i for i in range(yticks_range)])
    plt.show()  


def print_monthly_chart(labels, data_tuple):
    """
    Prints monthly plotext bar chart to the terminal
    """
    dates_list = data_tuple[0]
    data_lists = data_tuple[1]

    temp_list = []
    # Re-format to 'datetime'
    for date in dates_list:
        datetime_format = datetime.strptime(date, '%d/%m/%Y')
        # Get month name + year
        month_year = datetime_format.strftime('%b-%y')
        temp_list.append(month_year)

    # Add unique month/years only to list, for use in plotext
    month_year_list = []
    for month_year in temp_list:
        [month_year_list.append(month_year) for month_year in temp_list if month_year not in month_year_list]

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
    plt.multiple_bar(month_year_list, totals_data_lists, label = labels)
    plt.title("Bar Chart")
    plt.theme('dark')
    plt.yticks([1000 * i for i in range(yticks_range)])
    plt.show()  
    

def print_bar_chart(labels, data_tuple):
    """
    Depending on number of dates selected by user,
    chooses to present plotext bar chart in;
    daily, weekly or monthly format.
    """
    dates_list = data_tuple[0]

    # Under 2 weeks; present daily chart
    if len(dates_list) <= 14:
        print_daily_chart(labels, data_tuple)

    # Under 14 weeks; present weekly chart
    elif len(dates_list) <= 98:
        print_weekly_chart(labels, data_tuple)

    # Everything else; present monthly chart
    else:
        print_monthly_chart(labels, data_tuple)
    
    
def main():
    # income_data = record_data('income', 2023)
    # update_worksheet('income', income_data)
    # calculate_totals('income', income_data)

    # expense_data = record_data('expense', 2023)
    # update_worksheet('expense', expense_data)
    # calculate_totals('expense', expense_data)

    # time_period = input_time_period()
    # time_period_data = get_data_dict('income', time_period)
    
    # key_values = input_key_values(time_period_data)
    # data_tuple = concatenate_data(key_values, time_period_data)
    # print(data_tuple)
    # print_bar_chart(key_values, data_tuple)
    print_bar_chart(['John', 'Susan', 'Carol', 'Mario', 'Retail'], (['01/01/2022', '02/01/2022', '03/01/2022', '04/01/2022', '05/01/2022', '06/01/2022', '07/01/2022', '08/01/2022', '09/01/2022', '10/01/2022', '11/01/2022', '12/01/2022', '13/01/2022', '14/01/2022', '15/01/2022', '16/01/2022', '17/01/2022', '18/01/2022', '19/01/2022', '20/01/2022', '21/01/2022', '22/01/2022', '23/01/2022', '24/01/2022', '25/01/2022', '26/01/2022', '27/01/2022', '28/01/2022', '29/01/2022', '30/01/2022', '31/01/2022', '01/02/2022', '02/02/2022', '03/02/2022', '04/02/2022', '05/02/2022', '06/02/2022', '07/02/2022', '08/02/2022', '09/02/2022', '10/02/2022', '11/02/2022', '12/02/2022', '13/02/2022', '14/02/2022', '15/02/2022', '16/02/2022', '17/02/2022', '18/02/2022', '19/02/2022', '20/02/2022', '21/02/2022', '22/02/2022', '23/02/2022', '24/02/2022', '25/02/2022', '26/02/2022', '27/02/2022', '28/02/2022', '01/03/2022', '02/03/2022', '03/03/2022', '04/03/2022', '05/03/2022', '06/03/2022', '07/03/2022', '08/03/2022', '09/03/2022', '10/03/2022', '11/03/2022', '12/03/2022', '13/03/2022', '14/03/2022', '15/03/2022', '16/03/2022', '17/03/2022', '18/03/2022', '19/03/2022', '20/03/2022', '21/03/2022', '22/03/2022', '23/03/2022', '24/03/2022', '25/03/2022', '26/03/2022', '27/03/2022', '28/03/2022', '29/03/2022', '30/03/2022', '31/03/2022', '01/04/2022', '02/04/2022', '03/04/2022', '04/04/2022', '05/04/2022', '06/04/2022', '07/04/2022', '08/04/2022', '09/04/2022', '10/04/2022', '11/04/2022', '12/04/2022', '13/04/2022', '14/04/2022', '15/04/2022', '16/04/2022', '17/04/2022', '18/04/2022', '19/04/2022', '20/04/2022', '21/04/2022', '22/04/2022', '23/04/2022', '24/04/2022', '25/04/2022', '26/04/2022', '27/04/2022', '28/04/2022', '29/04/2022', '30/04/2022'], [[1643, 1513, 1476, 1525, 1482, 1480, 1431, 1326, 1614, 1664, 1669, 1251, 1302, 1336, 1448, 1403, 1608, 1448, 1234, 1677, 1595, 1369, 1233, 1349, 1457, 1224, 1379, 1319, 1282, 1218, 1695, 1692, 1271, 1623, 1673, 1394, 1606, 1389, 1528, 1632, 1407, 1519, 1548, 1398, 1293, 1505, 1658, 1308, 1422, 1256, 1316, 1308, 1620, 1488, 1431, 1286, 1261, 1590, 1602, 1297, 1418, 1429, 1279, 1499, 1508, 1487, 1674, 1484, 1700, 1619, 1655, 1478, 1694, 1515, 1354, 1384, 1676, 1275, 1696, 1334, 1262, 1201, 1214, 1319, 1597, 1647, 1698, 1574, 1421, 1345, 1484, 1693, 1454, 1314, 1576, 1467, 1229, 1404, 1660, 1658, 1200, 1610, 1653, 1304, 1403, 1211, 1448, 1332, 1287, 1208, 1212, 1508, 1442, 1374, 1327, 1328, 1441, 1590, 1390, 1679], [1534, 1567, 1534, 1032, 1058, 1571, 1390, 1574, 1555, 1481, 1501, 1199, 1091, 1282, 1065, 1306, 1135, 1521, 1044, 1093, 1521, 1585, 1353, 1041, 1030, 1557, 1264, 1007, 1361, 1140, 1422, 1114, 1562, 1503, 1001, 1314, 1141, 1316, 1132, 1040, 1243, 1013, 1532, 1432, 1487, 1097, 1344, 1547, 1352, 1462, 1137, 1051, 1504, 1112, 1102, 1378, 1360, 1554, 1563, 1184, 1478, 1338, 1500, 1274, 1495, 1548, 1112, 1567, 1309, 1190, 1542, 1174, 1261, 1140, 1494, 1299, 1298, 1273, 1479, 1532, 1468, 1471, 1066, 1325, 1203, 1380, 1067, 1116, 1296, 1420, 1289, 1544, 1482, 1529, 1306, 1264, 1269, 1351, 1139, 1075, 1148, 1529, 1001, 1472, 1547, 1175, 1197, 1345, 1243, 1349, 1239, 1379, 1306, 1366, 1451, 1017, 1453, 1087, 1577, 1551], [1009, 1085, 1241, 900, 1397, 1208, 1385, 1325, 1372, 1142, 1158, 1225, 930, 1065, 1006, 1150, 1076, 1202, 1203, 1343, 1337, 1091, 1051, 918, 933, 1315, 1287, 1227, 1297, 926, 1189, 967, 967, 1180, 1058, 1314, 964, 1369, 1140, 1012, 1193, 1370, 1384, 1027, 1139, 1056, 1017, 1397, 1295, 974, 1343, 981, 1024, 1142, 953, 1300, 988, 949, 1146, 1053, 1149, 1040, 1205, 1373, 925, 1061, 1031, 1125, 1150, 958, 1114, 949, 1175, 961, 1284, 934, 1222, 1044, 1397, 1049, 1393, 1036, 1184, 1091, 1205, 1132, 1356, 1066, 962, 1308, 1301, 922, 1373, 1153, 1255, 1122, 971, 1289, 1164, 989, 1103, 938, 1213, 1202, 1053, 1313, 982, 1163, 1285, 1240, 1071, 1332, 1201, 994, 1207, 1360, 1377, 948, 1374, 1148], [1043, 1039, 1071, 1203, 1211, 1328, 1037, 701, 741, 763, 849, 912, 1208, 862, 1315, 905, 1001, 905, 731, 1195, 1285, 919, 723, 710, 1075, 969, 875, 837, 755, 1221, 1349, 1211, 1320, 739, 1343, 1324, 1147, 1146, 1339, 775, 918, 1319, 1268, 1027, 737, 1128, 804, 911, 1058, 711, 1188, 770, 756, 826, 1111, 786, 832, 1302, 892, 1252, 1164, 795, 713, 1012, 1249, 1260, 907, 957, 1184, 874, 1275, 984, 1061, 1194, 950, 766, 1017, 1049, 890, 951, 764, 1011, 1193, 778, 727, 924, 827, 1249, 767, 1089, 1285, 1091, 876, 1283, 978, 1083, 1284, 1226, 711, 841, 1196, 958, 1015, 1339, 1345, 770, 963, 1063, 921, 1257, 970, 1096, 901, 854, 1058, 791, 1289, 1090, 1003, 1136], [64, 163, 74, 113, 69, 138, 149, 71, 244, 222, 123, 193, 188, 130, 243, 185, 192, 153, 68, 247, 218, 209, 145, 69, 57, 224, 101, 194, 74, 139, 136, 57, 82, 106, 79, 179, 200, 97, 173, 195, 88, 208, 211, 94, 143, 120, 81, 81, 50, 230, 155, 51, 115, 83, 163, 120, 100, 189, 123, 182, 165, 137, 135, 70, 88, 173, 194, 194, 54, 202, 154, 88, 165, 141, 135, 187, 191, 179, 114, 243, 208, 162, 59, 243, 192, 163, 100, 179, 236, 90, 85, 186, 137, 205, 71, 241, 170, 171, 240, 155, 189, 239, 148, 204, 152, 90, 79, 55, 131, 196, 99, 236, 97, 236, 157, 240, 207, 220, 82, 141]]))


main()