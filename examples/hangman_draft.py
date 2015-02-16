import random


HANGMAN = [

""""
------
|    |
|
|
|
|
|
|
|
------
""",
""""
------
|    |
|    0
|
|
|
|
|
|
------
""",
""""
------
|    |
|    0
|   -+-
|
|
|
|
|
------
""",
""""
------
|    |
|    0
|  /-+-
|
|
|
|
|
------
""",

""""
------
|    |
|    0
|  /-+-/
|    |
|    
|   
|
|
------
""",
""""
------
|    |
|    0
|  /-+-/
|    |
|    | 
|   
|
|
------
""",
""""
------
|    |
|    0
|  /-+-/
|    |
|    | 
|   /
|
|
------
""",
""""
------
|    |
|    0
|  /-+-/
|    |
|    | 
|   / \\
|
|
------
"""
]

#Create a variable to store how many
#chances the player has to guess the word
MAX_WRONG = len(HANGMAN) - 1

#Create a list of words, the secret word will be one of these
#Call the list "WORDS"

#Generate a random word from our list of words
word = random.choice(WORDS)

#Create a string that has one dash for each letter in the secret word
so_far = "-"*len(word)

#Create a variable to store the number of wrong guesses player has made
#Call the variable "wrong"

#Create a list to store all the letters used
#Call the list "used"


print "Welcome to Hangman. Good luck!"


while wrong < MAX_WRONG and so_far != word:
    print HANGMAN[wrong]

    #Ask the user to take a guess
    #store the answer in a variable named "guess"

    #Convert user guess to lower case

    #Update the list of used characters
    used.append(guess)

    #Check if the guessed letter is in the word
    if guess in word:
		print "Yes! %s is in the word" % guess

        #Create a temporary emptry string
		new = ""

        #create a temporary string that has
        #the letters guessed previously
        #and the new letter inserted
        #in the right position
		for i in range(0, len(word)):
			if guess == word[i]:
				new = new + guess
			else:
				new = new + so_far[i]
		
		so_far = new

    else:
        print "Sorry %s is NOT in the word." % guess
        wrong += 1

    #Print the variable showing the guessed characters/word so far
    print "\nSo far, the word is: %s " % so_far

    #Print a message showing the letters used up to this point
    print "\nYou've used the following letters:\n", used


if wrong == MAX_WRONG:
    #print hangman from HANGMAN
	print "You've been hanged!"

else:
    #Output a message to the player
    #saying they won
	print "You guessed it!"

#print the word




