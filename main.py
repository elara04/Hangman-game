
# -*- coding: utf-8 -*-
"""
Edgar Lara
CPSC 362: Software Engineering
Open Source 3
sunday Apr 24, 2022

"""

import random
from datetime import datetime

# Hangman class.
class Hangman:
    
    def __init__(self,word, triesAllowed):
        pass

    def Guess(self,):
        """Pass in a letter (length = 1) and check to see if it is in the word.
            If it is, replace blanks in display word with letter and return True
            If not, decrement the number of tries left and return False
        """
        pass
            
                

    def GetNumTriesLeft(self):
        """Return the number of tries left"""
        pass
    
    def GetDisplayWord(self):
        """Return the display word (with dashes where letters have not been guessed)
        i.e. the word happy with only the letter 'p' guessed so far would be '--pp-'"""
        pass
    
    def GetLettersUsed(self):
        """Return a string with the list of letters that have been used"""
        pass
        

    def GetGameResult(self):
        """Return True if all letters have been guessed. False otherwise"""
        pass

    def DrawPerson(self):
        """Optional: Return string representing state of gallows"""
        pass

# implement the logic of your game below
if __name__=="__main__":
    # Read all the words from the hangman_words.txt file
    wordFile = open("hangman_words.txt", "r")
    wordFileText = wordFile.read()
    wordFile.close()
    list_of_words = wordFileText.split()
    # Seed the random number generator with current system time
    
   
    # Convert the string of words in wordFile to a list,
    
    # then get a random word using
    # randomIndex = random.randint(min, max)
    randomIndex = random.randint(0, len(list_of_words))
    word_for_game = list_of_words[randomIndex]
    numTries = len(word_for_game)
    
    
    # Instantiate a game using the Hangman class
    #game = Hangman(word_for_game,numTries)
    
    
    print("\nWelcome to Hangman")
    runGame=True
    
   # while runGame:
        
        #  print(f"\nHere's is your word so far: {game.GetDisplayWord()}")
        #  print(f"you have {game.GetNumTriesLeft()} guesses left")
        
        # # get user imput and verify its a letter if not prompt user to pick a leetter
                
        #  start hangman after choice passed the conditions
        # result = game.Guess()
        # if result:
        #     print(f"Good guess! Letters used: {game.GetLettersUsed()}")
           
        # else:
        #      print(f"Too bad! Letters used: {game.GetLettersUsed()}")
             
        # if game.triesAllowed == 0 or game.display_word == game.word:
        #     endGame = game.GetGameResult()
        #     if endGame:
        #         print("Congratulatios! You won!!! The word was", game.word)
        #     else:
        #         print("You lost. The word was", game.word)
        #     runGame = False
       
        
        
        
        
        
        
            
            
    
    
    
    
