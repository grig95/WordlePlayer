import utility
from multiprocessing import connection
import wordle

#globals
word_list=[]
word_dictionary={}
let_freq=[]

#deletes words where there ISN'T a letter on a certain position
def delete_not_equal(letter, position):
    global word_dictionary
    delete_list = []
    for s in word_dictionary:
        if s[position] != letter:
            delete_list.append(s)
    for s in delete_list:
        del word_dictionary[s]

#deletes words where there IS a letter on a certain position
def delete_equal(letter, position):
    global word_dictionary
    delete_list = []
    for s in word_dictionary:
        if s[position] == letter:
            delete_list.append(s)
    for s in delete_list:
        del word_dictionary[s]

#deletes words that don't contain a certain letter
def delete_not_in_word(letter):
    global word_dictionary
    delete_list = []
    for s in word_dictionary:
        if letter not in s:
            delete_list.append(s)
    for s in delete_list:
        del word_dictionary[s]


def solve(conn=None, guess_list_save_file=None):
    #mark global variables
    global word_list
    global word_dictionary
    global let_freq

    #opening and reading the word database and putting it into a dictionary
    file = open("cuvinte_wordle.txt","r")
    word_list = [x for x in file.read().split()]
    word_dictionary = {x: 0 for x in word_list}

    #generating the letter frequency matrix
    reply = ""
    let_freq = []
    for x in range(5):
        let_freq.append([0] * 26)

    #guessing the word
    while reply != "xxxxx":
        maxim = 0
        guess = ""
        nr = 0

        #calculating the frequency of letters on every position
        for x in word_dictionary:
            nr += 1
            for i in range(5):
                let_freq[i][ord(x[i]) - ord('A')] += 1

        #calculating the probability of each word
        for x in word_dictionary:
            word_dictionary[x] = 1
            for i in range(5):
                if x.count(x[i]) > 1:
                    word_dictionary[x] /= 1.5
                word_dictionary[x] *= let_freq[i][ord(x[i]) - ord('A')] / nr

        #searching for the guess (word with highest probability)
        for x in word_dictionary:
            if maxim < word_dictionary[x]:
                maxim = word_dictionary[x]
                guess = x

        #printing guess
        utility.send_output(guess, conn)

        #reading the reply and managing it
        reply = utility.get_input(conn)
        if reply != "xxxxx":
            for i in range(5):
                if reply[i] == 'x': #deleting words that don't have the matching letter
                    delete_not_equal(guess[i], i)
                elif reply[i] == '*': #deleting the words that have the letter on that position or don't contain it
                    delete_equal(guess[i], i)
                    delete_not_in_word(guess[i])
                elif reply[i] == '-': #deleting words that contain the letter
                    for j in range(5):
                        delete_equal(guess[i], j)
                for j in range(26): #reseting the letter frequency matrix
                    let_freq[i][j] = 0
