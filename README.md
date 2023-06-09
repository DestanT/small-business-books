# Small Business Books

## Table of Contents
1. [Introduction](#introduction)
2. [Goals](#goals)
3. [Wireframe & Planning](#wireframe--planning)
4. [Features:](#features)
    1. [First Visit](#first-visit)
    2. [The Deck Of Cards](#the-deck-of-cards)
    3. [The 'Hit', 'Split' and 'Stand' Functions](#the-hit-split-and-stand-functions)
        - [Hit](#hit)
        - [Split](#split)
        - [Stand](#stand)
    4. [The Poker Chips and Betting](#the-poker-chips-and-betting)
    5. [End Game Score Screen](#end-game-score-screen)
    6. [Animations](#animations)
    7. [Sound Effects](#sound-effects)
5. [Future Features/Roadmap](#future-featuresroadmap)
6. [Testing](#testing)
    1. [Lighthouse Tests](#lighthouse-tests)
    2. [Validator Testing](#validator-testing)
    3. [Friends and Family Testing](#friends-and-family-testing)
    4. [Process](#process)
7. [Challenges & Bugs](#challenges--bugs)
    1. [Challenges](#challenges)
    2. [Fixed Bugs](#fixed-bugs)
    3. [Unfixed Bugs](#unfixed-bugs)
8. [Technologies Used](#technologies-used)
9. [Deployment](#deployment)
10. [Development](#development)
11. [Credits](#credits)
    1. [Content](#content)
    2. [Media](#media)

## Introduction
Small Business Books is a Python-based command-line application designed to assist small businesses in managing their financial data. The application allows users to input income and expense data, which is then updated in a Google Sheets spreadsheet via the Google Sheets API.

Using Google Sheets as a database and leveraging the power of Python, the user can input a date range to visualise their incomes and expenses, allowing them to easily track and monitor their financial performance over time.

You can view the application on Heroku by clicking [**here**](https://small-business-books.herokuapp.com/).

## Goals
As a small business, I would use this application to:
* Input income data
* Input expense data
* Have all of my business' income and expense data in one place (Google Sheets, in this case)
* View all income and expense data to be able to compare how the business is doing every month/year
* View and compare employees' incomes to the business and set up progress reports to see how things could be improved
* View when the quietest times are for the business and make offers/changes according to those quiet periods
* See an overall trend in various aspects of income and expenses of the business to better plan for the future

As the owner of the application, I would:
* Apply new parameters/functions over time, by listening to the needs of the business
* Make sure the application remains bug free by listening to any problems that may have occured by the users of the application

## Wireframe & Planning

## Features:
### Main Menu
When the application is launched the user is greeted with the main menu.
* The application checks for a valid input by the user to move forward, else throws an error and asks the user to try again

### 1. Record Income
Records income data from the user's CSV input to Google Sheets via the API. The features within are:
* Checks to see what headings there are in row 1 of the excel sheet, instead of just printing pre-chosen headings. This was implemented with the future possibility of staff/parameter changes in mind. The function will work with any number of changes to this row.
* Validates the date to be in the right format (DD/MM/YYYY)
* Validates the right number of data points given and throws an error otherwise.
* Dynamic headings
* therefore dynamically
* Calculates total income and automatically updates google sheets

### 2. Record Expense
Records expense data from the user's CSV input to Google Sheets via the API. The features within are identical to the fetaures in "Record Income" as the functions used are identical (Difference in arguments within parameters only)

### 3. View Charts
The user is presented with a bar chart that makes viewing the data much more pleasant and easier to understand and get an overview over. The application achieves this by asking a series of questions to its user:

* The user is promted to enter a start date and an end date, the application:
	* checks that the format of the date is correct (DD/MM/YYYY)
	* checks that the date is valid, ie 31st February, for example would not be valid
	* checks that the end date is at least one day after the start date
* The user is promted to enter the names of the parameters they wish to view in the bar chart, the application (for example the names of their staff members):
	* checks whether or not those names/parameters are present in the excel sheets, prompts the user to re-enter if non existent parameters are entered
	* is not case sensitive, for better UX
* The application concatenates the data based on the parameters selected, so for example if only "Retail" sales and "Total" income is of interest, then only those two can be selected:
	* Also the order in which they are selected is the order in which they will be displayed - this allows the user a little more flexibility with how their data is presented to them.
* The application will:
	* Display a daily chart if data is up to 14 days long
		* displays every date in the x axis
	* Display a weekly chart if data is up to 14 weeks long
		* displays every 7th date in the x axis
		* calculations are done for every 7 days
	* And display a monthly chart is data is any longer than 14 weeks
		* displays every month-year in the x axis
		* calculations are done according to the month the data falls within
	* This was to ensure readability in the charts, although the conditions can be looked at again in the future
	

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

### __Friends and Family Testing__

The project was also tested by friends and family; using their native web browsers for responsiveness using these devices/tools:
  * Monitor 25" screen
  * Windows laptop 15" screen
  * iPhone 12 Pro Max
  * OnePlus 8
  * Samsung S22 Ultra
  * iPad Pro 12.9" screen
  * iPad Pro 11" screen
  * Chrome dev tools for various other options

### __Process__

The application was tested 
| Test | Expected Outcome(s) | Outcome |
| :--- | :--- | :---: |
| First Visit | Triggers 'Name Input' screen. | &#9745;
|||
 Clicking the name in 'Game Rules' | Triggers 'Name Input' screen. | &#9745;
|||
| `Start` button | Plays card animations, | &#9745;
||deals 2 cards each to dealer and player, | &#9745;
||minimum bet of $50 is applied automatically, | &#9745;
||cash value is updated, | &#9745;
||poker chips are grayed out, | &#9745;
||starts the countdown timer, | &#9745;
||updates dealer/player sums and remaining cards, | &#9745;
||Hit, Split*, Stand buttons become visible. | &#9745;
|||
| `Hit` button | Plays card animation, | &#9745;
||deals 1 card to the player, | &#9745;
||updates player sum and remaining cards. | &#9745;
|||
| `Stand` button | Plays card animation, | &#9745;
||the dealer draws until at least 17 points are reached, | &#9745;
||updates dealer sum and remaining cards, | &#9745;
||win/loss conditions are unlocked. | &#9745;
|||
| `Split`* button | Only appears when 2 same-value cards are drawn at the start of a round, | &#9745;
||sets aside one of those cards*, | &#9745;
||*(only if player has enough cash to match initial bet value), | &#9745;
||copies current bet value and updates 'Side Bet: $XX', | &#9745;
||updates player cash value accordingly, | &#9745;
||before starting a brand new round, puts the split card into play. | &#9745;
|||
| `Poker Chips` | Play sound effects for a poker chip, | &#9745;
||add/subtract correct amounts. | &#9745;
|||
| Win/Loss Conditions: ||
|||
| The player going over 21 | 'aww' sound effect played, | &#9745;
||'You Lose' is displayed in red below the player sum, | &#9745;
||the player loses the current bet value, | &#9745;
||table clears cards away, | &#9745;
||dealer *doesn't* unnecessarily take its turn, | &#9745;
||The 'Deal' Button becomes visible, | &#9745;
||poker chips become usable again, | &#9745;
||previous bet value is automatically played, | &#9745;
||and player cash value is updated. | &#9745;
|||
| Player sum > dealer sum | 'ding' and 'poker chip winnings' sound effects played, | &#9745;
| -OR- | 'You Won!' is displayed in green below the player sum, | &#9745;
| dealer goes bust (above 21)| player doubles their bet, | &#9745;
||table clears cards away, | &#9745;
||The 'Deal' Button becomes visible, | &#9745;
||poker chips become usable again, | &#9745;
||previous bet value is automatically played, | &#9745;
||and player cash value is updated. | &#9745;
|||
| The timer runs out | Game is stopped, | &#9745;
||score screen pops up, | &#9745;
||correct score calculations (bet value + (side bet value)** + cash value) | &#9745;
||correct .innerHTML depending on which condition was met | &#9745;
||correctly displaying the top 3 scores. | &#9745;
|||
| The score screen `Close` button | Closes the score screen and allows the player to play a new round. | &#9745;
|||

*Split button only available if *initial* two cards are identical.\
**If currently active.

## __Challenges & Bugs__

### __Challenges__

The biggest challenge of this project was realising that a global leaderboard was not as simple as 'simply uploading data to the internet'. I learned a global leaderboard would require a server and a database of some sort (in this case a simple text/JSON file would have sufficed).

I even went as far as purchasing a Raspberry Pi to serve this purpose and did a substantial amount of research on how to 'build' a server. After everything, the part at which I felt I needed to let go of this ambition (for now!), is when I realised that GitHub pages would only communicate with a server over HTTPS. My server would have only been on HTTP, and that extra layer of complexity, and given the time I had to finish the project meant I had to unfortunately postpone my ambition to create a global leaderboard.

Another notable challenge was W3C validation:
  * The 'main game area' section in index.html did not have an h1-h6 element in it, which the validator did not like. I was too far into development to make a fundamental change to this, so I simply opted to change it to a div.

### __Fixed Bugs__
* Buttons correctly display and hide when they need to.
* Poker chips:
  * Now correctly function even if the player's hand is busted.
    * Previously would only function when the player chose to 'stand'.
  * The white 'deduct $100' poker chip now takes into account if the player has below $100 in bet value.
* If the timer ran out while in the middle of a hand; game elements would not correctly display/function on reset.
* Split button:
  * Now correctly hides if the player chooses to stand.
    * Previously the player could stand and then click 'Split' anyway - breaking the game.
  * When the split card comes into play, now correctly calculates win/loss cash values.
* Bet values are correctly calculated under all circumstances.
  * Previously bets over a certain amount would cause a bug in calculations.

### __Unfixed Bugs__
* I have found that on 'Chromium' (Version 1.39.120, 102.0.5005.99 Official Build) the 'Game Rules' section's scroll feature was not functioning as intended, instead, the entire section was on display, and viewing the bottom of the game rules meant users that were affected had to 'scroll away' from the game. Image of proper function below:\
![Scroll Bug](/documentation/bugs-rules-scroll.png)

## Technologies Used
* HTML
* CSS
* JavaScript
* Procreate (iPad)
* Endless Paper (iPad)

## Deployment
The project was deployed on GitHub pages from the 'Main Branch Source Code' using the following steps:
* 'git add .', 'git commit" and 'git push' commands were issued one final time when the project was ready and finished.
* On Github the repository for the project was selected.
* Click the 'Settings' tab.
* On the left; select 'Pages'.
* From here; select the source as 'Main Branch'.
* Click 'Save'.

GitHub may take a few minutes to deploy the website so be patient.

The live link to my project can be found [**here**](https://destant.github.io/blackjack-3-minute-challenge/).

## Development
Should anyone wish to add to the project, please feel free to develop it on a separate branch; then create a pull request and I will review and merge it. Thank you!

Should anyone wish to copy and paste the project - you are also welcome to - please remember to give me some credit!

## Credits 

### __Content__
* The wireframe was made using the [Endless Paper App](https://endlesspaper.app/) on the iPad.
* To help me find and visualize the font I used [Fontjoy](https://fontjoy.com/).
* [W3Schools](https://www.w3schools.com/), [Stack Overflow](https://stackoverflow.com/), and [Mozilla Dev Tools](https://developer.mozilla.org) were referred to a lot for general syntax and whenever I was stuck on a bug for a while - other similar experiences helped me build a better app.
* [FontAwesome](https://fontawesome.com/) for the "X" mark in the pop-up modal.
* [Favicon](https://favicon.io/emoji-favicons/game-die/) for the favicons.

### __Media__
* The poker chip images are from [PngAAA](https://www.pngaaa.com/).
* The playing cards .png are from [Super Dev Resources](https://superdevresources.com/free-playing-cards-set/).
* The sound effects are from [Epidemic Sound](https://www.epidemicsound.com/).
* To compress .PNG [CompressPNG](https://compresspng.com/).

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
