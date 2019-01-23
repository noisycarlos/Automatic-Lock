import time
import lock
import socket
import jwt
#import json

data_is_encrypted = False #Set to False if you want to send commands in plain-text

TCP_IP = '192.168.1.63' #Raspberry Pi's own ip
secret = 'abcdef123456789' #Change this to a random string
TCP_PORT = 8000
BUFFER_SIZE = 1024

conn = None


def close_all():
    lock.close_all()
    conn.close()
    exit()

def reboot():
    lock.close_all()
    conn.close()
    import os
    os.system('sudo reboot')


def process(command):
    global data_is_encrypted
    if(command == 'exit'):
        conn.send("Exiting...\n")
        close_all()
    elif(command == 'encrypt'):
        data_is_encrypted = True
        return "Using Encrypted Commands now.\n" 
    elif(command == 'plain'):
        data_is_encrypted = False
        return "Using Plain-Text Commands now.\n"
    elif(command == 'reboot please'):
        reboot()
        return "You asked for it.\n" 
    elif(command == 'reboot'):
        return "If you ask nicely.\n" 
    elif(command == 'lock'):
        return lock.lock() + "\n"
    elif(command == 'unlock'):
        return lock.unlock()+ "\n"
    elif(command == 'attempt'):
        return "Attempt " + str(attempt_num) + "\n"
    elif(command == 'hello'):
        return "Hi.\n"
    else:
        return command + ' is not a recognized command\n'

def start():
    attempt_num = 1
    while attempt_num <= 5:
        print("Attempt " + str(attempt_num) + " Awaiting connection... " + TCP_IP)

        connected = False
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            print('Binding...')
            s.bind((TCP_IP, TCP_PORT))
            s.listen(1)
            global conn
            conn, addr = s.accept()
            print('Connection address:', addr)
            connected = True
        except socket.error as ex:
            print("Error connecting: " + str(ex))
            time.sleep(5)
            attempt_num += 1

        global data_is_encrypted
        if connected:
            while 1:
                try:
                    data = conn.recv(BUFFER_SIZE)
                    if(not data or len(data) is 0):
                        break
                    data = data.strip()
                    command = data
                    invalid = False

                    if(data_is_encrypted):
                        try:
                            decoded = jwt.decode(data, secret, algorithms=['HS256'])
                            command = str(decoded["command"])
                        except jwt.ExpiredSignatureError:
                            result = command = "Expired Command"                        
                            invalid = True
                        except jwt.exceptions.DecodeError:
                            result = command = "Invalid Code"
                            invalid = True
        
                    print "Received " + command
                    if(not invalid):
                        result = process(command)
                    conn.send(result)
                except Exception as E:
                    print("Exception: " + E.message)
start()
close_all()
