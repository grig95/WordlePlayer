from random import randint
from multiprocessing import connection
import utility
#Use utility.get_input and utility.send_output to get/send data to variable pipes


#globals
guess_list=[]

def log_guesses(log_file):
    file=open(log_file, 'a')
    file.write(guess_list[-1]+' ')
    for guess in guess_list:
        file.write(guess+' ')
    file.write('\n')

#Takes as arguments a connection through which to communicate with the player process, a chosen word and
#a log file name.
#If the connection is None, the game will run in human-playable format.
#If the chosen word is None, the game will pick one at random.
#If the log file name is not None, the game will save the guesses in the specified file, in the specified format
#(i.e. solution, guess1, guess2,... guessN=solution).
def play(conn = None, chosen_word=None, log_file=None, debug_mode=False):
    #mark globals
    global guess_list

    #init word database
    file=open('cuvinte_wordle.txt')
    words=file.read().strip('\n').split('\n')

    #choose random word (if not imposed) and generate letter frequency array
    if chosen_word is None:
        chosen_word=words[randint(0, len(words)-1)]
    letter_frequency=[0 for i in range(26)]
    for c in chosen_word:
        letter_frequency[ord(c)-ord('A')]+=1

    #init variables
    guess=str()
    counter=0
    guess_list=[]

    #game loop
    while guess != chosen_word:
        counter+=1
        guess=utility.get_input(conn)
        guess_list.append(guess)
        #generate guess reply where reply[i] is:
        # x, if guess[i]==chosen_word[i]
        # *, if guess[i] is found in chosen_word, but not in that position
        # -, otherwise
        reply=str()
        for i in range(5):
            if guess[i] == chosen_word[i]:
                reply+='x'
            elif letter_frequency[ord(guess[i])-ord('A')] > 0:
                reply+='*'
            else:
                reply+='-'
        utility.send_output(reply, conn)

    #send/print total number of tries
    utility.send_output(counter, conn)

    #log guesses if required
    if log_file is not None:
        log_guesses(log_file)
    return guess_list


if __name__ == '__main__':
    play()
