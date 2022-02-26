## Hangman Game

 * A hangman game application where the player will have to guess letters (A-Z) to form the words on the line, If the player will have to gusses the right letter that is within a word. The letter will appear on its correct posistion. The player will then guess the correct world until the man is hung when this appear the game will be done.

* The hangman game will include a login and sign up, this will be stored in MogoDB.

 * Link to webpage 
 [thehangmangame](https://samanthakwenaeetile.github.io/Hang_Game1/) - you can view the live site with this link.

* The image of the live site.
![Am I Responsive?] <img width="1437" alt="Screenshot 2022-02-26 at 6 05 52 am" src="https://user-images.githubusercontent.com/74901613/155832002-6e644ec9-8b2a-4123-b4b8-014175237971.png">


# *How the user will play the hangman game *

* The player of the hangman game will have to input a command into the mock terminal, when they enter a letter into the game which they will have gussed it will infrom the user if the letter they have enterd is the correct letter or word they have gussed. If it is the correct word they will have won the game if it is the incorrect letter or word an error message will then display it self and the user will then be asked to resubmit thier choice again.

* Design flowchart
![20220226_064124](https://user-images.githubusercontent.com/74901613/155832863-72dd4bcc-6eaa-4c56-ac53-323985eac39c.jpg)


* wireframe (image)

![20220226_065852](https://user-images.githubusercontent.com/74901613/155834444-c2dd15cb-c480-422a-8930-594e24fa5eb1.jpg)

### **User Goals**

1.  The game should be easy to play
2.  The game be fun for the user to get them to keep coming back
3.  Challenge the player by adding lives to keep the user intersted in the game 

Target Audience
*  player 16 and over
*  I love for spelling 
 
## ** Features **
### ** Existing features in game**

1. Can view lives while playing the game 
* the user has a certain amount of lives before the game is over, it can be seen while the player is playing the game, it is also represtend along side the hangman being built at each turn when a life is lost.

2. Can view the rules of the game
* the words will be picked in randomly from a word list.
* the number of letters in a word will be showen by _ _ _ _ .

3. Game will check invalid inputs 
* all the inputs that the player will enter , checks will run to ensure that the is no invalid inputs that have been submitted - all invalid inputs will be followed by a error message letting the player know to try again.

* Features  that i could have done to improve the game.

1. Banner 

2. Main Menu

3. Login

4. Sign Up

6. Support 

# ** Technologies **
* Languages 

 Python

# ** Testing **

* The testing which i have done for the hangman game project are :

1. I tested the python code using a PEP8 linter website and then i fixed any erros. 
(http://pep8online.com/) 

2. I tested in the terninal and also on the site heroku which i used to deploye the site.

3. I manually tested the user inputs by entering the wrong data to confrim any error messages.

## **Validators**
* PEP8 - No errors returned from (http://pep8online.com/).

* Deployment 

 The website was deployed using GitHub to Heroku by following these steps: 

1. Create an account at heroku.com
2. Create a new app, add app name and your region
3. Click on create app
4. Go to "Settings"
Under Config Vars, add your sensitive data (the MongoDB URL for example)
For this project, set buildpacks to and in that order.
Go to "Deploy" and at "Deployment method", click on "Connect to Github"
Enter your repository name and click on it.
Choose the branch you want to buid your app from, and click "Deploy branch".
You can for fork the repository by following these steps:

Go to the GitHub repository
Click on Fork button in upper right hand corner
You can clone the repository by following these steps:

Go to the GitHub repository
Locate the Code button above the list of files and click it
Select if you prefere to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
Open Git Bash
Change the current working directory to the one where you want the cloned directory
Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
Press Enter to create your local clone


# Credits 

* [Code Institute](https://codeinstitute.net/) for the mock terminal for the deploy to a live site.

* [Python Hang Man tutorial] :
1. 
2. 
3. 
4. * [ASCII Art Generator](https://patorjk.com/software/taag/#p=display&h=2&f=Soft&t=The%20Hangman%20game) - for creating word art for game 

### **Thanks**
* code Institute mentors who adived and thier guidance and support on the completion of this project.