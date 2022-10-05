from socket import *
from multiprocessing import Process

def recive_client_request(message, clientAddress, serverSocket):
    modifiedMessage = message.decode().upper() 
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    return

if __name__ == '__main__': #fork to start child processes
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM) 
    serverSocket.bind(('', serverPort)) 
    while True:
        print("The server is ready to receive")
        message, clientAddress = serverSocket.recvfrom(2048)
        p = Process(target=recive_client_request, args=(message, clientAddress, serverSocket))
        p.start()
