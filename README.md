# WordlePlayer
Team: Anghel Fabian, Grigore Mihai, Bobic Teona

***Description***

This project consists of a Wordle Game and a Wordle Player, both of which use words from the 'cuvinte_wordle.txt' dictionary file.

***Requirements***
Python 3.11 (functionality on other versions is not guaranteed)

***How to use***

The project features two different programs, one for the game and one for the computer player. To try the game yourself, run the wordle.py script and start guessing (see the 'How to play as a human' section for more details). If you'd rather watch the computer play or if you'd like to recalculate the results, run the player.py script using the following arguments:

(nothing) : defaults to '-s'
-s : (single) watch the computer play one game
-f : (full test) recalculate the results and save them in 'solutii.txt' (also prints the average number of guesses at the end of the file)
-v : verbose, only useful in combination with '-f', prints to the console data regarding the current progress of the test

The current average number of guesses is: 4.560502881089576

***How to play as a human***

As stated before, firstly run the wordle.py script. The game will choose a random word from the dictionary, after which you will try to guess the word by writing a 5 letter word (in CAPS). The program will return a response based on what letters your words has. In each position, you will be given an 'x' if the letter in that position in your guess is correct, an '*' if the letter appears in the word but not in that position, or a '-' if you letter does not appear in the word at all. The game ends when you succeed in finding the word.

***How recalculation of the results works***

Using the '-f' (full test) option will overwrite the 'solutii.txt' file with the new guess path for each word of the dictionary, one on each line. The guess path starts with the word to be guessed, followed by the words the player program tried in order to arrive at the correct answer. On the last line of the file the new average number of guesses will be printed.

***How the player program works***

The player program calculates the entropy (i.e. the average amount of information that a word offers) of each possible word. This may not be the maximal entropy across the entire dictionary, but this is a simple way to balance the amount of information gained with each guess with the probability of each guess being correct (thus making it possible to guess without knowing all the necessary information). In addition, words with duplicate letters are discouraged. It then chooses the word that ranks highest as its guess and repeats this process until it arrives at the correct answer.

***Extra features***
Parallel processing:
To speed up the full dictionary test, the program starts multiple worker processes and assigns to each of them a part of the dictionary. This way the computation is done in parallel, using more resources and saving time.
