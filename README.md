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
As a user of the site, I would:
* Enjoy spending a few minutes every so often to play blackjack
* Return to the site to beat my high score
* Share the site with friends so that I could compete with them
* Screenshot the end screen with my top 3 high scores on it to show off to my friends and colleagues

As the owner of the site, I would:
* Listen to feedback from my users and add updates to include new features accordingly
* Fix bugs, as they are reported to me

## Wireframe & Planning
The wireframe:
  * The choice behind the design was to mimic a casino blackjack table and have everything in view for the player.\
![Wireframe](/documentation/wireframe-pp2.png)

The colours:
  * I wanted to include the typical green seen in all casinos, so opted to use that as the background. However, I did not want to overpower the viewing field either and so chose to also include a much lighter shade in the foreground.\
![Colours Used](/documentation/colour-choice.png)

The typography:
  * The typography was chosen for its simplicity and elegance.\
![Typography](/documentation/typography.png)

## Features:
### First Visit
![Input Name Pop-Up](/documentation/input-name-screen.png)
* On the first visit, the player is greeted with this pop-up modal window.
  * The player must input their name (minimum 2 characters, maximum 15).
  * The name is stored in localStorage.
  * The 'Game Rules' will display the player's name.\
  ![Greeting Player](/documentation/hi-player-name.png)
* On subsequent visits (i.e. if localStorage already has name data), the game will welcome the player back.\
![Welcome Back Player](/documentation/welcome-back-player-name.png)
* If the player wishes to change their name; they can click on their name in the 'Game Rules' section.

### The Deck Of Cards
The deck of cards is displayed on the side of the screen.
* It has a 'remaining' cards counter
* When the deck is below 15, it will reshuffle into a new deck
* It isn't explicitly stated, but the choice behind having a remaining card counter and only using one deck of cards was primarily because I wanted to give observant players an edge when it comes to card counting.\
![Draw Deck](/documentation/draw-deck.png)

### The 'Hit', 'Split' and 'Stand' Functions

#### __Hit__
![Hit Function](/documentation/function-hit.png)
![Player Sum](/documentation/player-sum.png)
* As long as the player has a sum below 21 the 'Hit' function allows the player to draw another card.
* Aces are automatically considered at their higher value of 11.
  * When the player exceeds 21 and holds an ace(s), one ace at a time is automatically recalculated to be worth 1 instead until a score of 21 or below is reached.
* If the player exceeds 21; the round is automatically lost and the 'aww' sound effect is played.
  * The 'Deal' button is revealed to deal out the new round.\
![Deal Button](/documentation/deal-button.png)

![Blackjack, 21](/documentation/perfect-score.png)
![Player Sum 21](/documentation/player-sum-21.png)
* When the player has 21 points exactly, the 'Hit' button will grey out and stop functioning.
  * This is to stop accidental clicks when the player has the best score.

#### __Split__
![Split Function](/documentation/function-split.png)
* If two identical cards are dealt at the beginning of a round, the 'Split' button will appear.
  * Players can decide to split or continue playing as normal.

![Split Function Pressed](/documentation/after-split.png)
* If the player decides to split, the left card is put aside (as seen in the image - bordered in red).
  * A side bet, matching the original bet, is created (as seen in the image - blue border).
    * Split bets can only be initiated if the player has enough cash to match the original bet.
  * The 'Player Sum' is updated (green border).
* Once the first card is played, the second card is put into play.

#### __Stand__
* Once the player is happy with their score, they can choose to 'Stand'
  * This initiates the dealer's turn:
    * The dealer will automatically draw cards until their obligation to score at least 17 is met.
  * Once the dealer has had their turn:
    * If the dealer is busted (score above 21); the player wins and cashes out double their bet.
    * Likewise; if the player has a higher score than the dealer.
      * The winning 'ding' sound is played.
      * The 'You Won!' text pops up for 1.5s below the 'Player Sum'.\
      ![Win Text](/documentation/win-text.png)
    * If the dealer exceeds the player's score; the player loses and loses their bet.
      * The 'aww' sound effect is played.
      * The 'You Lose.' text pops up for 1.5s below the 'Player Sum'.\
      ![Lose Text](/documentation/lose-text.png)
    * In case of a draw; nobody wins, the player retains their bet.
      * The 'Draw!' text pops up for 1.5s below the 'Player Sum'.\
      ![Draw Text](/documentation/draw-text.png)

### The Poker Chips and Betting
![The Poker Chips](/documentation/poker-chips.png)
* The player can click on the poker chips to add to or remove from their bet\
![Total Bet Value](/documentation/total-bet.png)
* Players can only remove a bet in multiples of $100 (as seen in the image; the white poker chip)
  * It is still possible to remove bets below $100. The game checks for this and adjusts accordingly.
* Cash value and bet value are adjusted with every click.
* Animations of chips moving to and from the bet value and hand are played.
* Poker chips will grey out when the player is not allowed to interact with them. And toggle back on when the player can again interact with them.\
![Greyed Out Poker Chips](/documentation/grey-poker-chips.png)

### End Game Score Screen
![Score Screen](/documentation/score-screen.png)
* Once the 3-minute timer runs out at the top of the screen the game will stop and the player will be greeted with the 'Score Screen'
  * The player's cash value, bet value, and (if they have) their side bet value will be tallied up.
  * The total will be stored on localStorage and compared. The top 3 scores will be shown on the scoreboard.
  * If the player has beaten their past high score they will be greeted with a 'Well Done' and an update of their scoreboard\
  ![Beating The Highscore](/documentation/well-done-score-screen.png)
  * If the player failed to beat any of their high scores, they will be greeted with a 'Better luck next time!':\
  ![Better Luck Next Time](/documentation/next-time-score-screen.png)
  * If the player runs out of money before the timer is finished, they will be greeted with this screen instead:\
  ![No Money Score Screen](/documentation/no-money-score-screen.png)
* If the player has had enough before the timer ends or simply wishes to record their high score without risking further losses, then the 'End Game' button can be pressed next to the timer at the top of the screen:\
![End Game Button](/documentation/end-game-button.png)

### Animations
The animations were done using elements of all three; HTML, CSS, and JavaScript. There are currently animations for:
* Poker chips being placed as bets, in their own colours.
* Poker chips being deducted from the current bet (Two $50 chips can be seen being withdrawn).
* Single cards being dealt to each; the dealer and the player.
 
Example Animations:
  * Cards being dealt:\
![Card Animations](/documentation/card-animations.png)
  * Poker chips being withdrawn from the bet:\
![Poker Chip Animations](/documentation/chip-animations.png)

### Sound Effects
There are currently 10 different sound effects in the game, these are:
 * For dealing a single card.
 * When the dealer flips their facedown card to face up.
 * A 'ding' for when the player wins a hand.
 * An 'aww' for when the player loses a hand.
 * Deck shuffle.
 * Two distinctive sounds for when placing a bet..
 * ..and when deducting from a bet.
 * Glass smashing - when the player 'busts' their hand (exceeds 21).
 * A 'boing' sound for when the player does something they shouldn't.
 * And finally the sound of poker chips being pushed around for when the player collects their winnings.

## Future Features/Roadmap

* Implementation of some casino blackjack staple features:
  * 'Double Down' bets
  * 'Insurance' bets
* A server and a database for global leaderboards

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

The game was played for a total of 10+ hours across the board and these were the primary testing criteria used:

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
