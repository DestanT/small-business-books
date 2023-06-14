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
* Identify quiet periods and make necessary adjusments or offers accordingly.
* Identify overall trends in various aspects of the business's income and expenses to better plan for the future.

As the owner of the application, I am committed to:
* Adding new parameters/functions over time based on user needs.
* Ensuring the application remains bug-free by addressing user-reported issues promptly.

## Flow of Logic
![Flowchart](/documentation/small-business-books-flowchart.png)

## Features:
### The Main Menu
Upon launching the application, the user is presented with the main menu. The application performs the following tasks:
* Validates user input and prompts for correct input if necessary.
* Provides options for different functionalities based on user selection.

### Record Income (Option 1)
The Records Income feature allows users to input income data in CSV format into Google Sheets using the Google Sheets API. The features includes the following functionalities:
* Dynamically detects the headings in the first row of the spreadsheet to accommodate potential changes.
* Validates the date format (DD/MM/YYYY).
* Validates the number of data points provided and displays an error if incorrect.
* Calculates the total income and updates the Google Sheets accordingly.

### Record Expense (Option 2)
Similar to the Record Income feature, the Record Expense feature enables users to input expense data in CSV format into Google Sheets using the Google Sheets API. The functionalities are identical.

### View Charts (Option 3)
The View Charts feature allows users to visualise their data using bar charts in the terminal. The application prompts users for the following information:
* Start and end dates for the data range:
  * Validates the date format (DD/MM/YYYY)
  * Checks for valid dates, ensuring the end date is after the start date.
* Parameters to be displayed in the bar chart (for example, staff members' names):
  * Verifies the existence of the entered parameters in the spreadsheet and prompts for correction if necessary.
  * Allows users to choose the order in which to display data, by entering parameters in any order.
  * Performs case-ins.
* Bar charts will display as follows:
  * Daily: for data range between 14 days.
  * Weekly: for data range between 14 weeks.
  * Monthly: for data range over 14 weeks.
  * All "Totals" calculations are done accordingly.

### The Export Function
Once the user is presented with the chart of their chosen time period and parameters, the user has the choice to export this data to a separate Sheet within the same Spreadsheet in Google Sheets. Every export:
* uses the datetime library to add the current date and time to the Sheet
* finds the first available row within the sheet and appends the data to the new row onwards

## Future Features/Roadmap

* Function to add and remove staff members from Google Sheets
* Split expenses up into their proper groups instead of having all bills under just "bills" for example
* Having an option to view line graphs and scatter diagrams
*

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
| Clicking “Run Program” | Application starts and the main menu is displayed | &#9745; |
| Entering an incorrect input (a string) | Throws an error and prompts user to re-try | &#9745; |
| Entering an incorrect input (integers) | Throws an error and prompts user to re-try | &#9745; |
| Entering an incorrect input (a “space”) | Throws an error and prompts user to re-try | &#9745; |
| Entering “1” | Starts the “Record Income” function | &#9745; |
| Entering “2” | Starts the “Record Expense” function | &#9745; |
| Entering “3” | Starts the “View Charts” function | &#9745; |

__The Record Income Function__
| Test | Expected Outcome(s) | Outcome |
| :--- | :--- | :---: |
| Inputting a year not in the list | Throws an error and prompts user to re-try | &#9745; |
| Inputting a valid year | Application continues to next question | &#9745; |
| Entering an incorrect input (integers) | Throws an error and prompts user to re-try | &#9745; |
| Entering an incorrect input (a “space”) | Throws an error and prompts user to re-try | &#9745; |
| Entering “1” | Starts the “Record Income” function | &#9745; |
| Entering “2” | Starts the “Record Expense” function | &#9745; |
| Entering “3” | Starts the “View Charts” function | &#9745; |

__The Record Expense Function__
| Test | Expected Outcome(s) | Outcome |
| :--- | :--- | :---: |
| Clicking “Run Program” | Application starts and the main menu is displayed | &#9745; |
| Entering an incorrect input (a string) | Throws an error and prompts user to re-try | &#9745; |
| Entering an incorrect input (integers) | Throws an error and prompts user to re-try | &#9745; |
| Entering an incorrect input (a “space”) | Throws an error and prompts user to re-try | &#9745; |
| Entering “1” | Starts the “Record Income” function | &#9745; |
| Entering “2” | Starts the “Record Expense” function | &#9745; |
| Entering “3” | Starts the “View Charts” function | &#9745; |

__The View Charts Function__
| Test | Expected Outcome(s) | Outcome |
| :--- | :--- | :---: |
| Clicking “Run Program” | Application starts and the main menu is displayed | &#9745; |
| Entering an incorrect input (a string) | Throws an error and prompts user to re-try | &#9745; |
| Entering an incorrect input (integers) | Throws an error and prompts user to re-try | &#9745; |
| Entering an incorrect input (a “space”) | Throws an error and prompts user to re-try | &#9745; |
| Entering “1” | Starts the “Record Income” function | &#9745; |
| Entering “2” | Starts the “Record Expense” function | &#9745; |
| Entering “3” | Starts the “View Charts” function | &#9745; |

## __Challenges & Bugs__

### __Challenges__

Some of the more challenging parts of this project were working with the plotext library; in particular the fact that when plotext had too much data to display, it wouldn’t display it in the pretty fashion that would be expected for a user to find it useful.

So it was more useful to clump the data in chunks of 14 points, for daily display; 14 points for a weekly display and everything else to be clumped into a monthly view of the data.

This in turn meant designing the functions to calculate these chunks. Being the first time working with Python, it was challenging to set up the functions to do what was a simple task in mind.

Another struggle was designing the application to stay within Google Sheets API usage limits of "60 requests, per minute, per user, per project". This meant ensuring effieciency when requesting data and making changes to the document.

### __Fixed Bugs__
* users could input invalid years...

### __Unfixed Bugs__


## Technologies Used
* Python 3.11
* Heroku

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

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Development
Should anyone wish to add to the project, please feel free to develop it on a separate branch; then create a pull request and I will review and merge it. Thank you!

Should anyone wish to copy and paste the project - you are also welcome to - please remember to give me some credit!

## Credits 

### __Content__

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

* year selection limited to 2021, 2022, 2023


### IMAGES IN FEATURES
### TABLE OF INSTRUCTUIONS ON HOW TO TEST - change tense
### TECHNOLOGIES - include libraries + justification ++ lucid charts ++ break down to languages and libraries and tools etc
development - where to add the creds.json file etc
think about more user friendly - more concise error messages
line 171 dont use bare except