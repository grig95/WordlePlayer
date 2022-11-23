from multiprocessing import connection, Process, Pipe, Queue
import utility
import solution
import wordle
import os
from math import ceil

def play(chosen_word=None, log_file=None, debug_mode=False):
    #creating pipe
    player_conn, game_conn = Pipe()

    #creating player process
    player_process=Process(target=solution.solve, args=(player_conn, debug_mode))

    #starting player process
    player_process.start()

    #running game on current process and saving guess_list
    guess_list = wordle.play(game_conn, chosen_word, log_file, debug_mode)

    #waiting for processes to finish execution and joining threads
    player_process.join()

    #close pipe
    player_conn.close()
    game_conn.close()

    #return guesses
    return guess_list

def calculate_average_guesses(log_file):
    file=open(log_file, 'r')
    lines=[line for line in file.read().strip('\n').split('\n')]

    total=0
    for line in lines:
        total+=len(line.split())-1

    result=total/len(lines)
    file.close()
    file=open(log_file, 'a')
    file.write(str(result))


def partial_test(id, words, queue):
    guesses=[]
    for word in words:
        guesses.append(play(word))
    queue.put((id, guesses))


def full_test(log_file):
    #open dictionary file and get words
    dict=open("cuvinte_wordle.txt", 'r')
    word_list=[x for x in dict.read().strip('\n').split()]

    #wipe data in log file
    open(log_file, 'w').close()

    #create Queue for results
    queue=Queue()

    # !!! os.cpu_count() actually reports the number of LOGICAL CORES !!!
    process_count=int(os.cpu_count()/2)-1 # 2 'cores' are needed for each game-player instance
    words_per_process=ceil(len(word_list)/process_count)
    processes=[Process(target=partial_test, args=(x, word_list[x*words_per_process:(x+1)*words_per_process], queue)) for x in range(process_count)]

    #start worker processes
    for process in processes:
        process.start()

    #get results
    results=[[] for _ in range(process_count)]
    for i in range(process_count):
        res=queue.get()
        results[res[0]]=res[1].copy()

    #join processes
    for process in processes:
        process.join()

    #output results in log_file
    file=open(log_file, 'w')
    for r in results:
        for result in r:
            file.write(result[-1]+' ')
            for r in result:
                file.write(r+' ')
            file.write('\n')
    file.close()

    calculate_average_guesses(log_file)


if __name__ == '__main__':
    full_test('solutii.txt')
