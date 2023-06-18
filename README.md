# Small Business Books

## Table of Contents
1. [Introduction](#introduction)
2. [Goals](#goals)
3. [Flow of Logic](#flow-of-logic)
4. [Features:](#features)
    1. [The Main Menu](#the-main-menu)
    2. [Record Income (Option 1)](#record-income-(option-1))
    3. [Record Expense (Option 2)](#record-expense-(option-2))
    4. [View Charts (Option 3)](#view-charts-(option-3))
    5. [The Export Function](#the-export-function)
5. [Future Features/Roadmap](#future-featuresroadmap)
6. [Testing](#testing)
    1. [Lighthouse Tests](#lighthouse-tests)
    2. [Validator Testing](#validator-testing)
    3. [Process](#process)
7. [Challenges & Bugs](#challenges--bugs)
    1. [Challenges](#challenges)
    2. [Fixed Bugs](#fixed-bugs)
    3. [Unfixed Bugs](#unfixed-bugs)
8. [Technologies Used](#technologies-used)
9. [Deployment](#deployment)
10. [Creating the Heroku app](#creating-the-heroku-app)
11. [Development](#development)
12. [Credits](#credits)
    1. [Content](#content)

## Introduction
Small Business Books is a Python-based command-line application designed to assist small businesses in managing their financial data. The application allows users to input income and expense data, which is then updated in a Google Sheets spreadsheet via the Google Sheets API.

Using Google Sheets as a database and leveraging the power of Python, the user can input a date range to visualise their incomes and expenses, allowing them to easily track and monitor their financial performance over time.

To access the application, visit the Heroku app [**here**](https://small-business-books.herokuapp.com/). You can also view the worksheet on Google Sheets by clicking [**here**](https://docs.google.com/spreadsheets/d/1GSfZcFmG2D2p7pMAxzfF4QCuH93I7T6DGtliOl3ZAEU/edit?usp=sharing).

## Goals
As a small business owner, the Small Business Books application helps me achieve the following goals:
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

## Flow of Logic
![Flowchart](/documentation/small-business-books-flowchart.png)

## Features:
### The Main Menu
The main menu is the first thing a user will interact with. It provides users with options to access different functionalities of the application. Key features of the main menu are:
* User input validation: The application validates the user's input and prompts for correct input if necessary. Ensuring only valid inputs are accepted.
* Selection of options: A list of options appear for users to choose from. These options allow users to choose different functionalities available in the application.

### Record Income (Option 1)
The Records Income feature allows users to input income data in CSV format into Google Sheets using the Google Sheets API. The features include the following functionalities:
* Dynamic heading detection: The application automatically detects headings in the first row of the spreadsheet to accommodate potential changes.
* Date format validation: The application validates the date format (DD/MM/YYYY).
* Data point validation: The application validates the number of data points provided by the user. It checks the number of columns of data needed and displays an error if an incorrect number of data points are given. This helps ensure data integrity.
* Total income calculations: The application calculates the total income based on the provided data points. It updates Google Sheets accordingly, providing a convenient way to track and view in the future.

### Record Expense (Option 2)
The Record Expense feature is similar to the Record Expense feature and allows users to input expense data in CSV format into Google Sheets using the Google Sheets API. The functionalities of the Record Expense feature are identical to those of the Record Income feature.

### View Income Charts (Option 3)
The View Income Charts feature allows users to visualise their income data using bar charts in the terminal. The application prompts users for the following information to generate the charts:
* Start and end dates: Users are prompted to enter the start and end dates for the data range they want to visualise. The application validates the date format (DD/MM/YYYY) entered by the user. It checks for valid dates, ensuring that the end date is after the start date.
* Parameter for the charts: Users are prompted to enter the parameters they want to view (selection of options are automatically displayed). The application verifies the existence of the entered parameters and prompts for correction if necessary. Users can enter the parameters in any order they wish to display them, and the application performs case-insensitive matching.
* Bar chart display: The bar charts are displayed in the terminal based on the selected data range and parameters. The display format, and thus the x and y-axis labels, depends on the time-period length chosen by the user:
  * Daily: If the data range is within 14 days, a daily bar chart is displayed.
  * Weekly: If the data range is between 14 days and 14 weeks, a weekly bar chart is displayed.
    * Totals calculations are done every 7 days, starting with the first date input.
  * Monthly: If the data range is over 14 weeks, a monthly bar chart is displayed.
    * Totals calculations are done for each month the data is from.

### View Expense Charts (Option 4)
The View Expense Charts feature is identical to the View Income Charts feature. With the exception, of course, of viewing expense data instead. Functionalities are identical.

### The Export Data Function
The Export Data Function allows users to export the charted data to a separate Sheet within the same Spreadsheet in Google Sheets. Here's how it works:
* Current date and time: The application uses the "datetime" library to retrieve the current date and time. This information is added as a form of timestamp for the exported data.
* Finding the first available row: The application identifies the first available row within the destination Sheet where the data is appended. This ensures that the exported data does not overwrite any existing data.
* Handling large export requests: In case of larger export requests that might exceed the quota limitations of the Google Sheets API, a delay timer is set. This delay ensures that the application adheres to the API limitations and avoids any errors/disruptions during the export process.

## Future Features/Roadmap
* Function to add and remove staff members from Google Sheets: This would allow users to add and remove staff members and other parameters as the changes arise and are needed, without the need to directly interact with Google Sheets itself.
* Split expenses into proper groups: Instead of having all utilities categorized under a single group, for example. This feature would aim to enhance the expense tracking feature and would allow users to make smarter more concise decisions for their business.
* View line graphs and scatter diagrams: In addition to the existing bar chart functionality, this feature would enable users to visualise their income and expense data from "another angle". Trends, patterns, and correlations can be easier to spot, for some, using different types of graph visualisation.
* View and review previously exported data: The application currently allows users to export data between two dates, but there is no built-in functionality to easily review the exported data. Adding a feature to utilise the timestamp from previously stored data and generate charts for reviewing the data would enhance the user experience.
* Improved user experience: optimising and reworking certain functions (for example, the export data function) to enhance the application's overall performance and reduce wait times.
* Dynamic Google Sheets creation: Implementation of the function to automatically create new Google Sheets within the Spreadsheet as needed. Currently, the application is limited to the existing Sheets and the user would have to manually intervene from Google Sheets to create new Sheets.

## Testing
### __Lighthouse Tests__
* Desktop:\
![Lighthouse Test Desktop](/documentation/lighthouse-desktop.png)
* Mobile:\
![Lighthouse Test Mobile](/documentation/lighthouse-mobile.png)

### __Validator Testing__
- HTML - No errors or warnings to show. Link to report [here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdestant.github.io%2Fblackjack-3-minute-challenge%2F).
- CSS - No errors found. Link to report [here](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fdestant.github.io%2Fblackjack-3-minute-challenge%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en).
- JavaScript - JSHint: No errors found. 
  * Configurations used:\
  ![JSHint Configurations](/documentation/jshint-configuration.png)
  * Metrics:\
  ![JSHint Metrics](/documentation/jshint-metrics.png)


### __Process__

__The Main Menu__
| Test | Expected Outcome(s) | Outcome |
| :--- | :--- | :---: |
| Click “Run Program” | Application starts and the main menu is displayed | &#9745; |
| Enter an incorrect input (a string) | Throws an error and prompts a re-try | &#9745; |
| Enter an incorrect input (integer) | Throws an error and prompts a re-try | &#9745; |
| Enter an incorrect input (a “space”) | Throws an error and prompts a re-try | &#9745; |
| Enter “1” | Starts the “Record Income” function | &#9745; |
| Enter “2” | Starts the “Record Expense” function | &#9745; |
| Enter “3” | Starts the “View Income Charts” function | &#9745; |
| Enter “4” | Starts the “View Expense Charts” function | &#9745; |


__The Record Income Function__
| Test | Expected Outcome(s) | Outcome |
| :--- | :--- | :---: |
| Input a year not in the list | Throws an error and prompts a re-try | &#9745; |
| Input a valid year | Application continues to the next question | &#9745; |
| Entering an incorrect input (integers) | Throws an error and prompts a re-try | &#9745; |
| Entering an incorrect input (a “space”) | Throws an error and prompts a re-try | &#9745; |
| Enter “1” | Starts the “Record Income” function | &#9745; |
| Entering “2” | Starts the “Record Expense” function | &#9745; |
| Entering “3” | Starts the “View Charts” function | &#9745; |

__The Record Expense Function__
| Test | Expected Outcome(s) | Outcome |
| :--- | :--- | :---: |
| Clicking “Run Program” | Application starts and the main menu is displayed | &#9745; |
| Entering an incorrect input (a string) | Throws an error and prompts the user to re-try | &#9745; |
| Entering an incorrect input (integers) | Throws an error and prompts the user to re-try | &#9745; |
| Entering an incorrect input (a “space”) | Throws an error and prompts the user to re-try | &#9745; |
| Entering “1” | Starts the “Record Income” function | &#9745; |
| Entering “2” | Starts the “Record Expense” function | &#9745; |
| Entering “3” | Starts the “View Charts” function | &#9745; |

__The View Income Charts Function__
| Test | Expected Outcome(s) | Outcome |
| :--- | :--- | :---: |
| Clicking “Run Program” | Application starts and the main menu is displayed | &#9745; |
| Entering an incorrect input (a string) | Throws an error and prompts the user to re-try | &#9745; |
| Entering an incorrect input (integers) | Throws an error and prompts the user to re-try | &#9745; |
| Entering an incorrect input (a “space”) | Throws an error and prompts the user to re-try | &#9745; |
| Entering “1” | Starts the “Record Income” function | &#9745; |
| Entering “2” | Starts the “Record Expense” function | &#9745; |
| Entering “3” | Starts the “View Charts” function | &#9745; |

__The View Expense Charts Function__
| Test | Expected Outcome(s) | Outcome |
| :— | :— | :—: |
| Clicking “Run Program” | Application starts and the main menu is displayed | &#9745; |
| Entering an incorrect input (a string) | Throws an error and prompts user to re-try | &#9745; |
| Entering an incorrect input (integers) | Throws an error and prompts user to re-try | &#9745; |
| Entering an incorrect input (a “space”) | Throws an error and prompts user to re-try | &#9745; |
| Entering “1” | Starts the “Record Income” function | &#9745; |
| Entering “2” | Starts the “Record Expense” function | &#9745; |
| Entering “3” | Starts the “View Charts” function | &#9745; |

## __Challenges & Bugs__

### __Challenges__
During the development of this project, several challenges were encountered:
* Non-integer data in Google Sheets: To address this issue the Sheets in the Spreadsheet had to be manually pre-populated with "0"s. In the future, a more elegant solution; within the function itself, will be the preferred route to take when working with Google Sheets APIs again.
* Visualisation with Plotext: When handling larger datasets, the "plotext" library struggled to display the data in a neat and useful fashion. To overcome this, two steps were taken:
  1. The data was grouped into weekly and monthly bar charts, allowing for a clearer representation of the data.
  2. The given terminal size for Heroku of 80 x 24 was increased to 160 x 48, providing more space for displaying charts.
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

## Technologies Used
### Languages
* Python 3.11.1

### Libraries
* **GSpread**: Used to interact with Google Sheets via the Google Sheets API
* **Datetime**: Primarily used for date format validation and timestamps
* **Plotext**: Used to visualise data as bar charts
* **Math**: Used for basic mathematical operations 
* **OS**: Used for clearing the terminal for a better user experience
* **Time**: Used to create the delays between Google Sheets API requests

### Tools
* [Heroku](https://www.heroku.com/)
* [Lucid Charts](https://www.lucidchart.com/) 

## Deployment
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

## Creating the Heroku app

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

## Development
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

## Credits 
### __Content__
* Inspirations for the project were taken from the "Love Sandwiches" project by Code Institute, any re-used code was credited in the run.py file
* [Python Documentation](https://docs.python.org/3/contents.html)
* [Datetime Documentation](https://docs.python.org/3/library/datetime.html)
* [Gspread Documentation](https://docs.gspread.org/en/latest/index.html)
* [Plotext Documentation](https://github.com/piccolomo/plotext/blob/master/README.md)



### IMAGES IN FEATURES
### TABLE OF INSTRUCTUIONS ON HOW TO TEST - change tense
### TECHNOLOGIES - include libraries + justification ++ lucid charts ++ break down to languages and libraries and tools etc
think about more user friendly - more concise error messages
line 171 dont use bare except
Date selection bug when viewing charts