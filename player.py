from multiprocessing import connection, Process, Pipe
import utility
import solution
import wordle

def play(chosen_word=None, log_file=None):
    #creating pipe
    player_conn, game_conn = Pipe()

    #creating processes
    player_process=Process(target=solution.solve, args=(player_conn,))
    game_process=Process(target=wordle.play, args=(game_conn, chosen_word, log_file))

    #starting processes
    game_process.start()
    player_process.start()

    #waiting for processes to finish execution and joining threads
    game_process.join()
    player_process.join()

    #close pipe
    player_conn.close()
    game_conn.close()

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

def full_test(log_file):
    #open dictionary file and get words
    dict=open("cuvinte_wordle.txt", 'r')
    word_list=[x for x in dict.read().strip('\n').split()]

    #wipe data in log file
    open(log_file, 'w').close()

    #play for each word
    for i in range(len(word_list)):
        print(i)
        play(word_list[i], log_file)

    calculate_average_guesses(log_file)

if __name__ == '__main__':
    full_test('solutii.txt')
