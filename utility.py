from multiprocessing import connection

#set to True to see data exchange in console
DEBUG_MODE=False

#Gets input from either connection conn or stdin
def get_input(conn = None):
    if conn is None:
        return input()
    else:
        return conn.recv()

#Sends output to either connection conn or stdout
#Setting debug_mode to True will also print the output to console
def send_output(output, conn = None, debug_mode=False):
    global DEBUG_MODE
    if conn is None:
        print(output)
    else:
        conn.send(output)
        if DEBUG_MODE or debug_mode:
            print(output)
