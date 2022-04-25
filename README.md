# Hangman-game
my repostitory for the opens source 3 assignment for CPSC 362 it is a python hangman game

# Overview
Everyone has heard of the game "hangman."  Right?  The player tries to guess a preselected word one letter at a time.  If a letter is guessed that is not in the word, a body part is added to the person. If enough letters are missed, then the whole body is drawn on the person and the player loses.  If the player guesses all the letters in the word before the body is fully drawn, they win.

# Background
I'll provide a few elements to help with this task:
- a file containing a list of English words with at least 6 - 12 letters
- a string variable containing the contents of this file
- a list variable from the string of all possible words
- a random word choosen from the list
- a class "skeleton" with several empty member functions for you to implement
- a example_out.txt file with how game output should be when class implemented

# Requirements
Using the English word chosen and the skeleton class. Your code **shall** then get input from the user in the form of a single letter. It **shall** check to see if this letter is in the random word. If it is, the letter **shall** be applied to the word so the user can see where it goes, and a turn attempt **shall NOT** be counted. If the letter is not in the word, an attempt **shall** be counted. The number of attempts allowed by the user will be equal to the number of letters in the word. The code **shall** continue prompting the user for a letter until all of the attempts have been made, or the word has been guessed. You can choose whatever logic you would like, but all member functions of the skeleton Hangman class (except DrawPerson which is optional) **shall** be implemented.


Some things to think about
1. Are you in danger of having an infinite loop?
2. How do you want to display the partial word to the user?
3. Are you keeping track of letters already used?  Don't penalize the player if they forget what they've already guessed.
4. Feel free to add functions to the class, but make sure to implement each one that is there.
