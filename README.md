# WordlePlayer
Team: Anghel Fabian, Grigore Mihai, Bobic Teona

***Description***
In this project, we created a Wordle Game, that includes also a program that allows a human to play the game by himself and a program that let's you see how a computer can play the game, on his own. As a team, we also used the Shannon Entropy to ifnd the average number of guesses. As you may know, at a conceptual level, Shannon's Entropy is simply the "amount of information" in a variable.

***How to use***
The project features two different programs, one for the game and one as a player. To try the game yourself, run the wordle.py script. If you'd rather watch the computer play or if you'd like to recalculate the results, simply run the player.py script. 

The current average number of guesses is: 4.5858215470577965

***How to play as a human***
As we said before, you will have to run the wordle.py script. The game will generate a random word that you will have to guess in this way: at every step you will try to guess the word by writing a 5 letter word. The program will return your results based on what letters your words has. For example, you will be given a 'X' if the letter is in the right position, a '*' if the letter appears in the word but not in that position, or a '_' if you didn't guess the letter. The game ends, when the player succeds in finding the word.
The program calculates the frequency of the letters of the word. After that it will verify if the word has been guess, or if any of the letters are correct. This will happen until the word is found repeatedly.

***How to watch the computer play***
For the computer to be able to play the wordle game, might be a little tricky. The logic of the program works like this: at every step, the wordle player tries the most likely word, given its current knowledge. This is determined by comparing the frequencies of each letter on each position in the set of words that might be the correct one against every word. To understand better, the computer uses also the solution.py in order to find faster the word. 
The program starts by creating a dictionary and calculating the frequency for every letter. It 'looks' in the word list that it has and after verifying that the word is not the correct one, it will eliminate the words that have the wrong letters in the wrong positions. The probability of each word is being calculated and then the computer will look after the word with the highest probability. This will take place, until the word is being found. 

***How to recalculate the results***
In order to recalculate the results for each word and ,in this way, rewrite the 'guess path', you will have to run the player.py script. This will write the 'guess path' for every word in the dictionary in solutii.txt, along with the average number of guesses. The program uses the solution.py script in order to succesfully write the 'guess path' for every word.


