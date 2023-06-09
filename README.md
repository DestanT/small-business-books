# __Small Business Books__

## __Table of Contents__
1. [Introduction](#introduction)
2. [Goals](#goals)
3. [Flow of Logic](#flow-of-logic)
4. [Features:](#features)
    * [The Main Menu](#the-main-menu)
    * [Record Income (Option 1)](#record-income-option-1)
    * [Record Expense (Option 2)](#record-expense-option-2)
    * [View Income Charts (Option 3)](#view-income-charts-option-3)
    * [View Expense Charts (Option 4)](#view-expense-charts-option-4)
    * [The Export Data Function](#the-export-data-function)
5. [Future Features/Roadmap](#future-featuresroadmap)
6. [Testing](#testing)
7. [Challenges & Bugs](#challenges--bugs)
8. [Technologies Used](#technologies-used)
9. [Deployment](#deployment)
10. [Creating the Heroku app](#creating-the-heroku-app)
11. [Development](#development)
12. [Credits](#credits)

## __Introduction__

Small Business Books is a Python-based command-line application designed to assist small businesses in managing their financial data. The application allows users to input income and expense data, which is then updated in a Google Sheets spreadsheet via the Google Sheets API.

Using Google Sheets as a database and leveraging the power of Python, the user can input a date range to visualise their incomes and expenses, allowing them to easily track and monitor their financial performance over time.

To access the application, visit the Heroku app [**here**](https://small-business-books.herokuapp.com/). You can also view the worksheet on Google Sheets by clicking [**here**](https://docs.google.com/spreadsheets/d/1GSfZcFmG2D2p7pMAxzfF4QCuH93I7T6DGtliOl3ZAEU/edit?usp=sharing).

## __Goals__

As a small business owner, the Small Business Books application helps its user achieve the following goals:
* Input income data.
* Input expense data.
* Consolidate all income and expense data in one place (Google Sheets).
* View and compare monthly/yearly business performance based on income and expenses.
* Monitor employees' incomes and generate progress reports.
* Identify quiet periods and make necessary adjustments or offers accordingly.
* Identify overall trends in various aspects of the business's income and expenses to better plan for the future.

As the owner of the application, I am committed to:
* Adding new parameters/functions over time based on user needs.
* Ensuring the application remains bug-free by addressing user-reported issues promptly.

## __Flow of Logic__

![Flowchart](/documentation/small-business-books-flowchart.png)

## __Features:__

### __The Main Menu__

![Main Menu](/documentation/main-menu.png)\
The main menu is the first thing a user will interact with. It provides users with options to access different functionalities of the application. Key features of the main menu are:
* User input validation: The application validates the user's input and prompts for correct input if necessary. Ensuring only valid inputs are accepted.
* Selection of options: A list of options appear for users to choose from. These options allow users to choose different functionalities available in the application.

### __Record Income (Option 1)__

![Record Income Data](/documentation/enter-income-data.png)\
The Records Income feature allows users to input income data in CSV format into Google Sheets using the Google Sheets API. The features include the following functionalities:
* Dynamic heading detection: The application automatically detects headings in the first row of the spreadsheet to accommodate potential changes.
    * An example of this can be seen if the year 2021 is selected ("Carol" has been replaced with "TEST")\
    ![Test](/documentation/enter-income-data-test.png)
* Date format validation: The application validates the date format (DD/MM/YYYY).
* Data point validation: The application validates the number of data points provided by the user. It checks the number of columns of data needed and displays an error if an incorrect number of data points are given. This helps ensure data integrity.\
![Data Point Validation](/documentation/data-point-validation.png)
* Total income calculations: The application calculates the total income based on the provided data points. It updates Google Sheets accordingly, providing a convenient way to track and view in the future.

### __Record Expense (Option 2)__

The Record Expense feature is similar to the Record Expense feature and allows users to input expense data in CSV format into Google Sheets using the Google Sheets API. The functionalities of the Record Expense feature are identical to those of the Record Income feature.

### __View Income Charts (Option 3)__

![Plotext Bar Chart](/documentation/plt-bar-chart.png)\
The View Income Charts feature allows users to visualise their income data using bar charts in the terminal. The application prompts users for the following information to generate the charts:
* Start and end dates: Users are prompted to enter the start and end dates for the data range they want to visualise. The application validates the date format (DD/MM/YYYY) entered by the user. It checks for valid dates, ensuring that the end date is after the start date. Examples of wrong inputs are shown below:
    * Incorrect date format:\
    ![Date Validation](/documentation/date-validation.png)
    * Start date outside the range:\
    ![Date outside range](/documentation/date-validation-2.png)
    * End date earlier than the start date:\
    ![Invalid end date](/documentation/date-validation-3.png)
    * End date outside of range:\
    ![End date outside range](/documentation/date-validation-4.png)
* Parameter for the charts: Users are prompted to enter the parameters they want to view (selection of options are automatically displayed). The application verifies the existence of the entered parameters and prompts for correction if necessary. Users can enter the parameters in any order they wish to display them, and the application performs case-insensitive matching.\
![Parameter Validation](/documentation/name-validation.png)
* Bar chart display: The bar charts are displayed in the terminal based on the selected data range and parameters. The display format, and thus the x and y-axis labels, depends on the time-period chosen by the user:
  * Daily: If the data range is within 14 days, a daily bar chart is displayed.\
  ![Daily Chart](/documentation/daily-chart.png)
  * Weekly: If the data range is between 14 days and 14 weeks, a weekly bar chart is displayed.
    * Totals calculations are done every 7 days, starting with the first date input.\
    ![Weekly Chart](/documentation/weekly-chart.png)
  * Monthly: If the data range is over 14 weeks, a monthly bar chart is displayed.
    * Totals calculations are done for each month the data is from.\
    ![Monthly Chart](/documentation/monthly-chart.png)

### __View Expense Charts (Option 4)__

The View Expense Charts feature is identical to the View Income Charts feature. With the exception, of course, of viewing expense data instead. Functionalities are identical.

### __The Export Data Function__

![Export Data Function](/documentation/export-data.png)\
The Export Data Function allows users to export the charted data to a separate Sheet within the same Spreadsheet in Google Sheets. Here's how it works:
* Current date and time: The application uses the "datetime" library to retrieve the current date and time. This information is added as a form of timestamp for the exported data.\
![Google Sheets Export](/documentation/google-sheets-export.png)
* Finding the first available row: The application identifies the first available row within the destination Sheet where the data is appended. This ensures that the exported data does not overwrite any existing data.
* Handling large export requests: In case of larger export requests that might exceed the quota limitations of the Google Sheets API, a delay timer is set. This delay ensures that the application adheres to the API limitations and avoids any errors/disruptions during the export process.\
![Time Delay](/documentation/export-data-timer.png)

## __Future Features/Roadmap__

* Function to add and remove staff members from Google Sheets: This would allow users to add and remove staff members and other parameters as the changes arise and are needed, without the need to directly interact with Google Sheets itself.
* Split expenses into proper groups: Instead of having all utilities categorized under a single group, for example. This feature would aim to enhance the expense tracking feature and would allow users to make smarter more concise decisions for their business.
* View line graphs and scatter diagrams: In addition to the existing bar chart functionality, this feature would enable users to visualise their income and expense data from "another angle". Trends, patterns, and correlations can be easier to spot, for some, using different types of graph visualisation.
* View and review previously exported data: The application currently allows users to export data between two dates, but there is no built-in functionality to easily review the exported data. Adding a feature to utilise the timestamp from previously stored data and generate charts for reviewing the data would enhance the user experience.
* Improved user experience: optimising and reworking certain functions (for example, the export data function) to enhance the application's overall performance and reduce wait times.
* Dynamic Google Sheets creation: Implementation of the function to automatically create new Google Sheets within the Spreadsheet as needed. Currently, the application is limited to the existing Sheets and the user would have to manually intervene from Google Sheets to create new Sheets.

## __Testing__

### __Pylint__

To ensure code quality and coding standards, the Python code in "run.py" was tested using the [**Pylint**](https://pypi.org/project/pylint/) tool. The latest iteration of the project scored a 9.32/10. During the testing process no critical issues were found and most minor issues such as indentations were addressed, improving the overall code quality. Here are a few notable ones that remained:
* run.py:244:0: R0914: Too many local variables (22/15) (too-many-locals)
* run.py:541:0: R0914: Too many local variables (19/15) (too-many-locals)
* run.py:725:0: R0915: Too many statements (57/50) (too-many-statements)

The above were ignored as they were not considered fundamentally bad for the overall performance of the application. Though, future updates will involve refactoring the code by implementing smaller functions to address these concerns.

**One particular warning was also observed:**
* run.py:572:8: W0106: Expression "[month_year_list.append(month_year) for month_year in temp_list if month_year not in month_year_list]" is assigned to nothing (expression-not-assigned)

After several iterations of changing the code to try and satisfy both Pylint and the overall functionality, failed, this was ultimately kept as is. Having also not found anything alarming [online](https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/expression-not-assigned.html) and message boards that suggested this was a serious fault, it was also, ultimately, ignored. Please consider letting me know if you think was a mistake on my part, and please condiser letting me know how you would have tackled this part of the code.

### __Process__

This section aims to provide a comprehensive guide for testing the application. Feel free to deviate from it as necessary.

__The Main Menu__

| Test | Expected Outcome(s) |
| :--- | :--- |
| Click “Run Program” | Application starts and the main menu is displayed |
| Enter an incorrect input (a string) | Throws an error and prompts a re-try |
| Enter an incorrect input (integer) | Throws an error and prompts a re-try |
| Enter an incorrect input (a “space”) | Throws an error and prompts a re-try |
| Enter “1” | Starts the “Record Income” function |
| Enter “2” | Starts the “Record Expense” function |
| Enter “3” | Starts the “View Income Charts” function |
| Enter “4” | Starts the “View Expense Charts” function |

__The Record Income Function__

| Test | Expected Outcome(s) |
| :--- | :--- |
| Input a year not in the list | Throws an error and prompts a re-try |
| Input a valid year | Application continues to the next question |
|||
| Enter date in the wrong format | Throws an error and prompts a re-try |
| Enter invalid date (eg 30/02) | Throws an error and prompts a re-try |
| Enter an incorrect input (a “space”) | Throws an error and prompts a re-try |
| Enter **correct** date, followed by a string | Throws an error and prompts a re-try |
| Enter **correct** date, followed by a not enough data points | Throws an error, gives feedback and prompts a re-try |
| Enter **correct** date, followed by a too many data points | Throws an error, gives feedback and prompts a re-try |
| Enter **correct** date, followed **correct** number of data points | Updates corresponding worksheet in Google Sheets |

__The Record Expense Function__

Testing process for this function is identical to the Record Income function

__The View Income Charts Function__

| Test | Expected Outcome(s) |
| :--- | :--- |
| Input date before 01/01/2021 | Throws an error and prompts a re-try |
| Input date after 30/12/2023 | Throws an error and prompts a re-try |
| Input date within valid range | Application continues to the next question |
|||
| Input date before selected start date | Throws an error and prompts a re-try |
| Input same date as the selected start date | Throws an error and prompts a re-try |
| Input date after 31/12/2023 | Throws an error and prompts a re-try |
| Input a valid date after selected start date and on or before 31/12/2023 | Application continues to the next question |
|||
| Input an invalid selection, not on the list | Throws an error and prompts a re-try |
| Input valid selection (case-sensitive) | Application shows bar chart for chosen data |
| Input valid selection (case-insensitive) | Application shows bar chart for chosen data |
| Input valid selection (repeated selection) | Application shows bar chart with any repeated data present |
| Input valid selection (in any order you wish) | Application shows bar chart with the data in the given order |
|||
| Choose (M)enu | Takes user back to the main menu |
| Choose (E)xport | Timestamps data and exports it to Google Sheets, then takes the user back to the main menu |
| Choose any other input | Throws an error and prompts a re-try |

__The View Expense Charts Function__

Testing process for this function is identical to the Record Income function

## __Challenges & Bugs__

### __Challenges__

During the development of this project, several challenges were encountered:
* Non-integer data in Google Sheets: To address this issue the Sheets in the Spreadsheet had to be manually pre-populated with "0"s. In the future, a more elegant solution; within the function itself, will be the preferred route to take when working with Google Sheets APIs again.
* Visualisation with Plotext: When handling larger datasets, the "plotext" library struggled to display the data in a neat and useful fashion. To overcome this, two steps were taken:
  1. The data was grouped into weekly and monthly bar charts, allowing for a clearer representation of the data.
  2. The given terminal size for Heroku of 80 x 24 was increased to 120 x 48, providing more space for displaying charts.
        * Although, this still didn't produce the results as seen in a normal terminal.
* Working with Plotext in general: the library felt very limited and clunky to work with. Examples of this include, but aren't limited to:
    * Label placements - could not be changed and mostly got in the way of data.
    * Having labels per bar - for a more accurate representation of the value of each data point, was not possible.
* Designing the function to group the weekly/monthly totals: This proved challenging, especially for someone new to Python. However, through persistence, trial and error, the task was accomplished.
* Google Sheets API usage limits: Designing functions for the application to stay within Google API usage limits of "60 requests, per minute, per user" posed difficulties. Depending on the size of the data requested and then exported, this usage limit was sometimes insufficient.
  * A time delay was implemented: For larger data sets a time delay was introduced to ensure compliance with the usage limits. Initially, an exact delay of 60 seconds every 60(ish) requests was used for efficiency. However, this occasionally still resulted in "429: Too many requests HTTP status code response" errors. To ensure the smooth running of the application, a less efficient, longer time delay was tested and thus, chosen.

### __Fixed Bugs__

During the development of the project, and among many smaller bugs that were identified and fixed, here are a few notable ones:
Among many fixed bugs throughout the project, these are a few notable ones:
* Non-existent years: Previously, when prompted, the user could input a year that did not yet exist. This caused the application to encounter errors and stop functioning. This bug was fixed by implementing proper validation after said prompts to ensure the selected year is valid/exists before continuing operations.
* Exceeding the Google Sheets API usage quota: Users can select a long date range, which more often than not meant exceeding the Google Sheets API quota of "60 requests, per minute, per user". This resulted in an error and ultimately the proper function of the application. A time delay was implemented to delay the time between the requests made and thus stay within the API usage limits. Although this made the application slower performance-wise, it prevented errors caused by exceeding the quota.

### __Unfixed Bugs__

To the best of my knowledge, no unresolved bugs remain in the current version of the application. All identified bugs were addressed and fixed during the development process.

## __Technologies Used__

### __Languages__

* Python 3.11.1

### __Libraries__

* **Datetime**: Primarily used for date format validation and timestamps
* **Math**: Used for basic mathematical operations 
* **OS**: Used for clearing the terminal for a better user experience
* **Time**: Used to create the delays between Google Sheets API requests
* **Plotext**: Used to visualise data as bar charts
* **GSpread**: Used to interact with Google Sheets via the Google Sheets API

### __Tools__

* [**Heroku**](https://www.heroku.com/) - Used to house the in-browser app
* [**Lucid Charts**](https://www.lucidchart.com/) - Used to create the flow chart diagram

## __Deployment__

The project was deployed on GitHub pages from the 'Main Branch Source Code' using the following steps:
* 'git add .', 'git commit" and 'git push' commands were issued one final time when the project was ready and finished.
* On Github the repository for the project was selected.
* Click the 'Settings' tab.
* On the left; select 'Pages'.
* From here; select the source as 'Main Branch'.
* Click 'Save'.

GitHub may take a few minutes to deploy the website so be patient.

You can view the application on Heroku by clicking [**here**](https://small-business-books.herokuapp.com/).

Click [**here**](https://docs.google.com/spreadsheets/d/1GSfZcFmG2D2p7pMAxzfF4QCuH93I7T6DGtliOl3ZAEU/edit?usp=sharing) to view the worksheet.

## __Creating the Heroku app__

Before creating the Heroku app:
1. Make sure you have a file named “requirements.txt” in your main project folder.
2. Open the command line and navigate to your project folder.
3. Run the command “pip3 freeze > requirements.txt”.
    * This will create a list of dependencies used in the project for Heroku to set up the environment later.
4. Push these latest changes, including the requirements.txt file, to your GitHub repository (or any other preferred Git service). 

Now, you can proceed with creating the Heroku app:
1. Sign in to your Heroku account (if you don't already have one, create a free account on [Heroku](https://www.heroku.com/) first).
2. Once logged in, click on the "Create new app" button on your Heroku dashboard and follow the subsequent steps.
3. From within your newly created app, click the “Settings” tab.
4. Scroll down to the section labeled “Config Vars” and click on “Reveal Config Vars”.
5. In the “Key” field enter “CREDS”.
6. In the “Value” field copy and paste the entire contents of the creds.json file from your project.
    * This will securely provide the necessary credentials to access your Google Sheets API.
7. Add another Key/Value of “PORT” and “8000” respectively.
8. Scroll down to the section labeled “Buildpacks” and click “Add buildpack”.
9. Add Python and NodeJS and make sure they are shown in that order.
10. Navigate to the “Deploy” tab at the top of the page.
11. Choose your preferred deployment method (GitHub, for example) and connect it to your app.
12. Search for the repository name in the dropdown menu and select it.
13. Click “Connect”.
14. Then, either select “Enable Automatic Deploys” or “Deploy Branch”; the difference is that one automatically deploys the app every time a change is pushed to GitHub and the other needs to be redeployed manually every time.
15. You should now have a working Heroku app on your dashboard.

## __Development__

If you would like to contribute to this project, please follow the following steps:

As the project uses a creds.json file for sensitive API keys, you would first need to: 
1. Click on [**this**](https://docs.google.com/spreadsheets/d/1GSfZcFmG2D2p7pMAxzfF4QCuH93I7T6DGtliOl3ZAEU/edit?usp=sharing) link to view and save a copy of the spreadsheet to your Google Sheets account.
2. Create your own project from the [**Google Clouds Platform**](https://console.cloud.google.com/).
3. Select the project and enable both Google Sheets and Google Drive APIs from "APIs & Services" from the side menu.
4. Generate Google Drive API credentials, answering the questions as follows:
    * Which API are you using? - Google Drive API.
    * Where will you be calling the API from? - Web server (eg. node.js).
    * What data will you be accessing? - Application data.
    * Are you planning on using this API with App Engine or Compute Engine? - No, I'm not using them.
5. Once the form has been filled out as explained above, click the "What credentials do I need?" button.
6. On the next page fill out the form as follows:
    * Service account name? - *You can name this anything you want*.
    * Role? - Editor.
    * Key type? - JSON.
7. Click "Continue", which will prompt a download of the credentials file to your computer.
    * Rename this file to "creds.json"
8. Drag and drop the creds.json file to your main project folder.
    * **Very important**: Add "creds.json" to your .gitignore file
9. On the Google Spreadsheet click "Share" and add the email within the creds.json file as an "Editor"
    * Untick "Notify people"

Then from GitHub:
1. Create a separate branch for your development work
2. Make any necessary modifications and improvements to the project on your branch.
3. Create a pull request with a clear and detailed description of the changes you have made.
4. I will review your changes and provide feedback if needed.
5. If everything looks good, I will merge the changes into the main branch of the project.

If you wish to use any parts of the project for your project, you are welcome to do so. However, please give credit to me by linking my GitHub profile.

Thank you for your interest in the project, and I look forward to any contributions or acknowledgments!

## __Credits__ 

### __Content__

* Inspirations for the project were taken from the "Love Sandwiches" project by Code Institute, any re-used code was credited in the run.py file
* [Python Documentation](https://docs.python.org/3/contents.html)
* [Datetime Documentation](https://docs.python.org/3/library/datetime.html)
* [Gspread Documentation](https://docs.gspread.org/en/latest/index.html)
* [Plotext Documentation](https://github.com/piccolomo/plotext/blob/master/README.md)
* [W3Schools](https://www.w3schools.com/) - general enquiries/syntax
* [GeekForGeeks](https://www.geeksforgeeks.org/python-programming-language/?ref=shm) - general enquiries/syntax
* [Stack Overflow](https://stackoverflow.com/) - general enquiries/syntax