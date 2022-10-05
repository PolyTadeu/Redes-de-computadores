from socket import *
from multiprocessing import Pool
from os import getpid

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

def send_message(message):
    clientSocket.sendto(message.encode(),(serverName, serverPort)) 
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 
    print(f"From process {getpid()} recive: {modifiedMessage.decode()}")

if __name__ == '__main__': #fork to start child processes
    messages = ["polyana", "tadeu", "teste", "tp", "paralelismo", "questão3"]
    with Pool(processes=6) as pool:
        pool.map(send_message, messages)
