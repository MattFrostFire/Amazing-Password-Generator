# Amazing-Password-Generator
This Python password generator (core math, os, string, and datetime module) has two modes: random and memorable. Random generates a high security password like google or microsoft does (Ex: _5}/|#~S.4N=~d). Memorable creates a password out of a common word (using top_english_nouns_lower_100000.txt) and adds numbers and a hyphen to it. Memorable and Random folders appear after run.


## a) Purpose of the Program:

  The purpose of this program is to give a user a randomly generated set of Memorable passwords and Random character passwords for personal use
  It generates the Memorable passwords from a txt file containing the top 100000 nouns
  1000 passwords are generated for each folder
  
## b) Input: 

  The program takes the following inputs:
    Path to a txt file containing at least three words with newline (or enter) spaces after each one
    
## c) Expected Output:

  The program prints the generated passwords into two folders "Memorable" and "Random" in the same directory where the .py and .txt files are.
  The memorable and random folders contain .txt files containing their respective generated passwords.
  
## d) Type of Execution:

  The program contains the following types of execution:

      Sequential Execution: The code is executed in a linear order from top to bottom
      Reusable Execution: Functions are used for modular and reusable code blocks.
      Repeatable Execution: A for loop is used to iterate through the lines of the txt file
      Conditional Execution: if/else statements are used to determine if a word starts with an uppercase letter in the Memorable sector or a Random password doesn't have more than one lowercase letter in a row

## e) Possible Improvements:

  The program could be improved by:
    Listing the directory where the folders with the passwords are 
    Adding a toggle for how random you want the Memorable category to be. 
          For example hello0- becomes h3ll0!@-- on high
