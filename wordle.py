from random import randint
from multiprocessing import connection

#Word length constant
WORD_LENGTH = 5

#Takes input from the connection with the player process or from stdin.
#Should always be used in play().
def get_input(conn = None):
    if conn is None:
        return input()
    else:
        return conn.recv()

#Sends the output through the connection to the player process or to stdout.
#Should always be used in play().
def send_output(output, conn = None):
    if conn is None:
        print(output)
    else:
        conn.send(output)


#Takes a connection as argument through which to communicate with the player process.
#If None, the game will run in human-playable format.
def play(conn = None):

    #init word database
    file=open('cuvinte_wordle.txt')
    words=file.read().strip('\n').split('\n')

    #choose random word and generate letter frequency array
    chosen_word=words[randint(0, len(words)-1)]
    letter_frequency=[0 for i in range(26)]
    for c in chosen_word:
        letter_frequency[ord(c)-ord('A')]+=1

    #init variables
    guess=str()
    counter=0

    #game loop
    while guess != chosen_word:
        counter+=1
        guess=get_input(conn)
        #generate guess reply where reply[i] is:
        # x, if guess[i]==chosen_word[i]
        # *, if guess[i] is found in chosen_word, but not in that position
        # -, otherwise
        reply=str()
        for i in range(WORD_LENGTH):
            if guess[i] == chosen_word[i]:
                reply+='x'
            elif letter_frequency[ord(guess[i])-ord('A')] > 0:
                reply+='*'
            else:
                reply+='-'
        send_output(reply, conn)

    #send/print total number of tries
    send_output(counter)


if __name__ == '__main__':
    play()
