# HANG-MAN
Hang-man is a word-guessing game with a timer to track your progress and how long it will take for you to win or lose. 
It is very straightforward and easy to play. It allows you to visually see how far you have come whether its a win and the letters are displayed, or, the hang-man is visually developed as you guess the wrong letters. 
Link to hang-man https://hangmann-461bf35a6e08.herokuapp.com/

## HOW TO PLAY
1. The computer will choose a secret word.
2. You have to guess one letter at a time.
3. You can only guess letters (no numbers or special characters).
4. You have a limited number of incorrect guesses before you lose the game.
5. Try to guess the word before you run out of guesses!
6. Good luck and have fun!

## USER STORIES
As a first time user, I want to understand the game so I can begin guessing straight away. 
As a first time user, I want to cover the rules so I am aware of how many times I can try before I lose. 

As a frequent visitor, I want to be able to challenge myself with new words to guess. 

## FEATURES
Welcome and How to play: 
![Alt text](<images/features 11.png>)
The game starts by prompting you that you have 7 lives, which is exciting since you do not know what will come your way. It shows you how many letters are in the word and allows you to make your first guess
![Alt text](<images/features 1.png>)
There is a timer going on and it times how long it takes for the user to finish the game. There is a feature to warn the user if the letter they have picked is right/wrong and how many lives they have left. You can also see the hangman forming everytime the user gets a letter wrong. 
![Alt text](<images/features 2.png>)
When the user wins, there is a text telling them so. They then can choose if they want to play again or quit by answering yes or no. 
![Alt text](<images/features 3.png>)
The user is notified that they have no more lives left and the hangman is fully formed to support the text. They can again choose to play or quit the next round. 
![Alt text](<images/features 4.png>)

## FLOWCHART
The flowchart represents the logic that has been followed: 
![Alt text](images/flowchart.png)

## TECHNOLOGIES USED
### Languages
Python 3.8.5: used to anchor the project and direct all application behavior

### Built in Packages
random  -  Python Random module is an in-built module of Python that is used to generate random numbers in Python. These are pseudo-random numbers means they are not truly random. This module can be used to perform random actions such as generating random numbers, printing random a value for a list or string, etc.
string - The built-in string class provides the ability to do complex variable substitutions and value formatting
time - the time module is another built-in way to get the current time in Python. 

### Other Tools
VSCode was used as the main tool to write and edit code.
GitHub was used to host the code of the website.

## Bugs
The lines were too long so I have made sure they were shorter than 79. However, the blank lines were unresolved.
![Alt text](<images/CI VALIDATOR.png>)

## Deployment
The program was deployed to Heroku.
This project requires you to have Python installed on your local PC.

Create a local copy of the GitHub repository by following one of the two processes below:

Clone the repository:

Open a folder on your computer with the terminal.
Run the following command
git clone https://github.com/Melisaavr/hang-man.git
Create your own GitHub repository to host the code.

Run the command git remote set-url origin <Your GitHub Repo Path> to set the remote repository location to your repository.

Push the files to your repository with the following command: git push

Create a Heroku account if you don't already have one here Heroku.

Create a new Heroku application on the following page here New Heroku App:

Create a new Heroku application
![Alt text](<images/heroku 1.png>)

Go to the Deploy tab:
![Alt text](<images/heroku 2.png>)

Link your GitHub account and connect the application to the repository you created.
![Alt text](<images/heroku 3.png>)

Go to the Settings tab:
![Alt text](<images/heroku 4.png>)

Click "Add buildpack":
![Alt text](<images/heroku 5.png>)

Add the Python and Node.js buildpacks in the following order:
![Alt text](<images/heroku 6.png>)

Click "Reveal Config Vars."
![Alt text](<images/heroku 7.png>)

Add 1 new Config Vars:

Key: PORT Value: 8000
This Config was provided by CODE INSTITUTE.

Go back to the Deploy tab:
![Alt text](<images/heroku 8.png>)

Click "Deploy Branch":
![Alt text](<images/heroku 9.png>)

Wait for the completion of the deployment.
![Alt text](<images/heroku 10.png>)

Click "Open app" to launch the application inside a web page.
![Alt text](<images/heroku 11.png>)


## Credits
How to add a timer on Python https://www.youtube.com/watch?v=KseiSR0MCTI&ab_channel=BroCode



