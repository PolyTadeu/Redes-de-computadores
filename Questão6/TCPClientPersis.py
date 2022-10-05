from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort)) 
while(True):
    sentence = input()
    clientSocket.send(sentence.encode())
    message = clientSocket.recv(1024)
    print(message.decode())
    if "Até logo!" in message.decode():
        break
clientSocket.close()
